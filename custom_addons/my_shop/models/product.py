from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    is_featured = fields.Boolean(
        string='Featured Product',
        default=False
    )