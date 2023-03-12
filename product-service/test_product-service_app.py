import unittest
from product import Product
import app

class TestProductService(unittest.TestCase):
    def setUp(self):
        self.products = [
            Product(1, 'Book', 'Textbook', 15.95),
            Product(2, 'Apple', 'Fuji', 0.50),
            Product(3, 'Chair', 'Child', 25.00)
        ]
    
    def test_get_products(self):
        products = app.get_products()
        self.assertEqual(self.products, products)