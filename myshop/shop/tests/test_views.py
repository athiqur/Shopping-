from django.test import TestCase
from django.urls import reverse
from shop.tests.test_model_mixin import ModelMixin


class TestProductList(ModelMixin, TestCase):
    def test_product_list_view_returns_correct_context_when_the_category_slug_is_valid(
        self,
    ):
        response = self.client.get(
            reverse("shop:product_list_by_category", args=[self.category])
        )
        self.assertEquals(response.context["products"][0], self.product)

    def test_product_list_view_returns_empty_context_when_the_category_slug_is_invalid(
        self,
    ):
        response = self.client.get(
            reverse("shop:product_list_by_category", args=["invalid-slug"])
        )
        self.assertIsNone(response.context["None"])
