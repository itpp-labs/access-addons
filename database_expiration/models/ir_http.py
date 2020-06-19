# Copyright 2020 Eugene Molotov <https://it-projects.info/team/em230418>
# License MIT (https://opensource.org/licenses/MIT).

from datetime import datetime

from odoo import models
from odoo.tools.misc import DEFAULT_SERVER_DATETIME_FORMAT


class IrHttp(models.AbstractModel):

    _inherit = "ir.http"

    def session_info(self):
        res = super(IrHttp, self).session_info()

        now = datetime.now()
        Config = self.env["ir.config_parameter"].sudo()
        database_expiration_date = Config.get_param("database_expiration_date", None)

        # Note:
        # DO NOT USE database.expiration_date (with dot)
        # it will be overwritten here: https://github.com/odoo/odoo/blob/f9a559f5455a4b964de9a99ff05756302071e959/addons/mail/models/update.py#L114

        if database_expiration_date:
            database_expiration_date = datetime.strptime(
                database_expiration_date, DEFAULT_SERVER_DATETIME_FORMAT
            )
            delta = database_expiration_date - now
            if now > database_expiration_date:
                res["database_block_message"] = "Your database is expired"
            elif delta.days > 7:
                pass
            elif delta.days > 1:
                res[
                    "database_block_message"
                ] = "Your database will expire in {} days".format(delta.days,)
                res["database_block_is_warning"] = True
            elif delta.days == 1:
                res[
                    "database_expiration_message"
                ] = "Your database will expire tomorrow"
                res["database_block_is_warning"] = True
            elif delta.days == 0:
                res["database_expiration_message"] = "Your database will expire today"
                res["database_block_is_warning"] = True


        return res
