from django.test import TestCase
from django.urls import reverse

from .models import Address, Letting


class LettingsTest(TestCase):

    def setUp(self):
        self.address = Address.objects.create(
            number=104,
            street="Avenue des Champs Elysées",
            city="Paris",
            state="IDF",
            zip_code=75008,
            country_iso_code="FRA"
        )
        self.letting = Letting.objects.create(title="TestP13", address=self.address)

    def test_lettings_index(self):
        response = self.client.get(reverse('lettings_index'))
        assert response.status_code == 200
        assert b"<title>Lettings</title>" in response.content

    def test_lettings(self):
        response = self.client.get(reverse('letting', args=[1]))
        assert response.status_code == 200
        assert b"<title>TestP13</title>" in response.content
