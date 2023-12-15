# -*- coding: utf-8 -*-
# from odoo import http


# class SiremaAhp(http.Controller):
#     @http.route('/sirema_ahp/sirema_ahp', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sirema_ahp/sirema_ahp/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sirema_ahp.listing', {
#             'root': '/sirema_ahp/sirema_ahp',
#             'objects': http.request.env['sirema_ahp.sirema_ahp'].search([]),
#         })

#     @http.route('/sirema_ahp/sirema_ahp/objects/<model("sirema_ahp.sirema_ahp"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sirema_ahp.object', {
#             'object': obj
#         })
