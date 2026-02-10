# -*- coding: utf-8 -*-

{
    'name': 'SLA Contracts',
    'author': 'KORV Consulting',
    'website': 'www.korv.consulting',
    'category': 'Sales',
    'summary': 'Gestion simple des contrats SLA liés aux commandes',
    'version': '1.0',
    'depends': ['sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/sla_contract_views.xml',
        'views/sale_order_views.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}

