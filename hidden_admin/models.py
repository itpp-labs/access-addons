# -*- coding: utf-8 -*-
from openerp import api, models, SUPERUSER_ID


class Channel(models.Model):
    _inherit = 'mail.channel'

    @api.model
    def channel_fetch_listeners(self, uuid):
        res = super(Channel, self).channel_fetch_listeners(uuid)
        return [p for p in res if p.get('id') != SUPERUSER_ID]
