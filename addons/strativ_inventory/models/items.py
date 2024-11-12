from odoo import fields, models


class Item(models.Model):
    _name = "strativ.inventory.item"
    _description = "Strativ Inventory Item"

    name = fields.Char(string="Name")
    buy_price = fields.Float(string="Buy Price")
    buy_date = fields.Date(string="Buy Date", default=fields.Datetime.now)
    description = fields.Text()
    image = fields.Image(string="Image", max_width=1920, max_height=1920, copy=False)
    active = fields.Boolean(string="Active", default=True)
    state = fields.Selection(
        selection=[
            ('bought', 'Bought'),
            ('pending', 'Pending'),
            ('allocated', 'Allocated')
        ],
        string="State",
        default='pending',
        required=True
    )
    category_id = fields.Many2one("inventory.category", string = "Inventory Category")
    admin = fields.Many2one('res.users', string="Office Admin", default=lambda self: self.env.user)
    employee = fields.Many2one('res.partner', string="Employee")
    tag = fields.Many2many('inventory.tags', string="Tag")

class ItemCategory(models.Model):
    _name = "inventory.category"
    _description = "Inventory Categories"
    _rec_name = 'type'
    
    type = fields.Char(string="Category", required = True)