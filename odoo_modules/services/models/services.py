# -*- coding: utf-8 -*-

from odoo import api, models, fields, _
from odoo.addons.http_routing.models.ir_http import slug
from odoo.tools.translate import html_translate
import json

class ServicesCategories(models.Model):
    _name = 'services.categories'
    _description = "Services category"
    _inherit = ['website.seo.metadata','website.published.multi.mixin']
    
    _order = 'id DESC'
    _mail_post_access = 'read'
    
    
    @api.multi
    @api.depends('name')
    def _compute_website_url(self):
        super(ServicesCategories, self)._compute_website_url()
        for category in self:
            category.website_url = "/services/%s" % (slug(category))
    
    # @api.multi
    # @api.depends('alias','parent_id')
    # def _compute_website_url(self):
    #     this = self

    #     for category in self:
    #         category_for_path = category
    #         parents_path = [category];
    #         while category_for_path.parent_id:
    #             parents_path = parents_path + [category_for_path.parent_id]
    #             category_for_path = category_for_path.parent_id
    #         parents_path = parents_path + [root_element]
            
    #         parents_path_alias = []
    #         parents_path_breadcrumbs_items = []
    #         for item in parents_path:
    #             # print(item.website_url)
    #             parents_path_alias = parents_path_alias + [item.alias or slug(item.name)]
    #             if item.name != category.name:
    #                 parents_path_breadcrumbs_items = parents_path_breadcrumbs_items + [{'name':item.name,'url':item.website_url}]

    #         category.website_url = '/' + '/'.join(reversed(parents_path_alias)) + '/'
    #         category.breadcrumbs = json.dumps(parents_path_breadcrumbs_items, ensure_ascii=False)
    
    @api.multi
    @api.depends('alias','parent_id')
    def _compute_breadcrumbs(self):
        # this = self
        # root_element = this.env['capabilities.capabilities'].search([('alias', '=', 'capabilities')])

        # for category in self:
        #     category_for_path = category
        #     parents_path = [category];
        #     while category_for_path.parent_id: 
        #         parents_path = parents_path + [category_for_path.parent_id]
        #         category_for_path = category_for_path.parent_id
        #     parents_path = parents_path + [root_element]
        #     parents_path = reversed(parents_path)
        #     print('----------------------')
        #     print(parents_path)
        #     print('----------------------')
        #     parents_path_breadcrumbs = []
        #     for item in parents_path:
        #         print('======================')
        #         print(item.name)
        #         print(item.website_url)
        #         print('======================')
        #         parents_path_breadcrumbs = parents_path_breadcrumbs + [{'name': item.name, 'url': item.website_url}]
            # print(parents_path_breadcrumbs)

        self.breadcrumbs = 'dfdfdf'

    def _default_content(self):
        return '''
            <section class="s_text_block">
                <div class="container">
                    <div class="row">
                        <div class="col-lg-12 mb16 mt16">
                            <p class="o_default_snippet_text">''' + _("Start writing here...") + '''</p>
                        </div>
                    </div>
                </div>
            </section>
        '''
    
    name = fields.Char('Category Name', required=True, translate=True)
    alias = fields.Char('Alias', help='SEO name')

    parent_id = fields.Many2one('services.categories', string='Parent Category', index=True, default= None)
    child_id = fields.One2many('services.categories', 'parent_id', string='Children Categories')
    

    breadcrumbs = fields.Char('Breadcrumbs dict', compute='_compute_breadcrumbs', store = True, help='Dict with URL and name breadrumbs items')
    
    
    content = fields.Html('Content', default=_default_content, translate=html_translate, sanitize=False)