 
 
from odoo import models, fields, api

class product(models.Model):
    _name = 'product'
    _description = 'product description'

   name = fields.Char( #ชื่อสินค้า
    string='Product Name', 
    required=True,
    )
    picture = fields.Char() #รูปภ่าพ
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
   saleprice = fields.Float(  #ราคาขาย
    string='Saleprice',
    required=True,
       )
    cost = fields.Float( #ต้นทุนที่รับมา
    string='Cost',
    required=True,
       )
component_id = fields.One2many(  #ชิ้นส่วนของ product
        comodel_name='component',
        string='component',
    )
orderdate = fields.Char(  #วันที่สั่งซื้อ
    string='Orderdate',
    required=True,
    )