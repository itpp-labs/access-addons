# -*- coding: utf-8 -*-
from odoo import SUPERUSER_ID, api, models


class Channel(models.Model):
    _inherit = "mail.channel"

    @api.model
    def channel_fetch_listeners(self, uuid):
        admin_id = self.env["res.users"].sudo().browse(SUPERUSER_ID).partner_id.id
        res = super(Channel, self).channel_fetch_listeners(uuid)
        return [p for p in res if p.get("id") != admin_id]
