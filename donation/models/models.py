# -*- coding: utf-8 -*-

from odoo import models, fields, api
import datetime

class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_a_donor = fields.Boolean(string  = "Is a Donor" , widget="radio")

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    state = fields.Selection([
        ('draft', 'Draft Donation Order'),
        ('sent', 'DO Sent'),
        ('to approve', 'To Approve'),
        ('purchase', 'Donation Order'),
        ('done', 'Locked'),
        ('cancel', 'Cancelled')
        ], string='Status', readonly=True, index=True, copy=False, default='draft', track_visibility='onchange')

class AccountInvoice(models.Model):
    _inherit = 'account.invoice'
 
class PurchaseRequisitionLine(models.Model):
    _inherit='purchase.requisition.line'

    donation_product_id =fields.Many2one("donation.donation")
    product_lines =fields.Many2one("donation.donation")
    schedule_date = fields.Date(string='Scheduled Date',default=fields.Date.today())
    
class Donation(models.Model):
    _name = 'donation.donation'
    _rec_name = 'donor'

    # name= fields.Char(string="",default=" ")
    donor = fields.Many2one('res.partner')
    purchase_order_id = fields.Integer(string="Purchase Order ID")
    # purchase_order = fields.Many2one(string="Purchase Order", domain="[('unpacked_state',  '!=', 'Donation Item Unpacked.)]")
    purchase_order = fields.Many2many('purchase.order')
    unpacked_state = fields.Char(string="Donation Item Unpacked")
    is_a_unnkown_item = fields.Boolean(string  = "Unknown Item" , widget="radio",default=True)
    donation_type = fields.Many2one('donation.category')
    donation_date = fields.Date(string="Donation Date",default=fields.Date.today())
    additional_notes = fields.Text(string="Additional Notes")
    donation_description = fields.Char(string="Donation Description")
    line_ids = fields.One2many('purchase.requisition.line',"donation_product_id",string="Line Ids")
    product_lines = fields.One2many('purchase.requisition.line',"product_lines", string='Product Lines')
    donation_state = fields.Selection([
            ('draft', 'Draft'),
            ('recieved', 'Recieved'),
            ('unpack', 'Unpacked'),
            ('move_to_inventory', 'Move to Inventory'),
            ],default='draft')

    @api.one
    def create_donation_order(self):
        """if the donation product is known products then this button will be shown in the donation header"""
        pass


    #This function is triggered when the user clicks on the button 'Set to concept'
    @api.one
    def draft_progressbar(self):
        self.write({
            'donation_state': 'draft',
        })
     
    #This function is triggered when the user clicks on the button 'Set to started'
    @api.one
    def received_progressbar(self):
        self.write({
        'donation_state': 'recieved',
        })
     
    #This function is triggered when the user clicks on the button 'In progress'
    @api.one
    def unpack_progressbar(self):
        self.write({
        'donation_state': 'unpack','unpacked_state' : 'Donation Item Unpacked.'
        })
        res = self.create_purchase_order()
        self.purchase_order = [(6, 0, [res.id,])]
    
    #This function is triggered when the user clicks on the button 'Done'
    @api.one
    def move_to_inventory_progressbar(self):
        self.write({
        'donation_state': 'move_to_inventory',
        })
        # import pdb;pdb.set_trace()
        self.purchase_order.button_confirm()

    @api.multi
    def create_purchase_order(self):
        """
        This function creates a purchase order when unpack button is clicked.
        If Po is created for unknown item then a blank PO with no product line is created. And if PO is created for known products then PO with product line is created in the draft state.
        """
        now = datetime.datetime.now()
        date_now = now.strftime("%d-%m-%Y")
        
#        import pdb; pdb.set_trace()
        if self.is_a_unnkown_item:
            if not self.product_lines:
                raise Warning("Please add Products in Box Items to unpack.")
            elif self.product_lines:
                purchase_line_ids_list = []
                for lines in self.product_lines:
                    
                    values = {
                            'product_id': lines.product_id.id,
                            'name' : lines.product_id.name,
                            'date_planned' : lines.schedule_date,
                            'product_qty' : lines.product_qty , 
                            'price_unit' : lines.price_unit,
                            'product_uom':lines.product_id.uom_id.id,
                            }
                    purchase_line_ids_list.append([0, 0, values])

                vals ={ 'partner_id':self.donor.id,'order_date':date_now,'date_planned':self.donation_date, 'order_line':purchase_line_ids_list}
                po = self.env['purchase.order'].create(vals)

        else:
            purchase_line_ids_list = []
            for lines in self.line_ids:
                values = {
                'product_id': lines.product_id.id,
                'name' : lines.product_id.name,
                'date_planned' : lines.schedule_date,
                'product_qty' : lines.product_qty , 
                'price_unit' : lines.price_unit,
                'product_uom':lines.product_id.uom_id.id,
                }

                purchase_line_ids_list.append([0, 0, values])

            vals ={ 'partner_id':self.donor.id,'order_date':date_now,'date_planned':self.donation_date, 'order_line':purchase_line_ids_list}

            po = self.env['purchase.order'].create(vals)

        # self.purchase_order_id = po.id
        return po


