from odoo import SUPERUSER_ID
from odoo import api
from odoo import models
from odoo.addons.base.res.res_users import is_reified_group

IR_CONFIG_NAME = 'access_restricted.fields_view_get_uid'


class ResUsers(models.Model):
    _inherit = 'res.users'

    @api.model
    def fields_view_get(self, view_id=None, view_type='form', **kwargs):
        if view_type == 'form':
            last_uid = self.env['ir.config_parameter'].sudo().get_param(IR_CONFIG_NAME)
            if int(last_uid) != self.env.uid:
                self.env['res.groups'].sudo()._update_user_groups_view()

        return super(ResUsers, self).fields_view_get(view_id=view_id, view_type=view_type, **kwargs)

    @api.multi
    def write(self, vals):
        for key in vals:
            if is_reified_group(key):
                self.env['ir.config_parameter'].sudo().set_param(IR_CONFIG_NAME, '0')
                break
        return super(ResUsers, self).write(vals)


class ResGroups(models.Model):
    _inherit = 'res.groups'

    @api.model
    def _update_user_groups_view(self):
        real_uid = (self.env.context or {}).get('uid', self.env.uid)
        self.env['ir.config_parameter'].sudo().set_param(IR_CONFIG_NAME, real_uid)
        return super(ResGroups, self.sudo())._update_user_groups_view()

    @api.model
    @api.returns('res.groups')
    def get_application_groups(self, domain=None):
        if domain is None:
            domain = []
        domain.append(('share', '=', False))

        real_uid = (self.env.context or {}).get('uid') or int(self.env['ir.config_parameter'].sudo().get_param(IR_CONFIG_NAME, '0'))
        if real_uid and real_uid != SUPERUSER_ID:
            group_no_one_id = self.env.ref('base.group_no_one').id
            domain = domain + ['|', ('users', 'in', [real_uid]), ('id', '=', group_no_one_id)]
        return self.sudo().search(domain)

    @api.multi
    def write(self, vals):
        config = self.env.context.get('config')

        # `isinstance` check is a non-xmplrpc proof.
        if config and isinstance(config, models.Model):
            implied_ids = vals.get('implied_ids')
            classified_group = config._get_classified_fields()['group']
            # when `res.config.settings`'s `execute` method writes the `users` field to group,
            # it is always to remove users and the `users` field is the only key in the write dict
            users = vals.get('users')
            implied_group = implied_ids and implied_ids[0][1]
            users_exclude_operation = users and len(vals) == 1 and all(u[0] == 3 for u in users)
            # ``all(u[0] == 3 for u in users)`` is to be sure that all operations are for removing.
            # `(3, id)` tuple removes the record from the set (the Many2many field `users`)
            add_implied_group_operation = implied_group in [group[2].id for group in classified_group]
            curr_user_allowed = self.env.user._is_superuser() or self.env['res.users'].has_group('access_restricted.group_allow_add_implied_from_settings')
            if users_exclude_operation or add_implied_group_operation and curr_user_allowed:
                self = self.sudo()
            else:
                # do nothing with groups if there is no permission to add from settings
                return
        return super(ResGroups, self).write(vals)
