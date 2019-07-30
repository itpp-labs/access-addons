from odoo import models, api


class ResUsers(models.Model):
    _inherit = 'res.users'

    @api.multi
    def action_clear_access_rights(self):
        self.ensure_one()
        admin_groups = [
            self.env.ref('base.group_user').id,
            self.env.ref('base.group_erp_manager').id,
            self.env.ref('base.group_system').id,
        ]

        user_types = [
            self.env.ref('base.group_portal').id,
            self.env.ref('base.group_public').id,
            self.env.ref('base.group_user').id,
        ]

        groups_id = []
        for g in self.groups_id:
            if self.env.uid == self.id and g.id in admin_groups or g.id in user_types:
                # don't allow for Administrator to clear his admin rights
                # don't clear user type
                continue
            groups_id.append((3, g.id))
        self.write({'groups_id': groups_id})
        return True
