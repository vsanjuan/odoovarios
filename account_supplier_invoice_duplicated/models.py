# -*- coding: utf-8 -*-

from openerp import models, fields, api
from openerp.exceptions import except_orm, Warning, RedirectWarning

class Duplicate_Invoice(models.Model):
    _inherit = 'account.invoice' 
    
    @api.multi
    def check_invoice_duplicate(self, reference, supplier_id):
        if not reference:
            return
        msg = 'La referencia de factura ' + reference + ' ya ha sido creada!' 
        numero = self.search_count([('type','=','in_invoice'),('reference','=',reference),('partner_id','=',supplier_id)])
        if numero > 0:
            raise Warning(msg)
        return 
        
# class dmpyme(models.Model):
#     _name = 'dmpyme.dmpyme'

#     name = fields.Char()