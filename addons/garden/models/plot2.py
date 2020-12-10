# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Plot2(models.Model):
    _name = 'plot2'
    _description = 'Garden Plot2'

    name = fields.Char(
        string='Plot Name',
        required=True,
    )
    plot_type2 = fields.Char(
        string='Type2',
        required=True,
    )
    slot2_ids = fields.One2many(
        comodel_name='slot2',
        inverse_name='plot2_id',
        string='Slot2 List',
    )
    state = fields.Selection(
        [
            ('draft', 'Draft'),
            ('process', 'Process'),
        ],
        default='draft',
    )

    def action_process(self):
        for rec in self:
            rec.state = 'process'
            rec.plot_type2 = 'Hello'