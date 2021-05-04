# Copyright 2020 Eugene Molotov <https://it-projects.info/team/em230418>
# License MIT (https://opensource.org/licenses/MIT).

import os

from odoo import models
from odoo.tools import human_size


# https://stackoverflow.com/a/1392549
def get_directory_size(start_path):
    total_size = 0
    for dirpath, _dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size


class IrHttp(models.AbstractModel):

    _inherit = "ir.http"

    def session_info(self):
        res = super(IrHttp, self).session_info()

        Config = self.env["ir.config_parameter"].sudo()
        try:
            database_limit_size = int(Config.get_param("database_limit_size", 0))
        except ValueError:
            return res

        if not database_limit_size:
            return res

        self.env.cr.execute("select pg_database_size(%s)", [self.env.cr.dbname])
        database_size = self.env.cr.fetchone()[0]

        filestore_size = get_directory_size(self.env["ir.attachment"]._filestore())

        total_size = database_size + filestore_size
        if total_size > database_limit_size:
            res["database_block_message"] = "Database size exceed ({} / {})".format(
                human_size(total_size),
                human_size(database_limit_size),
            )
        elif total_size > database_limit_size * 0.9:
            res[
                "database_block_message"
            ] = "Database size is about to be exceed (%s / %s)" % (
                human_size(total_size),
                human_size(database_limit_size),
            )
            res["database_block_is_warning"] = True

        return res
