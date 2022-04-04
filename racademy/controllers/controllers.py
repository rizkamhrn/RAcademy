# -*- coding: utf-8 -*-
# from odoo import http


# class Racademy(http.Controller):
#     @http.route('/racademy/racademy/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/racademy/racademy/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('racademy.listing', {
#             'root': '/racademy/racademy',
#             'objects': http.request.env['racademy.racademy'].search([]),
#         })

#     @http.route('/racademy/racademy/objects/<model("racademy.racademy"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('racademy.object', {
#             'object': obj
#         })
