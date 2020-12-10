# -*- coding: utf-8 -*-

from odoo import models, fields, api

class accounting(models.Model):
    _name = 'accounting'
    _description = 'all money flow'

productname = fields.Char(  #สินค้าที่ขาย
    string='Productname',
    required=True,
    )
unitprice = fields.Float(  #ราคาต่อหน่วย
    string='Unitprice',
    required=True,
       )
count = fields.Integer(  #จำนวนสินค้า
    string='countp',
    required=True,
    )
Total = fields.Integer(  #จำนวนสินค้าทุกรายการในบัญชี
    string='Total Product ',
    required=True,
    )
Sales  = fields.Float(  #ยอดขาย
    string='Sales',
    required=True,
       )
saledate = fields.Char(  #วัน-เวลาที่ขาย
    string='Saledate',
    required=True,
    )
seller_id = fields.One2one(  #คนที่ขาย
        comodel_name='seller',
        string='seller',
    )

