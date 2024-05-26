from odoo import models, fields

class ResPartner(models.Model):
    _inherit = "res.partner"

    base = fields.Char(string="base")
