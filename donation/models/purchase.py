# -*- coding: utf-8 -*-

from odoo import models, fields, api

class PurchaseOrder(models.Model):
    _inherit='purchase.order'
    
    is_a_unnkown_item = fields.Boolean(string  = "Unknown Item" , widget="radio",default=True)
    product_lines = fields.One2many('purchase.requisition.line',"product_lines", string='Product Lines')
    box_numbers=fields.Float('Number of Boxes')
    contact_number=fields.Char('Contact Number')
    receipt_address=fields.Text('Receipt Address')
    donation_type = fields.Many2one('donation.category')
    donation_description = fields.Char(string="Donation Description")