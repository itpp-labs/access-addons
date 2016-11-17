# -*- coding: utf-8 -*-
{
    'name': 'Apps',
    'summary': """ """,
    'images': [],
    'version': '1.0.0',
    'application': False,
    'author': 'IT-Projects LLC, Dinar Gabbasov',
    'website': 'https://twitter.com/gabbasov_dinar',
    'category': 'Access',
    'license': 'GPL-3',

    'depends': [
        'access_apps',
    ],
    'data': [
        'views/apps_view.xml',
        'security.xml',
    ],

    'post_load': None,
    'pre_init_hook': None,
    'post_init_hook': None,

    'auto_install': False,
    'installable': True
}
