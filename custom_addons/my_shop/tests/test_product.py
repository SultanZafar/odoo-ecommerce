# -*- coding: utf-8 -*-
from odoo.tests.common import TransactionCase

class TestFeaturedProduct(TransactionCase):

    def test_featured_field_exists(self):
        """Test: is_featured field kaam kar raha hai"""
        product = self.env['product.template'].create({
            'name': 'Test Laptop',
            'list_price': 50000,
            'is_featured': True,
        })
        # Check karo field True hai
        self.assertTrue(product.is_featured)
        print("✅ TEST PASS: is_featured field kaam kar raha hai!")

    def test_unfeatured_product(self):
        """Test: featured nahi hai to False hoga"""
        product = self.env['product.template'].create({
            'name': 'Normal Product',
            'list_price': 1000,
            'is_featured': False,
        })
        self.assertFalse(product.is_featured)
        print("✅ TEST PASS: Normal product featured nahi hai!")