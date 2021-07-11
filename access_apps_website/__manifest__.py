# -*- coding: utf-8 -*-
{
    "name": """Restrict access to "Install Apps" in Website""",
    "summary": """Only users with "Show Apps Menu" access see "Install Apps" menu.""",
    "category": "Access",
    "images": ["images/install_apps.png"],
    "version": "10.0.1.0.0",
    "author": "IT-Projects LLC",
    "support": "apps@itpp.dev",
    "website": "https://twitter.com/OdooFree",
    "license": "Other OSI approved licence",  # MIT
    "depends": ["access_apps", "website"],
    "external_dependencies": {"python": [], "bin": []},
    "data": ["views/access_apps.xml"],
    "demo": [],
    "installable": True,
    "auto_install": True,
}
