from django.test import TestCase
from django.test import SimpleTestCase


class TestDeliveryApp(SimpleTestCase):

    def test_index(self):
        response = self.client.get('categories/')
        self.assertEqual(response.status_code, 200)

