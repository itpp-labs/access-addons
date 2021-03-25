# Copyright 2020 Eugene Molotov <https://it-projects.info/team/em230418>
# Copyright 2021 Denis Mudarisov <https://github.com/trojikman>
# License MIT (https://opensource.org/licenses/MIT).

import logging
from datetime import datetime

from mako.template import Template

from odoo import models
from odoo.tools.misc import DEFAULT_SERVER_DATETIME_FORMAT

_logger = logging.getLogger(__name__)
DATABASE_BLOCK_MESSAGE_HTML_TEMPLATE = Template(
    "<p>${database_block_message}</p><a href='${database_expiration_link}'>${database_expiration_link_label}</a>"
)


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

            try:
                database_expiration_warning_delay = int(
                    Config.get_param("database_expiration_warning_delay", 7)
                )
                if not database_expiration_warning_delay > 1:
                    raise ValueError("Value must be greater than 1")
            except ValueError as e:
                _logger.warning(
                    "Could not get expiration warning delay: %s. Using default: 7 days"
                    % str(e)
                )
                database_expiration_warning_delay = 7

            if now > database_expiration_date:
                res["database_block_message"] = "Your database is expired"
            elif delta.days > database_expiration_warning_delay:
                pass
            elif delta.days > 1:
                res[
                    "database_block_message"
                ] = "Your database will expire in {} days".format(
                    delta.days,
                )
                res["database_block_is_warning"] = True
            elif delta.days == 1:
                res["database_block_message"] = "Your database will expire tomorrow"
                res["database_block_is_warning"] = True
            elif delta.days == 0:
                res["database_block_message"] = "Your database will expire today"
                res["database_block_is_warning"] = True

            if res.get("database_block_message"):
                database_expiration_link = Config.get_param(
                    "database_expiration_details_link", None
                )

                if database_expiration_link:
                    database_expiration_link_label = Config.get_param(
                        "database_expiration_details_link_label", "Details"
                    )
                    res[
                        "database_block_message"
                    ] = DATABASE_BLOCK_MESSAGE_HTML_TEMPLATE.render(
                        database_block_message=res["database_block_message"],
                        database_expiration_link=database_expiration_link,
                        database_expiration_link_label=database_expiration_link_label,
                    )

        return res
