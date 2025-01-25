from django.test import TestCase
from django.contrib.auth.models import User
from logbook.serializers import UserSerializer

class UserSerializerTest(TestCase):

    def test_valid_user_serializer(self):
        valid_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'testpass123',
            'confirm_password': 'testpass123'
        }
        serializer = UserSerializer(data=valid_data)
        self.assertTrue(serializer.is_valid())

    
    def test_passwords_not_matching(self):
        valid_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'testpass123',
            'confirm_password': 'testpass1234'
        }
        serializer = UserSerializer(data=valid_data)
        self.assertFalse(serializer.is_valid())
    
    def test_duplicate_email(self):
        User.objects.create_user(
            username='existing',
            email='test@example.com',
            password='testpass123'
        )

        data = {
           'username':'existing',
            'email': 'test@example.com',
            'password': 'testpass123',
            'confirm_password': 'testpass123'
        }

        serializer = UserSerializer(data=data)
        self.assertFalse(serializer.is_valid())
