from odoo import models, api, fields

class ResPartner(models.Model):
    _inherit = "res.partner"

    p1 = fields.Char(string="p1")
    p1_primary = fields.Char(string="p1 primary")

    @api.model
    def get_view(self, view_id=None, view_type="form", **options):
        current_user_groups = self.env.user.groups_id.mapped("name")
        if view_type == "form" and "Group P1" in current_user_groups:
            view_id = self.env.ref("foo_p1.res_partner_form_p1_primary").id
        res = super().get_view(view_id=view_id, view_type=view_type, **options)
        return res

