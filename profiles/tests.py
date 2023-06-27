from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from .models import Profile


class ProfilesTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="username",
            password="password",
            email="user1@example.com"
        )
        self.profile = Profile.objects.create(user=self.user, favorite_city="Paris")

    def test_profiles_index(self):
        response = self.client.get(reverse('profiles_index'))
        assert response.status_code == 200
        assert b"<title>Profiles</title>" in response.content

    def test_profile(self):
        response = self.client.get(reverse('profile', args=["username"]))
        assert response.status_code == 200
        assert b"<title>username</title>" in response.content
