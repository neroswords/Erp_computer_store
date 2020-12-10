# -*- coding: utf-8 -*-

from odoo import models, fields, api

class sell(models.Model):
    _name = 'sell'
    _description = 'all money flow'


    product_id = fields.One2many(  
        comodel_name='product',
        string='product',
        inverse_name='sell_id'
    )
    product_name = fields.Char(  #สินค้าที่ขาย
        string='name',
        related='product_id.name',
    )
    unitprice = fields.Float(  #ราคาต่อหน่วย
        string='Unitprice',
        required=True,
    )
    count = fields.Integer(  #จำนวนสินค้า
        string='count',
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

