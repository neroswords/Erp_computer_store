# -*- coding: utf-8 -*-

from odoo import models, fields, api


class seller(models.Model):
  _name = 'seller'
  _description = 'seller description'

  name = fields.Char(
      string='Seller Name',
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
  education = fields.Char(
      string='Education',
      required=True
  )
 


