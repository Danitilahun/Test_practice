class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self):
        if self.quantity<0:
            raise ValueError()
        return self.price * self.quantity



import unittest

class TestProduct(unittest.TestCase):
    def setUp(self):
        self.product = Product("Laptop", 999.99, 5)

    def test_attributes(self):
        self.assertEqual(self.product.name, "Laptop")
        self.assertEqual(self.product.price, 999.99)
        self.assertEqual(self.product.quantity, 5)

    def test_total_price(self):
        self.assertEqual(self.product.total_price(), 999.99 * 5)
    def test_total_price_zero_quantity(self):
        # Test total price when quantity is zero
        zero_quantity_product = Product("Mouse", 19.99, 0)
        self.assertEqual(zero_quantity_product.total_price(), 0)


    def test_total_price_negative_quantity(self):
        # Test total price when quantity is negative
        negative_quantity_product = Product("Headphones", 49.99, -1)
        with self.assertRaises(ValueError):
            negative_quantity_product.total_price()

if __name__ == '__main__':
    unittest.main()