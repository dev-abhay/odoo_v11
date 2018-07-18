# -*- coding: utf-8 -*-
from odoo import http

# class Donation(http.Controller):
#     @http.route('/donation/donation/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/donation/donation/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('donation.listing', {
#             'root': '/donation/donation',
#             'objects': http.request.env['donation.donation'].search([]),
#         })

#     @http.route('/donation/donation/objects/<model("donation.donation"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('donation.object', {
#             'object': obj
#         })