from odoo import models, fields, api


class SaleOrderMission(models.Model):
    _inherit = "sale.order"

    # On récupère le nom du produit via la première ligne de commande
    mission_name = fields.Char(
        related='order_line.product_id.name', 
        string="Nom de la Mission",
        readonly=True,
        store=True # Recommandé pour pouvoir faire des recherches ou trier par nom de mission
    )