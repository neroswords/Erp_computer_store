
from odoo import models, fields, api

class component(models.Model):
    _name = 'component'
    _description = 'component for computer'
    name = fields.Char( #ชื่อของชิ้นส่วน
        string='Component name', 
        required=True,
    )
    picture = fields.Char() #รูปภ่าพ
    brand = fields.Char(  #ยี่ห้อชิ้นส่วน
        string='Brand of product',
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
    saleprice = fields.Float(  #ราคาขาย
        string='Saleprice',
        required=True,
    )
    cost = fields.Float( #ต้นทุนที่รับมา
        string='Cost',
        required=True,
    )
    orderdate = fields.Char(  #วันที่สั่งซื้อ
        string='Orderdate',
        required=True,
    )
    product_id = fields.Many2one(
        comodel_name='product',
        string='product',
    )
    
