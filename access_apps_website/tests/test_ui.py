# Copyright 2018 Rafis bikbov <https://it-projects.info/team/RafiZz>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).
from odoo.tests import common, tagged


@tagged('at_install', 'post_install')
class TestUI(common.HttpCase):

    def test_ui(self):
        phantom_env = self.env
        demo_user = phantom_env.ref('base.user_demo')
        system_group = phantom_env.ref('base.group_system')
        allow_apps_group = phantom_env.ref('access_apps.group_allow_apps')
        demo_user.write({'groups_id': [(4, system_group.id)]})
        demo_user.write({'groups_id': [(3, allow_apps_group.id)]})

        phantom_env.ref('base.module_website_blog').state = 'uninstalled'

        tour = 'access_apps_website.tour'
        self.phantom_js(
            '/web',
            "odoo.__DEBUG__.services['web_tour.tour']"
            ".run('%s')" % tour,

            "odoo.__DEBUG__.services['web_tour.tour']"
            ".tours['%s'].ready" % tour,

            login='demo',
        )
