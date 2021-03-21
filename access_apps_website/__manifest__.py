{
    "name": """Restrict access to "Install Apps" in Website""",
    "summary": """Only users with "Show Apps Menu" access see "Install Apps" menu.""",
    "category": "Access",
    "images": ["images/install_apps.png"],
    "vesion": "11.0.1.0.0",
    "author": "IT-Projects LLC",
    "support": "apps@itpp.dev",
    "website": "https://itpp.dev",
    "license": "Other OSI approved licence",  # MIT
    "price": 20.00,
    "currency": "EUR",
    "depends": ["access_apps", "website"],
    "external_dependencies": {"python": [], "bin": []},
    "data": ["views/access_apps.xml"],
    "demo": [],
    "installable": False,
    "auto_install": True,
}
