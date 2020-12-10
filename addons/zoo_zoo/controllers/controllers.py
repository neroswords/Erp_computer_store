# -*- coding: utf-8 -*-
# from odoo import http


# class ZooZoo(http.Controller):
#     @http.route('/zoo_zoo/zoo_zoo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/zoo_zoo/zoo_zoo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('zoo_zoo.listing', {
#             'root': '/zoo_zoo/zoo_zoo',
#             'objects': http.request.env['zoo_zoo.zoo_zoo'].search([]),
#         })

#     @http.route('/zoo_zoo/zoo_zoo/objects/<model("zoo_zoo.zoo_zoo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('zoo_zoo.object', {
#             'object': obj
#         })
