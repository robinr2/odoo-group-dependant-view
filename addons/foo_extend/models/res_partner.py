from odoo import models, fields

class ResPartner(models.Model):
    _inherit = "res.partner"

    extend = fields.Char(string="extend")
    p1_extend = fields.Char(string="p1 extend")
    p2_extend = fields.Char(string="p2 extend")
    p1_primary_extend = fields.Char(string="p1 primary extend")
    p2_primary_extend = fields.Char(string="p2 primary extend")
