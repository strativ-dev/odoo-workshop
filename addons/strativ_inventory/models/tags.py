from odoo import fields, models

class Employees(models.Model):
    _name = "inventory.tags"
    _description = "Inventory Tags"
    _rec_name = 'tag_name'
    
    tag_name = fields.Char(string = "Tag")
    