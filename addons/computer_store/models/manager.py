# -*- coding: utf-8 -*-

from odoo import models, fields, api


class manage(models.Model):
    _inherit = 'seller'

    
    is_manager = fields.Boolean(
        name='manager',
        default = False
    )
