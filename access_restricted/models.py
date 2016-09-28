# -*- coding: utf-8 -*-
from openerp import SUPERUSER_ID
from openerp import api
from openerp import models
from openerp.addons.base.res.res_users import is_reified_group
from openerp.tools.translate import _
from openerp.tools import ustr

IR_CONFIG_NAME = 'access_restricted.fields_view_get_uid'


class ResUsers(models.Model):
    _inherit = 'res.users'

    @api.model
    def fields_view_get(self, view_id=None, view_type='form', **kwargs):
        if view_type == 'form':
            last_uid = self.env['ir.config_parameter'].get_param(IR_CONFIG_NAME)
            if int(last_uid) != self.env.uid:
                self.env['res.groups'].sudo().update_user_groups_view()

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
    def update_user_groups_view(self):
        real_uid = (self.env.context or {}).get('uid', self.env.uid)
        self.env['ir.config_parameter'].sudo().set_param(IR_CONFIG_NAME, real_uid)
        return super(ResGroups, self.sudo()).update_user_groups_view()

    @api.model
    @api.returns('res.groups')
    def get_application_groups(self, domain=None):
        if domain is None:
            domain = []
        domain.append(('share', '=', False))

        real_uid = (self.env.context or {}).get('uid') or int(self.env['ir.config_parameter'].get_param(IR_CONFIG_NAME, '0'))
        if real_uid and real_uid != SUPERUSER_ID:
            group_no_one_id = self.env.ref('base.group_no_one').id
            domain = domain + ['|', ('users', 'in', [real_uid]), ('id', '=', group_no_one_id)]
        return self.sudo().search(domain)


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    @api.model
    def _get_classified_fields(self):
        uid = self.env.uid
        classified = super(ResConfigSettings, self)._get_classified_fields()
        if uid == SUPERUSER_ID:
            return classified

        group = []
        for name, groups, implied_group in classified['group']:
            if self.env['res.users'].search_count([('id', '=', uid), ('groups_id', 'in', [implied_group.id])]):
                group.append((name, groups, implied_group))
        classified['group'] = group
        return classified

    @api.model
    def fields_get(self, fields=None, **kwargs):
        uid = self.env.uid
        fields = super(ResConfigSettings, self).fields_get(
            fields, **kwargs)

        if uid == SUPERUSER_ID:
            return fields

        for name in fields:
            if not name.startswith('group_'):
                continue
            f = self._columns[name]
            if self.env['res.users'].has_group(f.implied_group):
                continue

            fields[name].update(
                readonly=True,
                help=ustr(fields[name].get('help', '')) +
                _('\n\nYou don\'t have access to change this settings, because you administration rights are restricted'))
        return fields
