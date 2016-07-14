from openerp import models, api, exceptions, SUPERUSER_ID
from openerp.addons.base.res.res_users import is_reified_group
from openerp.tools.translate import _
from openerp.tools import ustr

IR_CONFIG_NAME = 'access_restricted.fields_view_get_uid'


class ResUsers(models.Model):
    _inherit = 'res.users'

    def fields_view_get(self, cr, uid, view_id=None, view_type='form', context=None, toolbar=False, submenu=False):
        if view_type == 'form':
            last_uid = self.pool['ir.config_parameter'].get_param(cr, uid, IR_CONFIG_NAME, context=context)
            if int(last_uid) != uid:
                self.pool['res.groups'].update_user_groups_view(cr, SUPERUSER_ID, context=context)

        return super(ResUsers, self).fields_view_get(cr, uid, view_id, view_type, context, toolbar, submenu)

    @api.multi
    def write(self, vals):
        for key in vals:
            if is_reified_group(key):
                self.env['ir.config_parameter'].sudo().set_param(IR_CONFIG_NAME, '0')
                break
        return super(ResUsers, self).write(vals)


class ResGroups(models.Model):
    _inherit = 'res.groups'

    def update_user_groups_view(self, cr, uid, context=None):
        real_uid = (context or {}).get('uid', uid)
        self.pool['ir.config_parameter'].set_param(cr, SUPERUSER_ID, IR_CONFIG_NAME, real_uid, context=context)
        return super(ResGroups, self).update_user_groups_view(cr, SUPERUSER_ID, context=context)

    def get_application_groups(self, cr, uid, domain=None, context=None):
        if domain is None:
            domain = []
        domain.append(('share', '=', False))

        real_uid = (context or {}).get('uid') or int(self.pool['ir.config_parameter'].get_param(cr, uid, IR_CONFIG_NAME, '0', context=context))
        if real_uid and real_uid != SUPERUSER_ID:
            model_data_obj = self.pool.get('ir.model.data')
            _model, group_no_one_id = model_data_obj.get_object_reference(cr, uid, 'base', 'group_no_one')
            domain = domain + ['|', ('users', 'in', [real_uid]), ('id', '=', group_no_one_id)]
        return self.search(cr, SUPERUSER_ID, domain, context=context)


class res_config_settings(models.TransientModel):
    _inherit = 'res.config.settings'

    def _get_classified_fields(self, cr, uid, context=None):
        classified = super(res_config_settings, self)._get_classified_fields(cr, uid, context=context)
        if uid == SUPERUSER_ID:
            return classified

        group = []
        for name, groups, implied_group in classified['group']:
            if self.pool['res.users'].search_count(cr, uid, [('id', '=', uid), ('groups_id', 'in', [implied_group.id])]):
                group.append((name, groups, implied_group))
        classified['group'] = group
        return classified


    def fields_get(self, cr, uid, fields=None, context=None, write_access=True, attributes=None):
        fields = super(res_config_settings, self).fields_get(
            cr, uid, fields, context, write_access, attributes)

        if uid == SUPERUSER_ID:
            return fields

        for name in fields:
            if not name.startswith('group_'):
                continue
            f = self._columns[name]
            if self.pool['res.users'].has_group(cr, uid, f.implied_group):
                continue

            fields[name].update(
                readonly=True,
                help= ustr(fields[name].get('help', '')) +
                     _('\n\nYou don\'t have access to change this settings, because you administration rights are restricted'))
        return fields
