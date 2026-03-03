from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    # rccm = fields.Char(string="RCCM", help="This field stores the RCCM / SIREN number of the lead.")

    department_id = fields.Many2one('hr.department', string="Département assigné")

    employee_id = fields.Many2one('hr.employee', string="Employé assigné", domain="[('department_id', '=', department_id)]")

    interested_service = fields.Char(string="Produit / service d’intérêt", tracking=True)

    stage_name = fields.Char(related='stage_id.name', store=False)

    activity_area_id = fields.Many2one('crm.activity_area', string="Secteur d'activité")

    company_size_id = fields.Many2one('crm.company_size', string="Taille de l'entreprise")

    company_revenue = fields.Float(string="Chiffre d'affaire")
    
    company_creation_date = fields.Date(string="Date de création de l'entreprise")

    number_of_employees = fields.Selection([('1-10', '1 - 10'), ('11-50', '11 - 50'), ('51-200', '51 - 200'),  ('201-500', '201 - 500'), ('501-1000', '501 - 1 000'), ('1 001-5 000', '1 001 - 5 000'), ('5 001-10 000', '5 001 - 10 000'), ('more10k', '+ 10 000')], string="Nombre d’employés", tracking=True)

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
    desired_start_date = fields.Date(string="Date de démarrage souhaitée", tracking=True)
    decision_criteria = fields.Text(string="Critères de décision client", tracking=True)
    identified_risks = fields.Text(string="Risques identifiés", tracking=True)

    # Fields for Opportunity management
    opportunity_qualified = fields.Boolean(string="Opportunité qualifiée", tracking=True)
    estimated_deal_amount = fields.Float(string="Montant estimé de l’affaire", tracking=True)
    closing_probability = fields.Float(string="Probabilité de closing (%)", tracking=True)
    estimated_closing_date = fields.Date(string="Date de closing estimée", tracking=True)
    estimated_cost = fields.Float(string="Coût estimé", tracking=True)
    target_margin = fields.Float(string="Marge cible (%)", tracking=True)
    competition_present = fields.Boolean(string="Concurrence présente", tracking=True)
    internal_capacity_available = fields.Boolean(string="Capacité interne disponible", tracking=True)
    business_priority = fields.Selection([('low', 'Basse'), ('medium', 'Moyenne'), ('high', 'Haute')], string="Priorité business", tracking=True)


    #  Fields for Proposition management
    proposal_sent = fields.Boolean(string="Proposition envoyée", tracking=True)
    proposal_sent_date = fields.Date(string="Date d’envoi de l’offre", tracking=True)
    proposed_amount = fields.Float(string="Montant proposé", tracking=True)
    proposed_discount = fields.Float(string="Remise proposée (%)", tracking=True)
    offer_validity_date = fields.Date(string="Date de validité de l’offre", tracking=True)
    follow_up_date = fields.Date(string="Date de relance prévue", tracking=True)
    initial_client_feedback = fields.Text(string="Feedback initial client", tracking=True)

    # Fields for Negociation management
    negotiation_active = fields.Boolean(string="Négociation en cours", tracking=True)
    negotiated_points = fields.Selection([('price', 'Prix'), ('timeline', 'Délais'), ('scope', 'Scope'), ('payment', 'Paiement')], string="Points négociés", tracking=True)
    requested_discount = fields.Float(string="Remise demandée (%)", tracking=True)
    granted_discount = fields.Float(string="Remise accordée (%)", tracking=True)
    main_loss_risk = fields.Text(string="Risque principal de perte", tracking=True)
    updated_closing_probability = fields.Float(string="Probabilité mise à jour (%)", tracking=True)
    final_decision_expected_date = fields.Date(string="Date décision finale attendue", tracking=True)
    last_client_feedback = fields.Text(string="Dernier feedback client", tracking=True)
    internal_go_no_go = fields.Selection([('go', 'Go'), ('no_go', 'No Go')], string="Go / No Go interne", tracking=True)

    # Fields for Client management
    is_client_active = fields.Boolean(string="Client actif", tracking=True)
    contract_type_id = fields.Many2one('crm.contract_type', string="Type de contrat")
    contract_start_date = fields.Date(string="Date de démarrage")
    contract_duration_months = fields.Integer(string="Durée du contrat")
    contract_duration_unit = fields.Selection([('day', 'Jour(s)'), ('month', 'Mois'), ('year', 'An(s)')], default='month')
    signed_contract = fields.Boolean(string="Contrat signé?", tracking=True)
    signed_contract_date = fields.Date(string="Date de signature du contrat")
    contract_amount = fields.Float(string="Montant du contrat", tracking=True)

    # Fields for Loyalty management
    recurring_client = fields.Boolean(string="Client récurrent", tracking=True)
    satisfaction_rate = fields.Float(string="Taux de satisfaction", tracking=True)
    nps = fields.Float(string="NPS", tracking=True)
    renewal_planned = fields.Boolean(string="Renouvellement prévu", tracking=True)
    renewal_date = fields.Date(string="Date de renouvellement", tracking=True)
    customer_lifetime_value = fields.Float(string="Valeur vie client (CLV)", tracking=True)
    upsell_done = fields.Boolean(string="Upsell réalisé", tracking=True)
    cross_sell_done = fields.Boolean(string="Cross-sell réalisé", tracking=True)

    # Remplit automatiquement le champ 'Nom du contact / Société' (partner_name) avec la valeur du champ 'name' du Lead lors de la modification du nom du Lead
    @api.onchange('name')
    def _onchange_name_fill_partner(self):
        for record in self:
            if record.name:

                # Remplit le champ 'Nom du contact / Société' (partner_name)
                record.partner_name = record.name

    def write(self, vals):
        # 1. On exécute l'écriture standard sur le Lead
        result = super(CrmLead, self).write(vals)

        # 2. Définition du mapping des noms qui diffèrent entre les deux modèles
        # (Le CRM utilise souvent 'email_from' là où le partenaire utilise 'email')
        field_mapping = {
            'email_from': 'email',
            'contact_name': 'name',
            # Ajoutez ici d'autres exceptions si nécessaire
        }

        # 3. Identifier les champs modifiés qui existent aussi chez le partenaire
        partner_model = self.env['res.partner']
        sync_vals = {}
        
        for field_name, value in vals.items():
            # Déterminer le nom du champ cible sur res.partner
            target_field = field_mapping.get(field_name, field_name)
            
            # Si le champ existe sur res.partner, on le prépare pour la synchro
            if target_field in partner_model._fields:
                sync_vals[target_field] = value

        # 4. Appliquer la mise à jour aux partenaires liés
        if sync_vals:
            for lead in self:
                if lead.partner_id:
                    # On utilise write() sur le partenaire avec les valeurs filtrées
                    lead.partner_id.write(sync_vals)
        
        return result