from odoo import models, fields, api
from odoo.exceptions import ValidationError


class SlaContract(models.Model):
    _name = "sla.contract"
    _description = "SLA Contract"
    _rec_name = "name"

    _sql_constraints = [
        (
            'mission_unique_sla',
            'unique(mission_id)',
            'Une mission ne peut avoir qu\'un seul SLA.',
        ),
    ]


    # champs de base


    name = fields.Char(string="SLA Reference", required=True)
    mission_id = fields.Many2one(
        comodel_name="sale.order",
        string="Mission",
        required=True,
        ondelete="cascade"
    )
    partner_id = fields.Many2one(
        comodel_name="res.partner",
        string="Client",
        related="mission_id.partner_id",
        store=True,
        readonly=True,)

    service_type = fields.Selection([
        ('recruitment', 'Recrutement'),
        ('temp_staffing', 'Intérim'),
        ('payroll', 'Paie'),
    ], required=True, string="Type de service")

    geo_scope = fields.Selection([
        ('city', 'Ville'),
        ('regional', 'Régional'),
        ('national', 'National'),
        ('international', 'International'),
    ], string="Périmètre géographique")

    active = fields.Boolean(default=True)

    start_date = fields.Date(string="Date de début")
    end_date = fields.Date(string="Date de fin")
    state = fields.Selection([
        ('draft', 'Brouillon'),
        ('active', 'Actif'),
        ('expired', 'Expiré'),
    ], default='draft', string="Statut",)

   
    # RECRUITMENT
    # =========================

    take_charge_hours = fields.Float("Délai prise en charge (heures)")
    shortlist_days = fields.Integer("Délai short-list (jours)")
    min_cv_shortlist = fields.Integer("Nb CV minimum")
    first_interview_days = fields.Integer("Délai 1er entretien client(jours)")
    time_to_fill_days_target = fields.Integer("Objectif time-to-fill (jours)")
    checks_included = fields.Text("Vérifications incluses")
    guarantee_days = fields.Integer("Période de garantie (jours)")
    free_replacement = fields.Boolean("Remplacement gratuit")
    replacement_count_included = fields.Integer("Nb remplacements inclus")
    replacement_conditions = fields.Text("Conditions de remplacement")

    # =========================
    # TEMP STAFFING
    # =========================

    candidate_proposal_hours = fields.Float("Délai proposition candidat (heures)")
    deployment_hours = fields.Float("Délai mise à disposition (heures)")
    replacement_hours = fields.Float("Délai remplacement (heures)")

    coverage_hours = fields.Selection([
        ('8x5', '8x5'),
        ('12x5', '12x5'),
        ('24x7', '24x7'),
    ], string="Couverture horaire")

    on_call = fields.Boolean("Astreinte")
    min_assignment_days = fields.Integer("Durée minimale mission (jours)")
    timesheet_required = fields.Boolean("Timesheet obligatoire")
    temp_docs_included = fields.Text("Documents inclus")

    # =========================
    # PAYROLL
    # =========================

    payroll_cycle_day = fields.Integer("Jour cutoff")
    payroll_delivery_day = fields.Integer("Jour livraison bulletins")
    correction_sla_hours = fields.Float("SLA corrections (heures)")
    compliance_checks = fields.Text("Contrôles conformité")

    # =========================
    # VALIDATIONS
    # =========================

    @api.onchange('mission_id')
    def _onchange_mission_id(self):
        """Auto-remplit le client depuis la mission"""
        if self.mission_id:
            self.partner_id = self.mission_id.partner_id

    @api.constrains('service_type')
    def _check_service_type_change(self):
        for rec in self:
            if rec._origin and rec._origin.service_type and rec._origin.service_type != rec.service_type:
                raise ValidationError("Impossible de changer le type de service d'un SLA existant.")

    @api.constrains('replacement_count_included', 'free_replacement')
    def _check_replacement_logic(self):
        for rec in self:
            if rec.free_replacement and rec.replacement_count_included <= 0:
                raise ValidationError("Veuillez définir un nombre de remplacements inclus.")

   
    def cron_check_sla_expiration(self):
        """Passe en 'expired' les contrats dont la date de fin est dépassée"""
        today = fields.Date.today()
        # On cherche uniquement les contrats 'active' qui ont une date de fin ANTÉRIEURE à aujourd'hui
        expired_contracts = self.search([
            ('state', '=', 'active'),
            ('end_date', '<', today)
        ])
        if expired_contracts:
            expired_contracts.write({'state': 'expired'}) 

             
