# -*- coding: utf-8 -*-
from openerp import http

# class Dmpyme(http.Controller):
#     @http.route('/dmpyme/dmpyme/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dmpyme/dmpyme/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('dmpyme.listing', {
#             'root': '/dmpyme/dmpyme',
#             'objects': http.request.env['dmpyme.dmpyme'].search([]),
#         })

#     @http.route('/dmpyme/dmpyme/objects/<model("dmpyme.dmpyme"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dmpyme.object', {
#             'object': obj
#         })