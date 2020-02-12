// Copyright 2018 Rafis Bikbov <https://www.it-projects.info/team/RafiZz>
// License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).
odoo.define("access_apps_website.tour", function(require) {
    "use strict";

    var tour = require("web_tour.tour");
    var base = require("web_editor.base");

    var core = require("web.core");
    var _t = core._t;

    var options = {
        test: true,
        url: "/",
        wait_for: base.ready(),
    };

    var name = "Blogs";
    var msg = _t('"%s" App is not installed in the system.');
    var expected_content = _.str.sprintf(msg, name);

    var tour_name = "access_apps_website.tour";
    tour.register(tour_name, options, [
        {
            content: 'Click "New" button',
            trigger: "#new-content-menu > a",
        },
        {
            content: 'Click "New Blog Post" button',
            extra_trigger: "#o_new_content_menu_choices",
            trigger: "#o_new_content_menu_choices a[data-action=new_blog_post]",
        },
        {
            content: "Check modal window text",
            extra_trigger: ".modal.o_technical_modal.show.modal_shown",
            trigger: _.str.sprintf(".modal-body:contains(%s)", expected_content),
        },
    ]);
});
