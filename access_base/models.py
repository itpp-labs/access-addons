# -*- coding: utf-8 -*-
from lxml import etree
from lxml.builder import E

from odoo import api, fields, models
from odoo.tools.translate import _

from odoo.addons.base.res.res_users import name_boolean_group, name_selection_groups


class GroupsView(models.Model):
    _inherit = "res.groups"
    is_custom_group = fields.Boolean(
        "Custom Group", help="show group at the top of Access Rights tab in user form"
    )

    @api.model
    def _update_user_groups_view(self):
        # call super to make module compatible with other modules (e.g. access_restricted)
        super(GroupsView, self)._update_user_groups_view()

        if self._context.get("install_mode"):
            # use installation/admin language for translatable names in the view
            user_context = self.env["res.users"].context_get()
            self = self.with_context(**user_context)

        # We have to try-catch this, because at first init the view does not
        # exist but we are already creating some basic groups.
        view = self.env.ref("base.user_groups_view", raise_if_not_found=False)
        if view and view.exists() and view._name == "ir.ui.view":
            group_no_one = view.env.ref("base.group_no_one")
            xml1, xml2 = [], []
            xml1.append(E.separator(string=_("Application"), colspan="2"))

            xml3 = []
            xml3.append(E.separator(string=_("Custom User Groups"), colspan="4"))

            for app, kind, gs in self.get_groups_by_application():
                xml = None
                custom = False
                if (
                    kind == "selection"
                    and any([g.is_custom_group for g in gs])
                    or all([g.is_custom_group for g in gs])
                ):
                    xml = xml3
                    custom = True

                # hide groups in category 'Hidden' (except to group_no_one)
                attrs = (
                    {"groups": "base.group_no_one"}
                    if app
                    and (
                        app.xml_id == "base.module_category_hidden"
                        or app.xml_id == "base.module_category_extra"
                    )
                    and not custom
                    else {}
                )

                if kind == "selection":
                    xml = xml or xml1
                    # application name with a selection field
                    field_name = name_selection_groups(map(int, gs))
                    xml.append(E.field(name=field_name, **attrs))
                    xml.append(E.newline())
                else:
                    xml = xml or xml2
                    # application separator with boolean fields
                    app_name = app and app.name or _("Other")
                    if not custom:
                        xml.append(E.separator(string=app_name, colspan="4", **attrs))
                    for g in gs:
                        field_name = name_boolean_group(g.id)
                        if g == group_no_one:
                            # make the group_no_one invisible in the form view
                            xml.append(E.field(name=field_name, invisible="1", **attrs))
                        else:
                            xml.append(E.field(name=field_name, **attrs))

            xml2.append({"class": "o_label_nowrap"})
            xml = E.field(
                E.group(*(xml3), col="2"),
                E.group(*(xml2), col="4"),
                E.group(*(xml1), col="2"),
                name="groups_id",
                position="replace",
            )
            xml.addprevious(etree.Comment("GENERATED AUTOMATICALLY BY GROUPS"))
            xml_content = etree.tostring(
                xml, pretty_print=True, xml_declaration=True, encoding="utf-8"
            )
            view.write({"arch": xml_content})
        return True
