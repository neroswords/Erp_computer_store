# -*- coding: utf-8 -*-
{
    'name': "garden",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'mail',
        'contacts',
    ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/garden_security.xml',
        'wizard/set_status_views.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/plot_views.xml',
        'views/partner_views.xml',
        'views/plot2_views.xml',
        'views/slot2_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
