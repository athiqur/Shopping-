from django.test import TestCase
from shop.models import Category, Product
from django.test import RequestFactory
from cart.cart import Cart
from django.contrib.sessions.middleware import SessionMiddleware


class CartMixin(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            name="tea",
            slug="tea",
        )

        self.product = Product.objects.create(
            category=self.category,
            name="herbal-tea",
            slug="herbal-tea",
            price=200,
        )

    def create_session(self):
        request = RequestFactory().get("/")
        middleware = SessionMiddleware(request)
        middleware.process_request(request)
        self.cart = Cart(request)
        self.cart.add(self.product)
