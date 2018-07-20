# -*- coding: utf-8 -*-
from odoo import api, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    @api.model
    def _install_modules(self, modules):
        if self.env['res.users'].has_group('access_apps.group_allow_apps_only_from_settings'):
            self = self.sudo()

        return super(ResConfigSettings, self)._install_modules(modules)

    @api.model
    def default_get(self, fields):
        # We restricted any access to apps by default (`ir.module.module`) but in `website_sale` module configuration
        # there is a field that gets its default value by searching in apps.
        # Without this there is a possibility to encounter the `Access Error` when trying to open settings
        # - e.g. when administrators without access to apps open ``[[ Website Admin ]] >> Configuration >> Settings``

        # TODO: this solution may lead to unexpected result
        # if some of default methods uses self self.env.user to compute default value
        res = super(ResConfigSettings, self.sudo()).default_get(fields)
        return res
