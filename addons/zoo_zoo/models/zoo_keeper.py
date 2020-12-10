# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class ResPartner(models.Model):
#     _inherit = 'res.partner'

#     is_keeper = fields.Boolean(
#         name='is_keeper',
#     )   

class keeper(models.Model):
    _name = 'keeper'
    _description = 'person who take care animal in zoo'


    name = fields.Char(
        string='Firstname',
        required=True,
    )
    surname = fields.Char(
        string='Lastname',
        required=True,
    )
    picture = fields.Char()
    age = fields.Integer(
        string='Age',
        required=True,
    )
    sex = fields.Selection(
        [
            ('male', 'Male'),
            ('female', 'Female'),
        ],
        default='male',
    )
    address = fields.Char(
        string='Address',
        required=True
    )
    phone = fields.Char(
        string='Phone number',
        required=True
    )
    # animal_id = fields.One2many(
    #     comodel_name='animal',
    #     string='Animal in career',
    # )
    # animal_name = fields.Char(
    #     string='Animal name',
    #     related='animal_id.name',
    # )

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100