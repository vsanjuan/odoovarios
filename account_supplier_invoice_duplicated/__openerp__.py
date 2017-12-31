# -*- coding: utf-8 -*-
{
    'name': "Check duplicated supplier invoices",

    'summary': """
        Check if a supplier invoice was created before to avoid duplicates""",

    'description': """
    When a supplier invoice is created, this module check using the reference field if was created before.
    If yes, show a message to the user to avoid to have duplicated supplier invoices in the sistem
    """,

    'author': "DMPyme",
    'website': "http://www.dmpyme.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Accounting',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base','account'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}