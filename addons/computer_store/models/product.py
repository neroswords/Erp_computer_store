 
 
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
    Total = fields.Float(  #จำนวนสินค้าทุกรายการในบัญชี
        string='Total',
        inverse='_total',
    )
    component_id = fields.One2many(  #ชิ้นส่วนของ product
        comodel_name='component',
        string='component',
        inverse_name='product_id'
    )
    component_name = fields.Char(
        string='component name',
        related='component_id.name',
    )
    orderdate = fields.Char(  #วันที่สั่งซื้อ
        string='Orderdate',
        required=True,
    )
<<<<<<< HEAD
    orderdate2 = fields.Char(  #วันที่สั่งซื้อ
        string='Orderdate2',
        required=True,
    )
    @api.depends('Total')
    def _total(self):
        for rec in self:
            rec.Total = rec.saleprice * rec.count 
=======
    
>>>>>>> b1d65746e9e05b994d079501f3235ea82e0e1e1c
