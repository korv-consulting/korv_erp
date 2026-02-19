from odoo import api, fields, models, _

class CRMActivityArea(models.Model):
    _name = "crm.activity_area"
    _description = "Activity Area Record Records"

    name = fields.Char(string='Nom', required=True, tracking=True)
    slug = fields.Char(string='Slug', tracking=True, unique=True, help="Champ technique pour les références internes, généré automatiquement à partir du nom.")
    active = fields.Boolean(default=True)