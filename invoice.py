from openerp.osv import osv, fields
from openerp.tools.translate import _

class account_invoice(osv.Model):

    _name = "account.invoice"
    _inherit = 'account.invoice'
    _description = "Invoice extensions"


    def _function_attach_get(self, cr, uid, ids, field, arg, context=None):
        res = dict.fromkeys(ids, False)
        attach_db = self.pool.get('ir.attachment')
        for document in self.browse(cr, uid, ids, context=context):
            res[document.id] = attach_db.search(cr, uid, [['res_model', '=', 'account.invoice'], ['res_id', '=', document.id]], count=True)
        return res

    _columns = {
        'no_of_attachments': fields.function(_function_attach_get, type='integer', string='# of Attachments'),
    }





