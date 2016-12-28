# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo.tests.common import TransactionCase


class TestBarcodeGenerator(TransactionCase):

    def setUp(self):
        super(Tests, self).setUp()
        self.Model = self.env['product.packaging']
        self.record = self.partner_obj.browse(
            self.ref(
                'barcodes_generator_product_packaging'
                '.product_packaging_barcode'
            ),
        )
        self.record.generate_barcode()

    def test_generate_base(self):
        """ It should generate the correct base for the barcode. """
        self.assertEqual(
            self.record.barcode_base, 1,
        )

    def test_generate_sequence(self):
        """ It should generate the correct sequence for the barcode. """
        self.assertEqual(
            self.record.barcode,
            "1230000000013",
        )
