# -*- coding: utf-8 -*-
{
    'name': "WEDDING ORGANIZER",

    'summary': """
        Custom Module Odoo 14""",

    'description': """
        Untuk pemesanan kebutuhan Wedding
    """,

    'author': "Ahmad Yulian Dinata",
    'website': "https://www.linkedin.com/in/ahmaddyd/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Productivity',
    'version': '0.1',
    'application': True,

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/panggung_views.xml',
        'views/pelaminan_views.xml',
        'views/kursi_pengantin_views.xml',
        'views/kursi_tamu_views.xml',
        'views/order_views.xml',
        'views/res_partner_views.xml',
        'views/pegawai_views.xml',
        'views/pelanggan_views.xml',
        'views/pengembalian_views.xml',
        'views/akunting_views.xml',
        'report/report.xml',
        'report/wo_order_report.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
