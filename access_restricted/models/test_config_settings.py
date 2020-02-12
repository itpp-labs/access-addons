# -*- coding: utf-8 -*-

from odoo import fields, models


class TestConfigSettings(models.TransientModel):

    _name = "test.config.settings"
    _inherit = ["res.config.settings"]

    group_user = fields.Boolean(
        group="base.group_system", implied_group="base.group_user"
    )
