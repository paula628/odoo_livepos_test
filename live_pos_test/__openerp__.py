# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Live POS Test',
    'version': '1.1',
    'author': 'PKT',
    'category': 'Test',
    'sequence': 21,
    'website': ' ',
    'summary': ' ',
    'description': """


    """,
    'author': 'PKT',
    'website': 'https://www.odoo.com/page/employees',
    'depends': ['base_setup'],
    'data': [
        'live_pos_test_view.xml',
        'security/live_pos_test_security.xml',
        'security/ir.model.access.csv',
    ],

    'installable': True,
    'application': True,
    'auto_install': False,
    'qweb': [ 'static/src/xml/suggestions.xml' ],
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
