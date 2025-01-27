from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from logbook.models import Exercise
from rest_framework import status


class ExerciseViewTest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        
        self.client.force_authenticate(user=self.user)

    def test_get_exercise_list(self):
        response = self.client.get('/api/exercises/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unauthenticated_request(self):
        self.client.force_authenticate(user=None)
        response = self.client.get('/api/exercises/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


    def test_post_new_exercise(self):
        valid_data = {
            "name": "test exercise",
            "description" : "This is a test exercise",
            "rest_period": "30",
            "is_custom": "True"
        }
         
        response = self.client.post('/api/exercises/',valid_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Exercise.objects.filter(name='test exercise').exists())

    def test_post_duplicate_exercise(self):
        valid_data = {
            "name": "test exercise",
            "description" : "This is a test exercise",
            "rest_period": "30",
            "is_custom": "True"
        }
        self.client.post('/api/exercises/',valid_data)
        response = self.client.post('/api/exercises/',valid_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

