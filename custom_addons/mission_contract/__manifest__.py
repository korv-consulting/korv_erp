# -*- coding: utf-8 -*-

{
    'name': 'Mission Contracts',
    'author': 'KORV Consulting',
    'website': 'www.korv-consulting.fr',
    'category': 'Sales',
    'summary': 'Gestion contrats Mission liés aux commandes',
    'version': '1.0',
    'depends': ['sale'],
    'data': [
        'security/ir.model.access.csv',
        'report/mission_contract_report.xml',
        'views/mission_contract_views.xml',
        'views/sale_order_views.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}

