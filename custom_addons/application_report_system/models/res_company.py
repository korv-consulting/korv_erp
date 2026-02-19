from odoo import models, fields

class ResCompany(models.Model):
    _inherit = 'res.company'

    logo_secondary = fields.Binary("Logo secondaire KORV WORK")
