{
    "name": """Multi-website support in Security Rules""",
    "summary": """Provide access depending on current website""",
    "category": "Access",
    # "live_test_url": "",
    "images": [],
    "version": "11.0.1.3.1",
    "application": False,

    "author": "IT-Projects LLC, Ildar Nasyrov",
    "support": "apps@it-projects.info",
    "website": "https://it-projects.info/team/iledarn",
    "license": "LGPL-3",
    "price": 20.00,
    "currency": "EUR",

    "depends": [
        "web_website",
    ],
    "external_dependencies": {"python": [], "bin": []},
    "data": [
        "views/ir_rule_views.xml",
    ],
    "qweb": [
    ],
    "demo": [
    ],

    "post_load": None,
    "pre_init_hook": None,
    "post_init_hook": None,
    "uninstall_hook": None,

    "auto_install": False,
    "installable": True,
}
