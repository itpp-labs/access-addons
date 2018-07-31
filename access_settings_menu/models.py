# -*- coding: utf-8 -*-
from openerp import models, api, fields


class ResUsers(models.Model):
    _inherit = 'res.users'

    has_group_show_settings_menu = fields.Boolean(
        "Show Settings Menu",
        compute='_compute_groups_id', inverse='_inverse_groups_id',
        group_xml_id='access_settings_menu.group_show_settings_menu')

    @api.model
    def fields_get(self, *args, **kwargs):
        # switch to superuser to get access to virtual fields
        return super(ResUsers, self.sudo()).fields_get(*args, **kwargs)
