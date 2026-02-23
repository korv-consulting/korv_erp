from odoo import api, models, fields


class MissionTemplate(models.Model):
    _inherit = "product.template"
    _description = 'Mission'  # C'est cette ligne qui change le log

    description_mission = fields.Html(string="Description de la mission")
    start_date = fields.Date(string="Date de debut")
    end_date = fields.Date(string="Date de fin")
    reference = fields.Char(string="Référence de la mission")
    categorie = fields.Selection(
        [
            ("recruitment", "Recrutement"),
            ("software", "Developpement logiciel"),
            ("outsourcing", "OutSourcing"),
        ],
        string="Catégorie de la mission",
    )

    internal_note = fields.Text("Notes internes")

    work_location = fields.Text(string="Lieu de travail")

    # Add a state field to track the mission's progress. This is separate from the sale order's state and can have its own workflow.
    state = fields.Selection(
        [
            ("draft", "Brouillon"),
            ("confirmed", "Confirmée"),
            ("in_progress", "En cours"),
            ("done", "Terminée"),
            ("cancel", "Annulée"),
        ],
        default="draft",
        tracking=True,
        string="Statut",
        group_expand='_read_group_state_ids'
    )

    # client is a required field on the mission, but since we're using delegation inheritance, we can link it to the partner_id field of sale.order.
    partner_id = fields.Many2one("res.partner", string="Client", required=True)

    # Use the HR contract type model which exists in the codebase
    contract_type_id = fields.Many2one(
        "hr.contract.type",
        string="Type de contrat",
    )

    # Others
    work_time = fields.Datetime(string="Heure de travail à valider")
    work_conditions = fields.Text(string="Conditions de travail")
    affiliated_site = fields.Text(string="Site de rattachement")

    # We want to keep the existing product types (consu, service, storable) but add a new one for missions. We also set 'service' as the default type for ease of use, but you can choose another default if it makes more sense in your context.
    detailed_type = fields.Selection(
        selection_add=[],  # on garde les options existantes
        default="service",  # valeur par défaut
    )

    # politique de facturation
    invoice_policy = fields.Selection(
        selection=[
            ("order", "A la commande"),  # option existante
            ("delivery", "Quantité livrée"),  # option existante
            # ("prepaid", "A la commande"),
            ("postpaid", "A la fin de la mission"),
            # ("quantity", "Par quantité livrée"),
        ],
        string="Politique de facturation",
        default="order",  # valeur par défaut
    )

    @api.model
    def _read_group_state_ids(self, states, domain, order):
        """ 
        Cette fonction renvoie toutes les clés de la sélection 
        pour forcer l'affichage de toutes les colonnes en Kanban.
        """
        return [key for key, val in type(self).state.selection]

    

