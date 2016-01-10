from openerp import api
from openerp.osv import fields, osv


class users(osv.Model):
    """ Update of res.users class
        - if adding groups to an user, check if base.group_user is in it
        (member of 'Employee'), create an employee form linked to it.
    """
    _name = 'users'

    def _compute_total_bal(self, cr, uid, ids, fields, vals, context=None):       
        result = {}
        bal = 0
        for user_obj in self.browse(cr, uid, ids):
            for apt in user_obj.apartment_ids:
                 bal += apt.balance
        result[user_obj.id] = bal        
        print '--', result        
        return result

    def _compute_total_sq_meters(self, cr, uid, ids, fields, vals, context=None):        
        result={}
        total = 0
        for user_obj in self.browse(cr, uid, ids):
            for apt in user_obj.apartment_ids:
                 total += apt.sq_meters
        result[user_obj.id] = total        
        print '--', result
        return result    

    _columns = {
        'lastname': fields.char('Lastname'),
        'name': fields.char('Name'),
        'email': fields.char('Email'),
        'apartment_ids': fields.one2many('apartments', 'user_id', "Apartments"),
        'total_balance': fields.function(_compute_total_bal, type="float", store=False, string="Total Balance"),
        'total_sq_meters': fields.function(_compute_total_sq_meters, type="float", store=False, string="Total Square Meters"),
    }


users()

class apartments(osv.Model):

    _name = 'apartments'
    _rec_name = 'address'

    _columns = {
        'address': fields.char("Address"),        
        'sq_meters': fields.float("Square Meters"),
        'balance': fields.float("Balance"),
        'user_id': fields.many2one('users', "User ID"),
    }
apartments()
