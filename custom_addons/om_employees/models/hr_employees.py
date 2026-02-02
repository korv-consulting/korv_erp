# -*- coding: utf-8 -*-
from odoo import api, fields, models, _, tools


class HREmployees(models.Model):
    _inherit = 'hr.employee'

    matricule = fields.Integer(string="Matricule", default="1000", tracking=True)
    work_phone = fields.Char('Work Phone', compute="_compute_phones", store=True, readonly=False)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], string='Sexe')
    family_link_id = fields.Many2one('hr.family_link', string="Lien de parenté")
    emergency_contact = fields.Char("Nom", tracking=True)
    emergency_phone = fields.Char("Téléphone", tracking=True)
    emergency_contact2 = fields.Char("Nom", tracking=True)
    emergency_phone2 = fields.Char("Téléphone", tracking=True)
    family_link_id2 = fields.Many2one('hr.family_link', string="Lien de parenté")
    pdf_documents = fields.Many2many('ir.attachment', string='Documents PDF', domain="[('mimetype', '=', 'application/pdf')]")

    def _compute_phones(self):
        for employee in self:
            employee.work_phone = False
