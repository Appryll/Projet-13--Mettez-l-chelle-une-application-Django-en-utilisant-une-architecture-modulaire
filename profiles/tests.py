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
        self.assertIn(b'<p>First name: Natalia</p>', response.content)
        self.assertIn(b'<p>Last name: FERNANDEZ</p>', response.content)
        self.assertIn(b'<p>Email: contact@contact.com</p>', response.content)
        self.assertIn(b'<p>Favorite city: Paris</p>', response.content)
        # assert response.status_code == 200
        # assert b"<title>Test Lettings</title>" in response.content
