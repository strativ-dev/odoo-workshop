from odoo import fields, models


class Item(models.Model):
    _name = "strativ.inventory.item"
    _description = "Strativ inventory items"

    name = fields.Char(string="Name", required=True)
    buy_price = fields.Float(string="Buy price", required=True)
    buy_date = fields.Date(string="Buy date", required=True)
    description = fields.Text(string="Description")
    image = fields.Image(string="Image", max_width=1920, max_height=1920)