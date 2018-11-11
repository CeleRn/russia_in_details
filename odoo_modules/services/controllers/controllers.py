# -*- coding: utf-8 -*-
from odoo import http
import json

class Services(http.Controller):
    @http.route('/services/', type='http', auth='public', website=True)
    def index(self, **kw):
        Category =  http.request.env['services.categories'].sudo().search([('alias','=','services')],limit=1)
        Categories = http.request.env['services.categories'].sudo().search([('alias','!=','services')],limit=1)
        return http.request.render('services.index', {
            'categories': Categories.search([]),
            'main_object': Category
        })
        
    @http.route('/services/<alias_of_category>/', type='http', auth='public', website=True)
    def alias_of_category(self,alias_of_category, **kw):
        Category =  http.request.env['services.categories'].sudo().search([('alias','=',alias_of_category)],limit=1)
        if not Category:
            Category =  http.request.env['services.categories'].sudo().search([('alias','=',alias_of_category)],limit=1)
        values = {
            'category': Category,
            'main_object': Category
        }
        return http.request.render('services.category', values)