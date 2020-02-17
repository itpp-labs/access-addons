{
    "name": """Restrict access to buttons that install the modules in Website""",
    "summary": """Only users with "Allow install apps" access see/use buttons that install the modules.""",
    "category": "Access",
    "images": ["images/install_apps.png"],
    "version": "12.0.1.0.0",
    "author": "IT-Projects LLC",
    "support": "apps@itpp.dev",
    "website": "https://apps.odoo.com/apps/modules/12.0/access_apps_website/",
    "license": "Other OSI approved licence",  # MIT
    "price": 20.00,
    "currency": "EUR",
    "depends": ["access_apps", "website"],
    "external_dependencies": {"python": [], "bin": []},
    "data": ["views/access_apps.xml", "views/assets.xml"],
    "demo": [],
    "installable": True,
    "auto_install": True,
}
