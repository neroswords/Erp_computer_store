# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Zone(models.Model):
    _name = 'zone'
    _description = 'zone description'

    name = fields.Char(
        string='Zone Name',
        required=True,
    )
    picture = fields.Char()
    description = fields.Char(
        string='Description',
    )
    toilet_number = fields.Integer(
        string='Slot Name',
        required=True,
    )
    # cage_id = fields.One2many(
    #     comodel_name='cage',
    #     string='Cage',
    # )
    # cage_name = fields.Char(
    #     string='Cage name',
    #     related='cage_id.name',
    # )