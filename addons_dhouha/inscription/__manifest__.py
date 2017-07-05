# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Inscription',
    'version': '2.0',
    'category': 'module interne',
    'description': """

==================================================

Formation technque odoo
    """,
    'summary': 'Formation odoo',
    'website': 'https://www.targa-consult.com',
    'depends': ['sale'],
    'data': [
        'views/inscription_view.xml',
        'views/faculte_view.xml',
        'views/moy_view.xml',
        'views/matiere_view.xml',
        'views/resultat_view.xml',
        'views/sale_view.xml',
        'views/line_view.xml',
        'report/report_sale_order_view.xml'
       
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': True,
    'sequence': 105,
}
