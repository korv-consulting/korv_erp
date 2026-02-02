{
    'name': 'Employees Management System',
    'author': 'KORV Consulting',
    'website': 'www.korv.consulting',
    'category': 'Human Resources Application',
    'summary': 'Employees Management System',
    'depends':  ['hr'],
    'data': [
        'views/employees_view.xml',
        'security/ir.model.access.csv',
        'security/rules.xml',
    ],
    'installable': True,
}