# -*- coding: utf-8 -*-
from openerp import models, api


class ResUsers(models.Model):
    _inherit = 'res.users'

    @api.model
    def fields_get(self, **kwargs):
        # switch to superuser to get access to virtual fields
        return super(ResUsers, self.sudo()).fields_get(**kwargs)
