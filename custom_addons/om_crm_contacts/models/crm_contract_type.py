from odoo import api, fields, models, _

class CRMContractType(models.Model):
    _name = "crm.contract_type"
    _description = "Contract Type Record Records"

    name = fields.Char(string='Nom', required=True, tracking=True)
    slug = fields.Char(string='Slug', tracking=True, unique=True, help="Champ technique pour les références internes, généré automatiquement à partir du nom.")
    active = fields.Boolean(default=True)