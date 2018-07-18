# -*- coding: utf-8 -*-
from odoo import SUPERUSER_ID, models, fields, api, _
from odoo.addons.base.models.res_users import is_boolean_group, is_selection_groups
from odoo.exceptions import UserError

IR_CONFIG_NAME = 'access_restricted.fields_view_get_uid'


class ResUsers(models.Model):
    _inherit = 'res.users'

    has_group_allow_add_implied_from_settings = fields.Boolean(
        "Allow add implied groups from settings",
        compute='_compute_groups_id', inverse='_inverse_groups_id',
        group_xml_id='access_restricted.group_allow_add_implied_from_settings')

    @api.multi
    def write(self, vals):
        for key in vals:
            if is_boolean_group(key) or is_selection_groups(key):
                self.env['ir.config_parameter'].sudo().set_param(IR_CONFIG_NAME, '0')
                break
        return super(ResUsers, self).write(vals)

    def _inverse_groups_id(self):
        computed_group_fields = [field for field in self._field_computed.keys() if field.compute == '_compute_groups_id']

        for user in self:
            real_uid = (self.env.context or {}).get('uid') or int(self.env['ir.config_parameter'].sudo().get_param(IR_CONFIG_NAME, '0'))

            if real_uid and real_uid != SUPERUSER_ID:
                group_no_one_id = self.env.ref('base.group_no_one').id
                groups = [user[field.name] for field in computed_group_fields if field.name in user._cache]
                domain = [('users', 'not in', [real_uid]), ('id', '!=', group_no_one_id), ('id', 'in', groups)]

                if self.env['res.groups'].search(domain):
                    raise UserError(_('You can\'t escalate the privileges. See documentation of access_restricted module.'))

        super(ResUsers, self)._inverse_groups_id()


class ResGroups(models.Model):
    _inherit = 'res.groups'

    @api.multi
    def write(self, vals):
        context = dict(self.env.context)
        if context.get('config') and self.env['res.users'].has_group('access_restricted.group_allow_add_implied_from_settings'):
            classified = context['config']._get_classified_fields()
            implied_ids = vals.get('implied_ids')
            users = vals.get('users')
            if classified['group']:
                allowed_implied = [group[2].id for group in classified['group']]
            if implied_ids and implied_ids[0][1] in allowed_implied:
                self = self.sudo()
            elif users:
                if not [u[1] for u in users if u[1] in self.users.ids]:
                    self = self.sudo()
        return super(ResGroups, self).write(vals)
