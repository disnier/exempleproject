# -*- coding: utf-8 -*-
# from odoo import http


# class Addfield(http.Controller):
#     @http.route('/addfield/addfield', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/addfield/addfield/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('addfield.listing', {
#             'root': '/addfield/addfield',
#             'objects': http.request.env['addfield.addfield'].search([]),
#         })

#     @http.route('/addfield/addfield/objects/<model("addfield.addfield"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('addfield.object', {
#             'object': obj
#         })
