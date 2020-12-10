# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Animal(models.Model):
    _name = 'animal'
    _description = 'animal description'

    name = fields.Char(
        string='Animal Name',
        required=True,
    )
    picture = fields.Char()
    age = fields.Integer(
        string='Animal Age',
        required=True,
    )
    sex = fields.Char(
        string='Sex',
        required=True,
    )
    type_of_animal = fields.Char(
        string='Type of animal',
        required=True,
    )
    description = fields.Char(
        string='Description',
    )
    food = fields.Char(
        string='Food',
        required=True,
    )
    keeper_id = fields.Many2one(
        comodel_name='keeper',
        string='Zoo Keeper',
    )
    zoo_keeper_name = fields.Char(
        string='Zoo keeper name',
        related='keeper_id.name',
    )
    cage_id = fields.Many2one(
        comodel_name='cage',
        string='Cage',
    )
    cage_name = fields.Char(
        string='Cage name',
        related='cage_id.name',
    )
