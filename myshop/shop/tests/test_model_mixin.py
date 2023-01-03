from django.test import TestCase
from django.urls import reverse
from shop.models import Category, Product


class ModelMixin(TestCase):
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
