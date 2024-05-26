from odoo import models, fields

class ResPartner(models.Model):
    _inherit = "res.partner"

    base = fields.Char(string="base")

    p1 = fields.Char(string="p1")
    p2 = fields.Char(string="p2")

    p1_primary = fields.Char(string="p1 primary")
    p2_primary = fields.Char(string="p2 primary")

    extend = fields.Char(string="extend")
    p1_primary_extend = fields.Char(string="p1 primary extend")
    p2_primary_extend = fields.Char(string="p2 primary extend")
