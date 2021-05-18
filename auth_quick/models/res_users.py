# Copyright 2018 Ivan Yelizariev <https://it-projects.info/team/yelizariev>
# License MIT (https://opensource.org/licenses/MIT).
import logging

from odoo import fields, models
from odoo.exceptions import AccessDenied

_logger = logging.getLogger(__name__)


class ResUsers(models.Model):
    _inherit = "res.users"

    auth_quick_token = fields.Char()

    def _check_credentials(self, password, user_agent_env):
        try:
            return super(ResUsers, self)._check_credentials(password, user_agent_env)
        except AccessDenied:
            res = self.sudo().search(
                [("id", "=", self.env.uid), ("auth_quick_token", "=", password)]
            )
            if not res:
                raise
