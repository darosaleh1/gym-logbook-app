from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework import status


class RegisterViewTest(APITestCase):
        def test_valid_registration(self):
                data = {
                        'username': 'testuser',
                        'email': 'test@example.com',
                        'password': 'testpass123',
                        'confirm_password': 'testpass123'
                }
                response = self.client.post('/api/auth/register/', data)
                self.assertEqual(response.status_code, status.HTTP_201_CREATED)
                self.assertTrue(User.objects.filter(email='test@example.com').exists())
                
        def test_empty_username(self):
                data = {
                        'username': '',
                        'email': 'test@example.com',
                        'password': 'testpass123',
                        'confirm_password': 'testpass123'
                }
                response = self.client.post('/api/auth/register/', data)
                self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
                self.assertFalse(User.objects.filter(email="test@example.com").exists())


class EmailTokenObtainPairViewTest(APITestCase):
        def setUp(self):
                self.user = User.objects.create_user(
                         username='testuser',
                        email='test@example.com',
                        password='testpass123'
                )
        
        def test_valid_login(self):
                data = {
                        'email': 'test@example.com',
                        'password': 'testpass123'
                }
                response = self.client.post('/api/auth/token/', data)
                self.assertEqual(response.status_code, status.HTTP_200_OK)
                self.assertIn('access', response.data)
                self.assertIn('refresh', response.data)

        def test_invalid_credentials(self):
            data = {
                'email': 'test@example.com',
                'password': 'wrongpass'
            }
            response = self.client.post('/api/auth/token/', data)
            self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


                