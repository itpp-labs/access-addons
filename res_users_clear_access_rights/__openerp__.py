{
    'name' : 'Clear access rights button',
    "summary": """Useful tool to reset user rights""",
    'version' : '1.0.0',
    'author' : 'IT-Projects LLC, Ivan Yelizariev',
    'license': 'LGPL-3',
    'category' : 'Tools',
    'website' : 'https://it-projects.info',
    'depends' : ['base'],
    "external_dependencies": {"python": [], "bin": []},
    'data':[
        'views.xml',
        ],
    "demo": [
    ],
    'installable': True,
    'auto_install': False,
    'pre_init_hook': 'pre_init_hook',
}
