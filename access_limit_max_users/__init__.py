from odoo.api import Environment, SUPERUSER_ID


def post_init_hook(cr, registry):
    env = Environment(cr, SUPERUSER_ID, {})
    env.ref("access_limit_max_users.max_users_limit").max_records = env[
        "res.users"
    ].search_count([])
