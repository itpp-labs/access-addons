# -*- coding: utf-8 -*-
from odoo import models, fields


class ResUsers(models.Model):
    _inherit = 'res.users'

    group_apps_access_user = fields.Selection(
        selection=lambda self: self._get_group_selection('access_apps.module_category_access_apps'),
        string="Apps access", compute='_compute_groups_id', inverse='_inverse_groups_id',
        category_xml_id='access_apps.module_category_access_apps')
