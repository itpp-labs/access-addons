# -*- coding: utf-8 -*-

from odoo import models
from odoo.http import request


class IrHttp(models.AbstractModel):
    _inherit = 'ir.http'

    def session_info(self):
        res = super(IrHttp, self).session_info()
        res.update({'has_access_to_apps': request.env.user.has_group('access_apps.group_allow_apps')})
        return res
