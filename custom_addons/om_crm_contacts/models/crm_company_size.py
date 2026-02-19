from odoo import fields, models, _

class CRMCompanySize(models.Model):
    _name = "crm.company_size"
    _description = "Company Size Record Records"

    name = fields.Char(string='Nom', required=True, tracking=True)