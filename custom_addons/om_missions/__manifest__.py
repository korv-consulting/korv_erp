{
    'name': 'Missions Management System',
    'author': 'KORV Consulting',
    'website': 'www.korv.consulting',
    'category': 'Sales Application',
    'summary': 'Missions Management System',
    'application': True,
    'version': '1.0',
    'depends':  ['mail', 'hr' , 'sale', 'product' , 'stock', 'sale_stock'],
    'data': [
        'views/views.xml',
        'views/mission_inherit_product.xml',
        'security/ir.model.access.csv',
        'views/sale_order_inherit.xml',
    ],
    'installable': True,
    'license': 'LGPL-3',
}