# -*- coding: utf-8 -*-
{
    "name": """Limit number of records""",
    "summary": """e.g. allow to create maximum 10 users. Similar restriction can be applied to any table.""",
    "category": "Extra tools",
    "images": [],
    "version": "1.0.0",

    "author": "IT-Projects LLC, Pavel Romanchenko",
    "support": "apps@it-projects.info",
    "website": "https://it-projects.info",
    "license": "LGPL-3",
    "price": 30.00,
    "currency": "EUR",

    "depends": [
        'base_action_rule',
    ],
    "external_dependencies": {"python": [], "bin": []},
    "data": [
        'security/records_number_security.xml',
        'security/ir.model.access.csv',
        'views/base_limit.xml',
        'data/data.xml',
    ],
    "qweb": [],
    "demo": [
        'demo/demo.xml',
    ],

    "post_load": None,
    "pre_init_hook": None,
    "post_init_hook": None,
    "installable": True,
    "auto_install": False,
}
