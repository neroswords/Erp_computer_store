# -*- coding: utf-8 -*-

from odoo import models, fields


class partner(models.Model):
    _inherit = 'res.partner'

    creator = fields.Boolean(
        name='creator',
        default = False
    )