from odoo import api, fields, models, _

class CRMActivityArea(models.Model):
    _name = "crm.activity_area"
    _description = "Activity Area Record Records"

    name = fields.Char(string='Nom', required=True, tracking=True)