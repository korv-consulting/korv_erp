from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def _sla_default_mission_name(self):
        """Retourne un nom de mission par défaut basé sur la commande."""
        self.ensure_one()
        # On prend le nom de la première ligne de commande si possible,
        # sinon on retombe sur le nom de la commande.
        if self.order_line:
            return self.order_line[0].name
        return self.name

    def action_open_sla_contract(self):
        """Ouvre les SLA liés à cette commande ou prépare un nouveau SLA.

        - Préremplit partner, sale_order et mission_name.
        - Laisse tout modifiable par l'utilisateur.
        """
        self.ensure_one()

        action = self.env['ir.actions.act_window']._for_xml_id('sla_contract.action_sla_contract')

        # On force l'ouverture directe du formulaire en création
        form_view = self.env.ref('sla_contract.view_sla_contract_form')
        action.update({
            'views': [(form_view.id, 'form')],
            'view_mode': 'form',
            'target': 'current',
            'res_id': False,
        })

        # Construire un context propre (les actions ont souvent un context en texte)
        ctx = dict(self.env.context or {})
        ctx.update({
            'default_sale_order_id': self.id,
            'default_partner_id': self.partner_id.id,
            'default_mission_name': self._sla_default_mission_name(),
            'form_view_initial_mode': 'edit',
        })
        action['context'] = ctx
        return action

