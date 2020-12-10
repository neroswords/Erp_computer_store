# -*- coding: utf-8 -*-
# from odoo import http


# class Garden(http.Controller):
#     @http.route('/garden/garden/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/garden/garden/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('garden.listing', {
#             'root': '/garden/garden',
#             'objects': http.request.env['garden.garden'].search([]),
#         })

#     @http.route('/garden/garden/objects/<model("garden.garden"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('garden.object', {
#             'object': obj
#         })
