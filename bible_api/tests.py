from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
import json

class BibleAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_health_check(self):
        response = self.client.get('/api/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['status'], 'online')

    def test_guidance_endpoint(self):
        # Test valid request
        data = {'question': 'How to find peace?'}
        response = self.client.post('/api/guidance/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.json()['success'])
        self.assertIn('guidance', response.json())

        # Test empty question
        data = {'question': ''}
        response = self.client.post('/api/guidance/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # Test missing question
        data = {}
        response = self.client.post('/api/guidance/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
