# -*- coding: utf-8 -*-
{
    'name': 'Fleet Management',
    'version': '18.0.1.0.0',
    'summary': 'Vehicle management associated with contacts',
    'description': """
Custom module for vehicle management in Odoo.
Allows registering vehicles associated with contacts,
including validations, security groups, and custom views.
    """,
    'author': 'Nery Sinay',
    'website': 'https://github.com/nsinay',
    'category': 'Fleet',
    'license': 'LGPL-3',
    'depends': [
        'base',
        'contacts',
    ],
    'data': [
        'security/security_groups.xml',
        'security/ir.model.access.csv',

        'wizard/vehicle_transfer_wizard_views.xml',

        'views/vehicle_views.xml',
        'views/res_partner_views.xml',
        'views/menu.xml',

        'report/vehicle_report.xml',

        
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}