from django.test import TestCase
from cart.tests.test_cart_mixin import CartMixin
from cart.cart import Cart


class TestCart(CartMixin, TestCase):
    def test_add_success_adding_item_inside_cart_with_session(self):
        self.cart.add(self.product)
        self.assertEqual(self.cart.__len__(), 2)

    def test_remove_success_removing_item_from_cart_with_session(self):
        self.cart.remove(self.product)
        self.assertEqual(self.cart.__len__(), 0)

    def test_get_total_price_returns_correct_total_price(self):
        self.assertEqual(self.cart.get_total_price(), self.product.price)
