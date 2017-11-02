# -*- coding: utf-8 -*-
{
    'name': 'Custom Apps',
    'summary': """Simplify Apps Interface""",
    'images': [],
    'version': '1.0.0',
    'application': False,
    'author': 'IT-Projects LLC, Dinar Gabbasov',
    "support": "apps@it-projects.info",
    'website': 'https://twitter.com/gabbasov_dinar',
    'category': 'Access',
    'license': 'LGPL-3',

    'depends': [
        'access_apps',
    ],
    'data': [
        'views/apps_view.xml',
        'security.xml',
        'data/ir_config_parameter.xml',
    ],

    'post_load': None,
    'pre_init_hook': None,
    'post_init_hook': None,

    'auto_install': False,
    'installable': False
}
