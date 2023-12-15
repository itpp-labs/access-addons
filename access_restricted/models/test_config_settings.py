from odoo import fields, models


class TestConfigSettings(models.TransientModel):

    _description = "Test config settings"
    _inherit = ["res.config.settings"]

    group_test_access_restricted = fields.Boolean(
        group="base.group_system",
        # random group for test purposes
        implied_group="base.group_multi_currency",
    )
