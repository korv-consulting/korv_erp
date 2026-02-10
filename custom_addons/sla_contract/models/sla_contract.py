from odoo import fields, models


class SlaContract(models.Model):
    _name = 'sla.contract'
    _description = 'SLA Contract'
    _order = 'create_date desc, id desc'

    # Identification
    name = fields.Char(string='SLA Reference', required=True)
    sale_order_id = fields.Many2one(
        comodel_name='sale.order',
        string='Sales Order',
        ondelete='set null',
    )
    partner_id = fields.Many2one(
        comodel_name='res.partner',
        string='Customer',
        required=True,
        ondelete='restrict',
    )
    mission_name = fields.Char(string='Mission Name')

    # Period
    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')
    state = fields.Selection(
        selection=[
            ('draft', 'Draft'),
            ('active', 'Active'),
            ('expired', 'Expired'),
        ],
        string='Status',
        default='draft',
    )

    # SLA commitments
    response_time = fields.Float(string='Response Time (hours)')
    resolution_time = fields.Float(string='Resolution Time (hours)')
    support_hours = fields.Selection(
        selection=[
            ('8x5', '8x5'),
            ('24x7', '24x7'),
        ],
        string='Support Hours',
        default='8x5',
    )

    # Qualitative commitments
    scope = fields.Text(string='Scope')
    exclusions = fields.Text(string='Exclusions')

