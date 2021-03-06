# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Website Part 1',
    'version' : '1.0',
    'summary': 'Sample Website',
    'author': 'Odoo.',
    'sequence': 30,
    'description': """
Sample Website
====================
For Clinic Information Maintenance
    """,
    'category': 'website',
    'website': 'http://newwaveoffices.com/',
    'depends': [
        'website',
    ],
    'data': [
        'static/add_css.xml',       
        'data/website_menu.xml',
        'views/inquiries.xml',
        'views/website_templates.xml',
        'views/subscribers.xml',
        'views/menu.xml',
    ],
    #'demo': [
    #    'views/fpt_menus_ept.xml',
    #],
    #'qweb': [
    #    "static/src/xml/account_reconciliation.xml",
    #    "static/src/xml/account_payment.xml",
    #    "static/src/xml/account_report_backend.xml",
    #],
    'installable': True,
    'application': False,
    'auto_install': False,
}