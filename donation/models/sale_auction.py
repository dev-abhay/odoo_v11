from odoo import models, fields, api

class PurchaseOrder(models.Model):
    _inherit='sale.order'
    _name = 'donation.auction'
    
    auction_customer = fields.Many2many('res.partner', string="Customer", domain=[('customer', '=', True)])
    # source_do = fields.Char('Source Donation Order')


    # @api.multi
    # def auction_invitation(self):
    # 	for customer in self.auction_customer:
    # 		self.send_invitation_email(customer)
    # 	pass

    # @api.multi
    # def send_invitation_email(self,customer):
    # 	pass
    	
