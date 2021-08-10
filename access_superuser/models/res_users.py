from odoo import fields, models
from odoo.exceptions import UserError
from odoo.tools.translate import _


class Users(models.Model):
    _inherit = "res.users"

    is_sudoer = fields.Boolean(
        default=True,
        help="""
Is a User eligible to become a Superuser. If True and User is Admin (Administrator: Settings) - then ok""",
    )

    def write(self, vals):
        """
        if writing True in is_sudoer
        check if system user
        then let it pass or raise user error
        """

        if "is_sudoer" in vals and vals["is_sudoer"]:
            if self.env.is_superuser() and self._is_system():
                pass
            else:
                raise UserError(
                    _(
                        """
                        Insufficient rights for making someone a Sudoer
                        (You yourself should be in Superuser mode)
                        or this User is not a System User
                        (Administration: Settings)!"""
                    )
                )

        if "is_sudoer" in vals and not vals["is_sudoer"]:
            if self.env.is_superuser():
                raise UserError(
                    _(
                        """
                        To clear 'Is Sudoer' setting -
                        please exit from Superuser mode,
                        this way the System can
                        check that you are not trying to do it
                        on your own, which is prohibited
                        because someone should be a sudoer"""
                    )
                )
            elif self == self.env.user:
                raise UserError(
                    _(
                        """
                        You cannot uncheck 'Is Sudoer' setting on yourself -
                        this prevents the situation when no one is
                        eligible becoming Superuser"""
                    )
                )

        return super(Users, self).write(vals)
