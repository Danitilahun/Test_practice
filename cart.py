import unittest


class Product:
    def __init__(self, name, price, quantity):
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_price(self):
        return self.price * self.quantity


class ShoppingCart:
    def __init__(self):
        self.cart = []

    def add_product(self, product):
        self.cart.append(product)

    def get_cart_total(self):
        total = 0
        for product in self.cart:
            total += product.calculate_price()
        return total


class TestShoppingCart(unittest.TestCase):
    def test_empty_cart(self):
        # Create an empty shopping cart
        cart = ShoppingCart()

        # Check if the total price in an empty cart is 0
        self.assertEqual(cart.get_cart_total(), 0)

    def test_cart_with_products(self):
        # Create a shopping cart with products
        cart = ShoppingCart()
        product1 = Product("Laptop", 20.0, 1)
        product2 = Product("Phone", 10.0, 2)
        cart.add_product(product1)
        cart.add_product(product2)
        
        # Check if the total price in the cart matches the expected total
        self.assertEqual(cart.get_cart_total(), 40.0)

if __name__ == '__main__':
    unittest.main()