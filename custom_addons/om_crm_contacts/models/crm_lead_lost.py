from odoo import models, fields

class CrmLeadLost(models.TransientModel):
    _inherit = 'crm.lead.lost'

    opportunity_lost = fields.Boolean(string="Opportunité perdue", tracking=True)

    loss_date = fields.Date(string="Date de perte", tracking=True)

    winning_competitor = fields.Char(string="Concurrent gagnant", tracking=True)

    price_gap = fields.Float(string="Écart prix", tracking=True)

    lessons_learned = fields.Text(string="Leçon apprise", tracking=True)

    future_recontact_possible = fields.Boolean(string="Recontact futur possible", tracking=True)

    potential_recontact_date = fields.Date(string="Date de recontact potentiel", tracking=True)