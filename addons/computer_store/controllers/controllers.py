# -*- coding: utf-8 -*-
# from odoo import http


# class ComputerStore(http.Controller):
#     @http.route('/computer_store/computer_store/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/computer_store/computer_store/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('computer_store.listing', {
#             'root': '/computer_store/computer_store',
#             'objects': http.request.env['computer_store.computer_store'].search([]),
#         })

#     @http.route('/computer_store/computer_store/objects/<model("computer_store.computer_store"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('computer_store.object', {
#             'object': obj
#         })
