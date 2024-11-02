from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse


class JWTTokenTestCase(TestCase):
    def setUp(self):
        self.pair_url = reverse('create-token-pair')
        self.access_url = reverse('create-access-token')
        self.username = 'test'
        self.password = 'test'
        self.user = User.objects.create_user(username=self.username, password=self.password)

    def test_token_pair_creation(self):
        '''
        Test that a token pair can be created from a set of credentials.
        '''
        data = {
            'username': self.username,
            'password': self.password,
        }
        response = self.client.post(self.pair_url, data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('access', response.json())
        self.assertIn('refresh', response.json())

    def test_invalid_credentials(self):
        '''
        Test that a 401 response is returned when invalid credentials are provided.
        '''
        data = {
            'username': self.username,
            'password': 'invalid',
        }
        response = self.client.post(self.pair_url, data)
        self.assertEqual(response.status_code, 401)

    def test_access_token_creation(self):
        '''
        Test that an access token can be created from a refresh token.
        '''
        data = {
            'username': self.username,
            'password': self.password,
        }
        response = self.client.post(self.pair_url, data)
        generated_refresh_token = response.json()['refresh']
        data = {
            'refresh': generated_refresh_token,
        }
        response = self.client.post(self.access_url, data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('access', response.json())
        self.assertNotIn('refresh', response.json())

    def test_invalid_refresh_token(self):
        '''
        Test that a 401 response is returned when an invalid refresh token is provided.
        '''
        data = {
            'refresh': 'invalid',
        }
        response = self.client.post(self.access_url, data)
        self.assertEqual(response.status_code, 401)
