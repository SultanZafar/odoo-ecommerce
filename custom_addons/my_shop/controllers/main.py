# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class MyShopController(http.Controller):

    @http.route('/featured-products', auth='public', website=True)
    def featured_products(self, **kw):
        # Database se sirf featured products lo
        products = request.env['product.template'].sudo().search([
            ('is_featured', '=', True),
            ('website_published', '=', True),
        ])
        # Page render karo
        return request.render('my_shop.featured_products_page', {
            'products': products,
        })