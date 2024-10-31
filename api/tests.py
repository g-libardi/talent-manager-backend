from django.test import TestCase
from django.urls import reverse


class TestPingView(TestCase):
    def test_ping_view_(self):
        """
        Expects a 200 response with a {'message': 'pong'} JSON response
        """
        response = self.client.get(reverse('ping'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'message': 'pong'})
