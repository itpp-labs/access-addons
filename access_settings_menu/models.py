from inspect import signature
from odoo import api, models


class ResUsers(models.Model):
    _inherit = "res.users"

    @api.model
    def fields_get(self, *args, **kwargs):
        # switch to superuser to get access to virtual fields
        # clean kwargs before call the function
        sig = signature(super(ResUsers, self.sudo()).fields_get)
        kwargs = {key: kwargs[key] for key in kwargs.keys() if sig.parameters.get(key)}
        return super(ResUsers, self.sudo()).fields_get(*args, **kwargs)
