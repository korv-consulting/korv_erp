from odoo import fields, models, _

class CRMCompanySize(models.Model):
    _name = "crm.company_size"
    _description = "Company Size Record Records"

    name = fields.Char(string='Nom', required=True, tracking=True)
    slug = fields.Char(string='Slug', tracking=True, unique=True, help="Champ technique pour les références internes, généré automatiquement à partir du nom.")
    active = fields.Boolean(default=True)