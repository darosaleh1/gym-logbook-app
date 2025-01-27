from django.test import TestCase
from unittest.mock import Mock
from logbook.models import Exercise, Workout, WorkoutExercise
from django.contrib.auth.models import User
from logbook.serializers import WorkoutExerciseSerializer, WorkoutSerializer

class WorkoutTestSerializer(TestCase):
    def setUp(self):
        # Create test user
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )

        # Create test exercise
        self.exercise = Exercise.objects.create(
            name="test exercise",
            description="This is a test exercise",
            rest_period="30",
            is_custom=True,
            created_by=self.user  
        )

    
    def test_create_workout_with_exercises(self):
        valid_data = {
            "name": "Test Workout",
            "description": "Test workout description",
            "exercises": [{
                "exercise": self.exercise.id,
                "order": 1,
                "sets": 3,
                "reps": 10
            }]
        }
        
        mock_request = Mock()
        mock_request.user = self.user
        
        serializer = WorkoutSerializer(data=valid_data, context={'request': mock_request})
        self.assertTrue(serializer.is_valid())
        workout = serializer.save()

        # Verify workout was created correctly
        self.assertEqual(workout.name, "Test Workout")
        self.assertEqual(workout.description, "Test workout description")
        self.assertEqual(workout.created_by, self.user)

        # Verify exercise was added correctly
        self.assertEqual(workout.workoutexercise_set.count(), 1)
        workout_exercise = workout.workoutexercise_set.first()
        self.assertEqual(workout_exercise.exercise, self.exercise)
        self.assertEqual(workout_exercise.order, 1)
        self.assertEqual(workout_exercise.sets, 3)
        self.assertEqual(workout_exercise.reps, 10)


    
    
