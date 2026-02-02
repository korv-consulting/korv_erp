# -*- coding: utf-8 -*-
from odoo import api, fields, models, _, tools
from odoo.exceptions import ValidationError

class HRFamilyLink(models.Model):
    _name = "hr.family_link"
    _description = "Family Link Record Records"

    name = fields.Char(string='Name', required=True, tracking=True)