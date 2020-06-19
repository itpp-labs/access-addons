# Copyright 2020 Eugene Molotov <https://it-projects.info/team/em230418>
# License MIT (https://opensource.org/licenses/MIT).

from odoo import SUPERUSER_ID, models


class IrHttp(models.AbstractModel):

    _inherit = "ir.http"

    def session_info(self):
        res = super(IrHttp, self).session_info()

        res["database_block_show_message_in_apps_menu"] = bool(
            self.env["ir.module.module"]
            .with_user(SUPERUSER_ID)
            .search(
                [("name", "=", "web_responsive"), ("state", "=", "installed")], limit=1,
            )
        )

        return res
