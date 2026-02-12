from odoo import fields, models


class SlaContract(models.Model):
    _name = 'sla.contract'
    _description = 'SLA Contract'
    _order = 'create_date desc, id desc'

    # Identification
    name = fields.Char(string='Référence SLA', required=True)
    sale_order_id = fields.Many2one(
        comodel_name='sale.order',
        string='Commande',
        ondelete='set null',
    )
    partner_id = fields.Many2one(
        comodel_name='res.partner',
        string='Client',
        required=True,
        ondelete='restrict',
    )
    mission_name = fields.Char(string='Nom de la mission')

    # Period
    start_date = fields.Date(string='Date de début')
    end_date = fields.Date(string='Date de fin')
    state = fields.Selection(
        selection=[
            ('draft', 'Brouillon'),
            ('active', 'Actif'),
            ('expired', 'Expiré'),
        ],
        string='Statut',
        default='draft',
    )

    # Engagements SLA
    response_time = fields.Float(string='Temps de réponse(heures)')
    resolution_time = fields.Float(string='Temps de résolution(heures)')
    support_hours = fields.Selection(
        selection=[
            ('8x5', '8x5 (du lundi au vendredi, de 8h à 17h)'),
            ('24x7', '24x7 (7j/7, 24h/24)'),
        ],
        string='Heures de support',
        default='24x7',
    )

    # Couverture SLA
    scope = fields.Text(string='Services couverts')
    exclusions = fields.Text(string='Exclusions')

    def cron_check_sla_expiration(self):
        """Passe en 'expired' les contrats dont la date de fin est dépassée"""
        today = fields.Date.today()
        # On cherche uniquement les contrats 'active' qui ont une date de fin < aujourd'hui
        expired_contracts = self.search([
            ('state', '=', 'active'),
            ('end_date', '<', today)
        ])
        if expired_contracts:
            expired_contracts.write({'state': 'expired'}) 

