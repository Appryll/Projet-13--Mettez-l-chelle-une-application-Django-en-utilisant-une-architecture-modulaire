from django.test import TestCase
from django.urls import reverse
from .models import Address, Letting


class TestLettings(TestCase):
    def test_fx_index(self):
        url = reverse('lettings_index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<title>Lettings</title>', response.content)
        # assert response.status_code == 200
        # assert b"<title>Lettings</title>" in response.content

    def setUp(self):
        self.address = Address.objects.create(
            number=1,
            street="Rue Pasteur",
            city="Paris",
            state="",
            zip_code=75011,
            country_iso_code="FRA"
        )
        self.letting = Letting.objects.create(
            title="Test Lettings",
            address=self.address
            )

    def test_fx_lettings(self):
        url = reverse('letting', args=[1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<title>Test Lettings</title>', response.content)
        # assert response.status_code == 200
        # assert b"<title>Test Lettings</title>" in response.content
