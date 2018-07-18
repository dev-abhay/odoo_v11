# -*- coding: utf-8 -*-
{
    'name': "donation",

    'summary': """
    Module to manage donation products recieved from different sources.
        """,

    'description': """
    Module to manage donation products recieved from different sources.
    """,

    'author': "Demo Company",
    'website': "http://www.demo.com",

  
    'category': 'Uncategorized',
    'version': '1.0',

    'depends': ['base', 'contacts','sale','purchase_requisition','account','product','purchase',],

    'data': [
         'security/access_rights_group.xml',
#         'security/ir.model.access.csv',
        'data/data.xml',
        'views/views.xml',
        'views/donation_category.xml',
        'views/templates.xml',
        'views/res_partner_view.xml',
        'views/custom_purchase_view.xml',
        'views/product_view.xml',
        'views/purchase_view.xml',
        'views/sale_auction_view.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
}