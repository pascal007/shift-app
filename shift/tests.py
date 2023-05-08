from unittest import TestCase

from django.utils import timezone

from rest_framework.test import APIClient
from rest_framework.test import force_authenticate



from shift.models import Shift
from user.models import User


class TestShift(TestCase):
    def setUp(self):
        self.client = APIClient()
        payload = {
            'username': 'test_worker',
            'password': 'test_password'
        }
        response = self.client.post('/api/user/register', data=payload, format='json')
        # test user creation
        self.assertEqual(response.status_code, 201)
        response = self.client.post('/api/user/login', data=payload, format='json')
        # test user login
        self.assertEqual(response.status_code, 200)
        self.access_token = response.json()['data']['access']

    def tearDown(self):
        user = User.objects.filter(username='test_worker').first()
        Shift.objects.filter(worker=user).delete()
        user.delete()

    def test_authenticated_shifts(self):
        today = timezone.now().date()
        user = User.objects.get(username='test_worker')
        self.client.force_authenticate(user=user, token=self.access_token)
        response = self.client.get('/api/shift/')
        self.assertEqual(response.status_code, 200)
        response = self.client.post('/api/shift/', format='json', data={'start_hour': 0, 'date': today})
        self.assertEqual(response.status_code, 201)
        response = self.client.post('/api/shift/', format='json', data={'start_hour': 0, 'date': today})
        # fail to create duplicate same day record
        self.assertEqual(response.status_code, 400)
        # fail to create invalid start hour
        response = self.client.post('/api/shift/', format='json', data={'start_hour': 0, 'date': today})
        self.assertEqual(response.status_code, 400)

    def test_unauthenticated_shift(self):
        response = self.client.get('/api/shift/')
        self.assertEqual(response.status_code, 401)




