# -*- coding: utf-8 -*-

import models

from openerp import SUPERUSER_ID
from collections import OrderedDict
from openerp.tools import float_compare

def pre_init_hook(cr, registry):
    # It is necessary for compatibility with the module "access_restricted"
    registry['res.groups'].update_user_groups_view(cr, SUPERUSER_ID)
    return
