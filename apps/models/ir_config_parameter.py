# -*- coding: utf-8 -*-
from odoo import api, models

KEY = "apps.super_app_prefix"


class IrConfigParameter(models.Model):
    _inherit = "ir.config_parameter"

    @api.model
    def _recompute_is_super_app(self):
        self.env["ir.module.module"].search([])._compute_is_super_app()

    @api.model
    def create(self, vals):
        res = super(IrConfigParameter, self).create(vals)
        if vals and vals.get("key") == KEY:
            self._recompute_is_super_app()
        return res

    @api.multi
    def write(self, vals):
        res = super(IrConfigParameter, self).write(vals)
        if self.key == KEY:
            self._recompute_is_super_app()
        return res
