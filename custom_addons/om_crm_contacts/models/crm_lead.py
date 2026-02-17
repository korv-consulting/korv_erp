from odoo import models, fields

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    # rccm = fields.Char(string="RCCM", help="This field stores the RCCM / SIREN number of the lead.")

    department_id = fields.Many2one('hr.department', string="Département assigné")

    employee_id = fields.Many2one('hr.employee', string="Employé assigné", domain="[('department_id', '=', department_id)]")

    interested_service = fields.Char(string="Produit / service d’intérêt", tracking=True)

    stage_name = fields.Char(related='stage_id.name', store=False)

    activity_area_id = fields.Many2one('crm.activity_area', string="Secteur d'activité")

    company_size_id = fields.Many2one('crm.company_size', string="Taille de l'entreprise")

    # Fields for Lead qualification
    perceived_interest_level = fields.Selection([('low', 'Faible'), ('medium', 'Moyen'), ('high', 'Fort')], string='Niveau d\'intérêt perçu', tracking=True)
    perceived_urgency_level = fields.Selection([('low', 'Faible'), ('medium', 'Moyen'), ('high', 'Fort')], string='Niveau d\'urgence perçu', tracking=True)
    lead_status = fields.Selection([('new', 'Nouveau'), ('to_qualify', 'A Qualifier'), ('rejected', 'Rejeté')], string='Statut du Lead', tracking=True)
    has_consent_contact = fields.Boolean(string="Consentement pour contact", tracking=True)


    # Fields for Prospect management
    estimated_budget = fields.Float(string="Budget estimé", tracking=True)
    budget_available = fields.Selection([('yes', 'Oui'), ('no', 'Non'), ('unknown', 'Inconnu')], string="Budget disponible", tracking=True)
    decision_target_date = fields.Date(string="Date cible de décision", tracking=True)
    authority_level = fields.Selection([('decision_maker', 'Décideur'), ('influencer', 'Influenceur'), ('user', 'Utilisateur')], string="Niveau d'autorité", tracking=True)
    next_action = fields.Char(string="Prochaine action", tracking=True)
    next_action_date = fields.Date(string="Date de la prochaine action", tracking=True)

    # Fields for Confirmed Needs management
    needs_validated = fields.Boolean(string="Besoin validé", tracking=True)
    functional_requirement_description = fields.Text(string="Description fonctionnelle du besoin", tracking=True)
    expected_business_value = fields.Text(string="Valeur métier attendue", tracking=True)
    confirmed_budget = fields.Boolean(string="Budget confirmé", tracking=True)
    budget_range_min = fields.Float(string="Fourchette budgétaire minimum", tracking=True)
    budget_range_max = fields.Float(string="Fourchette budgétaire maximum", tracking=True)
    # decision_maker_identified = fields.Boolean(string="Décideur identifié", tracking=True)
    # decision_maker_name = fields.Char(string="Nom du décideur", tracking=True)
    desired_start_date = fields.Date(string="Date de démarrage souhaitée", tracking=True)
    decision_criteria = fields.Text(string="Critères de décision client", tracking=True)
    identified_risks = fields.Text(string="Risques identifiés", tracking=True)

    # Fields for Client management
    is_client_active = fields.Boolean(string="Client actif", tracking=True)
    contract_type_id = fields.Many2one('crm.contract_type', string="Type de contrat")
    contract_start_date = fields.Date(string="Date de démarrage")
    contract_duration_months = fields.Integer(string="Durée du contrat")
    contract_duration_unit = fields.Selection([('day', 'Jour(s)'), ('month', 'Mois'), ('year', 'An(s)')], default='month')
    signed_contract = fields.Boolean(string="Contrat signé?", tracking=True)
    signed_contract_date = fields.Date(string="Date de signature du contrat")
    contract_amount = fields.Float(string="Montant du contrat", tracking=True)

    