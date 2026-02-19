from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    rccm = fields.Char(string="RCCM", help="This field stores the RCCM / SIREN number of the company.")
    nui = fields.Char(string="NUI", help="This field stores the NUI number of the company.")

    department_id = fields.Many2one('hr.department', string="Département assigné")
    
    employee_id = fields.Many2one('hr.employee', string="Employé assigné", domain="[('department_id', '=', department_id)]")

    activity_area_id = fields.Many2one('crm.activity_area', string="Secteur d'activité")

    company_size_id = fields.Many2one('crm.company_size', string="Taille de l'entreprise")


    type = fields.Selection([
        ('contact', 'Contact'),
        ('invoice', 'Facturation'),
        ('delivery', 'Presation'),
        ('other', 'Autre')
    ], string='Adresse Type', default='contact')
