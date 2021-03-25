# Copyright 2020 Eugene Molotov <https://it-projects.info/team/em230418>
# License MIT (https://opensource.org/licenses/MIT).

{
    "name": """Block backend UI""",
    "summary": """This technical module allows blocking backend access and display the message""",
    "category": "Extra Tools",
    "images": [],
    "version": "14.0.1.0.0",
    "application": False,
    "author": "IT-Projects LLC, Eugene Molotov",
    "support": "help@itpp.dev",
    "website": "https://twitter.com/OdooFree",
    "license": "Other OSI approved licence",  # MIT
    "depends": ["web"],
    "external_dependencies": {"python": [], "bin": []},
    "data": ["views/assets.xml"],
    "demo": [],
    "qweb": ["static/src/xml/apps.xml"],
    "post_load": None,
    "pre_init_hook": None,
    "post_init_hook": None,
    "uninstall_hook": None,
    "auto_install": False,
    "installable": True,
}
