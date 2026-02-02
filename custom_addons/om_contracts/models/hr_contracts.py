# -*- coding: utf-8 -*-
from odoo import api, fields, models, _, tools


class HRContracts(models.Model):
    _inherit = 'hr.contract'

    trial_months = fields.Integer("Nombre de mois d'essai", tracking=True)
    bank_details = fields.Char('RIB', tracking=True)
    wage = fields.Monetary('Salaire Net', required=True, tracking=True)
    tax = fields.Monetary('Impôts', required=True, tracking=True)
    cnps_contribution = fields.Monetary('Cotisation CNPS', required=True, tracking=True)
    gross_wage = fields.Monetary('Salaire Brut', tracking=True, readonly=True, compute='compute_gross_wage', store=True)

    @api.depends('wage', 'tax', 'cnps_contribution')
    def compute_gross_wage(self):
        for record in self:
            record.gross_wage = record.wage + record.cnps_contribution + record.tax
