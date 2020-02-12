# -*- coding: utf-8 -*-
from odoo import api, fields, models


class Module(models.Model):
    _inherit = "ir.module.module"

    is_super_app = fields.Char("Super App", compute="_compute_is_super_app", store=True)

    @api.model
    def get_super_app_prefix(self):
        return self.env["ir.config_parameter"].get_param(
            "apps.super_app_prefix", "super_app_"
        )

    @api.depends("name")
    def _compute_is_super_app(self):
        prefix = self.get_super_app_prefix()
        for r in self:
            r.is_super_app = r.name.startswith(prefix)

    @api.multi
    def button_uninstall(self):
        if self.is_super_app:
            # uninstall explicit dependencies
            to_uninstall = self.dependencies_id.mapped("depend_id")

            # excluded dependencies of other installed super modules
            for super_app in self.search(
                [
                    ("state", "=", "installed"),
                    ("name", "!=", self.name),
                    ("is_super_app", "=", True),
                ]
            ):
                to_uninstall -= super_app.upstream_dependencies(
                    exclude_states=("dummy_state",)
                )

            # mark modules for uninstallation
            for module in to_uninstall:
                module.button_uninstall()

        return super(Module, self).button_uninstall()
