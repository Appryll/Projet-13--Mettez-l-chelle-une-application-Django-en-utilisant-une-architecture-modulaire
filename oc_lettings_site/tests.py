from django.test import TestCase
from django.urls import reverse


class TestHome(TestCase):
    def test_index_oc_lettings_site(self):
        url = reverse('index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<title>Holiday Homes</title>', response.content)
