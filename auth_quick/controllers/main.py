# Copyright 2018 Ivan Yelizariev <https://it-projects.info/team/yelizariev>
# License MIT (https://opensource.org/licenses/MIT).
import json
import logging
import urllib.parse

import requests
import werkzeug

from odoo import http
from odoo.http import request

_logger = logging.getLogger(__name__)


class AuthQuickMaster(http.Controller):
    def get_master_url(self):
        return request.env["ir.config_parameter"].sudo().get_param("auth_quick.master")

    def get_build_url(self):
        url = request.httprequest.url
        parsed = urllib.parse.urlparse(url)
        return parsed.scheme + "://" + parsed.netloc

    @http.route("/auth_quick/login", type="http", auth="public")
    def login(self, build_login=None, build_user_id=None):
        if not (build_login or build_user_id):
            return "Wrong args"

        if build_user_id:
            user = request.env["res.users"].sudo().browse(int(build_user_id))
            build_login = user.login
        else:
            user = request.env["res.users"].sudo().search([("login", "=", build_login)])
            build_user_id = user.id

        _logger.debug(
            "Authentication request for %s (id %s)", build_login, build_user_id
        )
        build_url = self.get_build_url()
        build = (
            request.env["ir.config_parameter"]
            .sudo()
            .get_param("auth_quick.build", "unknown")
        )
        master_url = self.get_master_url()
        params = urllib.parse.urlencode(
            {
                "build": build,
                "build_login": build_login,
                "build_user_id": build_user_id,
                "build_url": build_url,
            }
        )
        url = urllib.parse.urljoin(
            master_url, "/auth_quick_master/get-token?%s" % params
        )

        return werkzeug.utils.redirect(url, 302)

    @http.route("/auth_quick/check-token", type="http", auth="public")
    def check_token(self, token, test_cr=False):
        master_url = self.get_master_url()
        url = urllib.parse.urljoin(master_url, "/auth_quick_master/check-token")
        res = requests.post(
            url,
            data=json.dumps({"params": {"token": token}}),
            headers={"Content-Type": "application/json"},
        )
        _logger.debug("Response from master odoo: %s", res.text)
        result = res.json().get("result")
        if not result.get("success"):
            return "Wrong token"

        build_login = result["data"]["build_login"]
        user = request.env["res.users"].sudo().search([("login", "=", build_login)])
        user.write({"auth_quick_token": token})
        _logger.info("Successful Authentication as %s via token %s", build_login, token)

        if test_cr is False:
            # A new cursor is used to authenticate the user and it cannot see the
            # latest changes of current transaction.
            # Therefore we need to make the commit.

            # TODO: tests
            # In test mode, one special cursor is used for all transactions.
            # So we don't need to make the commit. More over commit() shall not be used,
            # because otherwise test changes are not rollbacked at the end of test
            request.env.cr.commit()

        request.session.authenticate(request.db, build_login, token)
        return werkzeug.utils.redirect("/")
