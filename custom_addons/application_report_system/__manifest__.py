{
    'name': 'Application Report System',
    'version': '1.0',
    'summary': 'Interview evaluation report for applicants',
    'author': 'KORV Consulting',
    'website': 'https://www.korv.consulting',
    'license': 'LGPL-3',
    'category': 'Human Resources',
    'depends': [
        'hr_recruitment'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/hr_applicant_views.xml',
        'views/report_applicant.xml',
    ],
    'installable': True,
    'application': False,
}
