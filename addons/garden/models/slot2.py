# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Slot2(models.Model):
    _name = 'slot2'
    _description = 'Garden Slot'

    name = fields.Char(
        string='Slot Name',
        required=True,
    )
    plot2_id = fields.Many2one(
        comodel_name='plot2',
        string='Plot2',
    )
