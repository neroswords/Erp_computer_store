# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_gardener = fields.Boolean(
        name='Is Gardener',
    )   


class Gardener(models.Model):
    _name = 'gardener'
    _description = 'Gardener'

    name = fields.Char(
        string='Plot Name',
        required=True,
    )

    plot_ids = fields.Many2many(
        comodel_name='plot',
        relation='gardener_plot_rel',
        column1='gardener_id',
        column2='plot_id',
        string='Plot',
    )