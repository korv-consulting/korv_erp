from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    rccm = fields.Char(string="RCCM", help="This field stores the RCCM / SIREN number of the company.")
    nui = fields.Char(string="NUI", help="This field stores the NUI number of the company.")

    department_id = fields.Many2one('hr.department', string="Département assigné")
    
    employee_id = fields.Many2one('hr.employee', string="Employé assigné", domain="[('department_id', '=', department_id)]")
