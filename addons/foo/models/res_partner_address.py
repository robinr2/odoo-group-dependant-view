from odoo import models, fields


class Address(models.Model):
    _name = "address"

    postcode = fields.Char()
    city = fields.Char()
    street = fields.Char()
    street_number = fields.Char()

class MailboxAdress(models.Model):
    _name = "mailbox.address"
    _inherits = {"address": "address_id"}

    address_id = fields.Many2one(comodel_name="address", required=True, ondelete="cascade")
    mailbox_name = fields.Char()


class BillingAddress(models.Model):
    _name = "billing.address"
    _inherits = {"address": "address_id"}

    address_id = fields.Many2one(comodel_name="address", required=True, ondelete="cascade")
    email = fields.Char()
