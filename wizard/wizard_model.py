# -*- coding: utf-8 -*-

from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError,ValidationError
from odoo.tools import float_is_zero, pycompat
from odoo.addons import decimal_precision as dp
from datetime import date
import os
import base64
from collections import defaultdict

class ArchiveProductPricelistItem(models.TransientModel):
    _name = 'archive.product.pricelist.item'

    def btn_archive(self):
        item_ids = self.env.context.get('active_ids',[])
        for item_id in item_ids:
            item = self.env['product.pricelist.item'].browse(item_id)
            value = item.active
            if not value:
                item.active = True
            else:
                item.active = False
