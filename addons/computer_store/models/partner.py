# -*- coding: utf-8 -*-

from odoo import models, fields


class partner(models.Model):
    _inherit = 'res.partner'

    manager = fields.Boolean(
        name='Manager',
    )