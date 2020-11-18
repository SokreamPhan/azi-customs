# -*- coding: utf-8 -*-
from openerp import fields, models, api

class purchase_order(models.Model):
    _inherit = "purchase.order"
    
    rfq_name = fields.Char('Rfq Reference', required=True, select=True, copy=False,
                            help="Unique number of the purchase order, "
                                 "computed automatically when the purchase order is created.")
    interchanging_rfq_sequence = fields.Char('Sequence')
    interchanging_po_sequence = fields.Char('Sequence')
                
    @api.model
    def create(self, vals):
        if vals.get('name','New') == 'New':
            name = self.env['ir.sequence'].next_by_code('purchase.order.quot') or 'New'
            vals['rfq_name'] = vals['name'] = name
            
        return super(purchase_order, self).create(vals)
        
    def wkf_confirm_order(self, cr, uid, ids, context=None):
        res =  super(purchase_order, self).wkf_confirm_order(cr, uid, ids, context=context)
        this = self.browse(cr, uid, ids)
        for order in this:
            if order.interchanging_rfq_sequence:
                order.write({'name': order.interchanging_po_sequence})
            else:
                new_name = self.pool.get('ir.sequence').next_by_code(cr,uid,'purchase.order') or '/'
                order.write({'interchanging_rfq_sequence':order.name})
                order.write({'name': new_name})
            order.picking_ids.write({'origin': order.interchanging_po_sequence})
            if order.picking_ids:
                for pick in self.picking_ids:
                    pick.move_lines.write({'origin': order.interchanging_po_sequence}) 
        return res
    
    def action_cancel_draft(self, cr, uid, ids, context=None):
        res = super(purchase_order, self).action_cancel_draft(cr, uid, ids, context=context)
        this = self.browse(cr, uid, ids)[0]
        if this.interchanging_rfq_sequence:
            this.write({'interchanging_po_sequence':this.name})
            this.write({'name':this.interchanging_rfq_sequence})
        return res