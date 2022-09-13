from django.test import TestCase
from django.urls import reverse
from .models import Profile
from django.contrib.auth.models import User


class TestProfile(TestCase):
    def test_fx_index(self):
        url = reverse('profiles_index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<title>Profiles</title>', response.content)
        # assert response.status_code == 200
        # assert b"<title>Lettings</title>" in response.content

    def setUp(self):
        self.user = User.objects.create(
            username="Appryll",
            first_name="Natalia",
            last_name="FERNANDEZ",
            email="contact@contact.com"
        )
        self.profile = Profile.objects.create(
            favorite_city="Paris",
            user=self.user)

    def test_fx_profile(self):
        url = reverse('profile', args=["Appryll"])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<title>Appryll</title>', response.content)
        self.assertIn(b'<p>Natalia</p>', response.content)
        self.assertIn(b'<h5>First name:</h5>', response.content)
        self.assertIn(b'<h5>Last name:</h5>', response.content)
        self.assertIn(b'<p>FERNANDEZ</p>', response.content)
        self.assertIn(b'<h5>Email:</h5>', response.content)
        self.assertIn(b'<p>contact@contact.com</p>', response.content)
        self.assertIn(b'<h5>Favorite city:</h5>', response.content)
        self.assertIn(b'<p>Paris</p>', response.content)
        # assert response.status_code == 200
        # assert b"<title>Test Lettings</title>" in response.content
