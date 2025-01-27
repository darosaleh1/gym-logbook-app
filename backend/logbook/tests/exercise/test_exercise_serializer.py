from django.test import TestCase
from logbook.models import Exercise
from django.contrib.auth.models import User
from logbook.serializers import ExerciseSerializer

class ExerciseSerializerTest(TestCase):
    def setUp(self):
            self.user = User.objects.create_user(
                username='testuser',
                password='testpass'
            )



    def test_valid_exercise_serializer(self):
        
       
        valid_data = {
            "name": "test exercise",
            "description" : "This is a test exercise",
            "rest_period": "30",
            "is_custom": True
        }

        serializer = ExerciseSerializer(
            data=valid_data,
            context={'request': type('Request', (), {'user': self.user})()}
            )
        self.assertTrue(serializer.is_valid())
    
    def test_empty_name(self):
        
       
        invalid_data = {
            "name": "",
            "description" : "This is a test exercise",
            "rest_period": "-30",
            "is_custom": True
        }

        serializer = ExerciseSerializer(
            data=invalid_data,
            context={'request': type('Request', (), {'user': self.user})()}
            )
        self.assertFalse(serializer.is_valid())
    
    def test_negative_rest_period(self):
        
       
        invalid_data = {
            "name": "test exercise",
            "description" : "This is a test exercise",
            "rest_period": "-30",
            "is_custom": True
        }

        serializer = ExerciseSerializer(
            data=invalid_data,
            context={'request': type('Request', (), {'user': self.user})()}
            )
        self.assertFalse(serializer.is_valid())