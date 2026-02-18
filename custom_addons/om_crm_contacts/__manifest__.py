{
    'name': 'KORV CRM customization',
    'author': 'KORV Consulting',
    'website': 'www.korv.consulting',
    'category': 'CRM',
    'summary': 'Customer Management System',
    'description': 'This module extends the CRM lead model to include additional fields and custom views for better lead management.',
    "depends": ["base", "crm", "hr", "contacts"],
    'data': [
        'views/crm_custom_views.xml',
        'views/crm_custom_client_views.xml',
        'security/ir.model.access.csv',
        'security/rules.xml',
    ],
    'installable': True,
}