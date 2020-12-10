# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Slot(models.Model):
    _name = 'slot'
    _description = 'Garden Slot'

    name = fields.Char(
        string='Slot Name',
        required=True,
    )
    plot_id = fields.Many2one(
        comodel_name='plot',
        string='Plot',
    )
    plot_name = fields.Char(
        string='Plot Name',
        related='plot_id.name',
    )
    is_blue = fields.Boolean(
        string='Is Blue'
    )
    is_yellow = fields.Boolean(
        string='Is Yellow'
    )
