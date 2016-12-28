# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Generate Barcodes for Packaging',
    'summary': 'Generate Barcodes for Product Packaging',
    'version': '10.0.1.0.0',
    'category': 'Tools',
    'author': 'LasLabs, '
              'Odoo Community Association (OCA)',
    'website': 'https://www.odoo-community.org',
    'license': 'AGPL-3',
    'depends': [
        'barcodes_generator_abstract',
        'product',
    ],
    'data': [
        'views/product_packaging.xml',
    ],
    'demo': [
        'demo/ir_sequence.xml',
        'demo/barcode_rule.xml',
        'demo/res_partner.xml',
        'demo/function.xml',
    ],
}
