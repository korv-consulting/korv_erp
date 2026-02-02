# -*- coding: utf-8 -*-
from odoo import api, fields, models, _, tools

AVAILABLE_PRIORITIES = [
    ('0', 'Normal'),
    ('1', 'Satisfactory'),
    ('2', 'Good'),
    ('3', 'Very Good'),
    ('4', 'Excellent'),
    ('5', 'Perfect')
]

class HRApplicant(models.Model):
    _inherit = 'hr.applicant'

    priority = fields.Selection(AVAILABLE_PRIORITIES, "Evaluation", default='0')