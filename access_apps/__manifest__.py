# Copyright 2018,2021 Ivan Yelizariev <https://it-projects.info/team/yelizariev>
# Copyright 2018 Ildar Nasyrov <https://it-projects.info/team/iledarn>
# License MIT (https://opensource.org/licenses/MIT).
{
    "name": """Control access to Apps""",
    "summary": """You can configure administrators which don't have access to Apps""",
    "category": "Extra Tools",
    # "live_test_url": "",
    "images": ["images/banner.png"],
    "version": "15.0.2.0.0",
    "application": False,
    "author": "IT-Projects LLC, Ivan Yelizariev",
    "support": "apps@itpp.dev",
    "website": "https://twitter.com/OdooFree",
    "license": "Other OSI approved licence",  # MIT
    # "price": 10.00,
    "currency": "EUR",
    "depends": ["access_restricted"],
    "external_dependencies": {"python": [], "bin": []},
    "data": ["security/access_apps_security.xml", "security/ir.model.access.csv"],
    "demo": [],
    "qweb": [],
    "post_load": None,
    "pre_init_hook": None,
    "post_init_hook": None,
    "uninstall_hook": "uninstall_hook",
    "auto_install": False,
    "installable": True,
}
