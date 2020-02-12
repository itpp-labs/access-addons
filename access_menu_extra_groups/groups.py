# -*- coding: utf-8 -*-
from odoo import SUPERUSER_ID, api, fields, models


class IrUiMenuExtra(models.Model):
    _inherit = "ir.ui.menu"

    extra_groups_id = fields.Many2many(
        "res.groups",
        "ir_ui_menu_extra_group_rel",
        "menu_id",
        "group_id",
        "Extra Groups",
        help="Menu is visible only for users who are in the groups specified in the fields:"
        '"groups_id" and "extra_groups_id".',
    )

    @api.multi
    @api.returns("self")
    def _filter_visible_menus(self):
        menus = super(IrUiMenuExtra, self)._filter_visible_menus()
        if self.env.user.id != SUPERUSER_ID:
            groups = self.env.user.groups_id
            menus = menus.filtered(
                lambda menu: not menu.extra_groups_id or menu.extra_groups_id & groups
            )
        return menus
