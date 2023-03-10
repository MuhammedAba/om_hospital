# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Hospital Management',
    'version' : '1.1.0',
    'category': 'Hospital',
    'summary': 'Hospital Management System',
    'sequence': -100,
    'description': """Hospital Management System""",
    'category': '',
    'depends': [],
    'data': [
        "security/ir.model.access.csv",
        'views/menu.xml',
        'views/patient_views.xml',
        'views/female_patient_view.xml',
    ],
    'demo': [],
    'author': 'Muhammed Aba',
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
