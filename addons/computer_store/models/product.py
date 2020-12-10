 
 
from odoo import models, fields, api

class product(models.Model):
    _name = 'product'
    _description = 'product description'

    name = fields.Char( #ชื่อสินค้า
        string='Product Name', 
        required=True,
    )
    picture = fields.Image()
    brand = fields.Char(  #ยี่ห้อของสินค้า
        string='brand Product',
        required=True,
    )
    count = fields.Integer(  #จำนวนสินค้า
        string='Count',
        required=True,
    )
    vendor = fields.Char(  #บริษัทที่รับมา
        string='Vendor',
        required=True,
    )
    saleprice = fields.Float(#ราคาขาย
        string='Saleprice',
        required=True,
    )
    cost = fields.Float( #ต้นทุนที่รับมา
        string='Cost',
        required=True,
    )
    # product_line = fields.One2many(
    #     'product_line',
    #     'product_id',
    #     string="Component"

    # )
    orderdate = fields.Char(  #วันที่สั่งซื้อ
        string='Orderdate',
        required=True,
    )
    # product_id = fields.Many2one(
    #     comodel_name='product',
    #     string='product',
    # )
    component_id = fields.One2many(
        comodel_name='component',
        string='component',
        inverse_name='product_id'
    )
    component_name = fields.Char(
        string='component name',
        related='component_id.name',
    )
    component_qty = fields.Integer(
        string='Quantity'
    )
