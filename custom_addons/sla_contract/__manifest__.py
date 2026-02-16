# -*- coding: utf-8 -*-

{
    'name': 'SLA Contracts',
    'author': 'KORV Consulting',
    'website': 'www.korv-consulting.fr',
    'category': 'Sales',
    'summary': 'Gestion simple des contrats SLA liés aux commandes',
    'version': '1.0',
    'depends': ['sale'],
    'data': [
        'data/sla_cron.xml',
        'security/ir.model.access.csv',
        'report/sla_contract_report.xml',
        'views/sla_contract_views.xml',
        'views/sale_order_views.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}

