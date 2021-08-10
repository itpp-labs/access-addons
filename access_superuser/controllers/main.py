from odoo import http
from odoo.addons.web.controllers.main import Home
from odoo.http import request


class Home(Home):
    @http.route()
    def switch_to_admin(self):
        uid = request.env.user.id
        if request.env.user.is_sudoer:
            return super(Home, self).switch_to_admin()
        else:
            return http.local_redirect(self._login_redirect(uid), keep_hash=True)
