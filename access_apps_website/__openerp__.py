# -*- coding: utf-8 -*-
{
     "name": """Control access to Apps in Websit""",
     "summary": """Restrict access to the 'Install Apps' item in the 'Customize' menu""",
     "category": "Tools",
     "images": ["images/install_apps.png"],
     "version": "1.0.0",

     "author": "IT-Projects LLC, Developer Name",
     "website": "https://it-projects.info",
     "license": "GPL-3",
     "price": 20.00,
     "currency": "EUR",

     "depends": [
         "access_apps",
         "website",
     ],
     "external_dependencies": {"python": [], "bin": []},
     "data": [
         "views/access_apps.xml",
     ],
     "demo": [
     ],
     "installable": True,
     "auto_install": True,
}