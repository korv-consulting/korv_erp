from odoo import models, fields, _
from odoo.exceptions import UserError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    # --- Informations Contractuelles ---
    is_contract = fields.Boolean(string="Est un contrat de mission", default=False)

    # Objet et Cadre
    mission_object = fields.Char(string="Objet de la mission")
    mission_location = fields.Char(string="Lieu d'exécution")

    # Dates de validité
    contract_start_date = fields.Date(string="Date de début")
    contract_end_date = fields.Date(string="Date de fin")

    # Clauses juridiques de base
    termination_notice = fields.Integer(string="Préavis de résiliation (jours)", default=30)
    payment_terms_desc = fields.Char(string="Modalités de règlement", help="Ex: 30 jours fin de mois")

    # Zone de texte libre pour le corps du contrat
    specific_clauses = fields.Html(string="Clauses spécifiques et Obligations")

    def action_print_contract(self):
        """Imprimer le contrat de mission pour cette commande.

        - Vérifie que la commande est confirmée et marquée comme contrat de mission.
        - Vérifie que les champs clés du contrat sont renseignés.
        - Si tout est bon, lance le report QWeb.
        """
        for order in self:
            if order.state not in ('sale', 'done'):
                raise UserError(_(
                    "Vous ne pouvez imprimer le contrat que pour une commande confirmée."
                ))

            if not order.is_contract:
                raise UserError(_(
                    "Cette commande n'est pas marquée comme contrat de mission."
                ))

            required_fields = [
                'mission_object',
                'mission_location',
                'contract_start_date',
                'contract_end_date',
                'payment_terms_desc',
            ]

            missing = [f for f in required_fields if not getattr(order, f)]
            if missing:
                labels = [order._fields[f].string for f in missing]
                raise UserError(_(
                    "Veuillez renseigner les champs suivants avant d'imprimer le contrat de mission : %s"
                ) % ", ".join(labels))

        return self.env.ref(
            'mission_contract.action_report_mission_contract_print'
        ).report_action(self)
