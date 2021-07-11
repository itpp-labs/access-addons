# -*- coding: utf-8 -*-
{
    "name": "Custom Apps",
    "summary": """Simplify Apps Interface""",
    "images": [],
    "version": "10.0.1.0.0",
    "application": False,
    "author": "IT-Projects LLC, Dinar Gabbasov",
    "support": "apps@itpp.dev",
    "website": "https://twitter.com/gabbasov_dinar",
    "category": "Access",
    "license": "Other OSI approved licence",  # MIT
    "depends": ["access_apps"],
    "data": ["views/apps_view.xml", "security.xml", "data/ir_config_parameter.xml"],
    "post_load": None,
    "pre_init_hook": None,
    "post_init_hook": None,
    "auto_install": False,
    "installable": True,
}
