from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    mailbox_address = fields.Many2one(comodel_name="mailbox.address")
    billing_address = fields.Many2one(comodel_name="billing.address")
    mailbox_address_name = fields.Char(
        string="Mailbox name", compute="_compute_mailbox_address_name"
    )

    @api.depends("mailbox_address")
    def _compute_mailbox_address_name(self):
        self.mailbox_address_name = self.mailbox_address.mailbox_name
        print("hello world!")
        print("bye world")
