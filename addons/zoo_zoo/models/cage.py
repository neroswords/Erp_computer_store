# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Cage(models.Model):
    _name = 'cage'
    _description = 'cage description'

    name = fields.Char(
        string='Slot Name',
        required=True,
    )
    picture = fields.Char()
    description = fields.Char(
        String='Description'
    )
    # animal_id = fields.One2many(
    #     comodel_name='animal',
    #     string='Animal in career',
    # )
    # animal_name = fields.Char(
    #     string='Animal name',
    #     related='animal_id.name',
    # )
    zone_id = fields.Many2one(
        comodel_name='zone',
        string='Zone',
    )
    zone_name = fields.Char(
        string='Zone name',
        related='zone_id.name',
    )