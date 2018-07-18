# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Donation(models.Model):
    _name = 'donation.category'
    _rec_name = 'category_name'

    category_name = fields.Char(string="Category Name", required=True)
    
class SupplierInfo(models.Model):
    _inherit='product.supplierinfo'
    
    name = fields.Many2one(
        'res.partner', 'Donor',
        domain=[('supplier', '=', True)], ondelete='cascade', required=True,
        help="Donor of this product")
    product_name = fields.Char(
        'Donor Product Name',
        help="This vendor's product name will be used when printing a request for quotation. Keep empty to use the internal one.")
    product_code = fields.Char(
        'Donor Product Code',
        help="This vendor's product code will be used when printing a request for quotation. Keep empty to use the internal one.")

class ProductTemplate(models.Model):
    _inherit = 'product.template'
    
    
    purchase_requisition = fields.Selection(
        [('rfq', 'Create a draft donation order'),
         ('tenders', 'Propose a call for tenders')],
        string='Procurement', default='rfq')
        