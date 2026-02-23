# -*- coding: utf-8 -*-
# from odoo import http


# class OmMissions(http.Controller):
#     @http.route('/om_missions/om_missions', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/om_missions/om_missions/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('om_missions.listing', {
#             'root': '/om_missions/om_missions',
#             'objects': http.request.env['om_missions.om_missions'].search([]),
#         })

#     @http.route('/om_missions/om_missions/objects/<model("om_missions.om_missions"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('om_missions.object', {
#             'object': obj
#         })

