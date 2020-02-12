# -*- coding: utf-8 -*-
from odoo import api, models


class ResUsers(models.Model):
    _inherit = "res.users"

    @api.multi
    def action_clear_access_rights(self):
        self.ensure_one()
        admin_groups = [
            self.env.ref("base.group_user").id,
            self.env.ref("base.group_erp_manager").id,
            self.env.ref("base.group_system").id,
        ]

        groups_id = []
        for g in self.groups_id:
            if self.env.uid == self.id and g.id in admin_groups:
                # don't allow for Administrator to clear his admin rights
                continue
            groups_id.append((3, g.id))
        self.write({"groups_id": groups_id})
        return True
