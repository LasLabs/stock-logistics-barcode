# -*- coding: utf-8 -*-
# Copyright 2016-2017 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Barcodes - Verhoeff",
    "summary": "It provides a Verhoeff barcode nomenclature.",
    "version": "10.0.1.0.0",
    "author": "LasLabs, "
              "Odoo Community Association (OCA)",
    "website": "https://laslabs.com/",
    "license": "LGPL-3",
    "category": "Extra Tools",
    "depends": [
        'barcodes',
    ],
    "data": [
        'views/assets.xml',
    ],
    'test': [
        'static/tests/js/barcode_parser.js',
    ],
    'installable': True,
}
