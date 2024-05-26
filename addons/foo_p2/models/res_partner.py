from odoo import models, api, fields

class ResPartner(models.Model):
    _inherit = "res.partner"

    @api.model
    def get_view(self, view_id=None, view_type="form", **options):
        current_user_groups = self.env.user.groups_id.mapped("name")
        if view_type == "form" and "Group P2" in current_user_groups:
            view_id = self.env.ref("foo_p2.res_partner_form_p2_primary").id
        res = super().get_view(view_id=view_id, view_type=view_type, **options)
        return res

