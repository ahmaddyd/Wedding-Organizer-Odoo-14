# -*- coding: utf-8 -*-
# from odoo import http


# class Weddingorganizer(http.Controller):
#     @http.route('/weddingorganizer/weddingorganizer/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/weddingorganizer/weddingorganizer/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('weddingorganizer.listing', {
#             'root': '/weddingorganizer/weddingorganizer',
#             'objects': http.request.env['weddingorganizer.weddingorganizer'].search([]),
#         })

#     @http.route('/weddingorganizer/weddingorganizer/objects/<model("weddingorganizer.weddingorganizer"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('weddingorganizer.object', {
#             'object': obj
#         })
