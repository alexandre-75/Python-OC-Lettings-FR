from django.test import TestCase
from django.urls import reverse


class IndexViewTest(TestCase):
    def test_index_view(self):
        response = self.client.get(reverse('index'))
        assert response.status_code == 200
        assert b"<title>Holiday Homes</title>" in response.content
