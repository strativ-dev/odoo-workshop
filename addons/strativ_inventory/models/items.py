from odoo import fields, models


class Item(models.Model):
    _name = "strativ.inventory.item"
    _description = "Strativ Inventory Item"

    name = fields.Char(string="Name", required=True)
    buy_price = fields.Float(string="Buy Price")
    buy_date = fields.Date(string="Buy Date")
    description = fields.Text()
    image = fields.Image(string="Image", max_width=1920, max_height=1920)
