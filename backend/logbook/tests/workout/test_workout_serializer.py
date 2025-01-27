from django.test import TestCase
from logbook.models import Exercise, Workout, WorkoutExercise
from django.contrib.auth.models import User
from logbook.serializers import WorkoutExerciseSerializer, WorkoutSerializer


class WorkoutSerializerTest(TestCase):

    def setUp(self):
        # test user
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )

        self.exercise = Exercise.objects.create(
            name="test exercise",
            description="This is a test exercise",
            rest_period="30",
            is_custom=True,
            created_by=self.user  #
        )

        #  workout
        self.workout = Workout.objects.create(
            name="Test Workout",
            description="Test workout description",
            created_by=self.user
        )

    def test_valid_workout_serializer(self):
        data = {
            "workout": self.workout.id,
            "exercise": self.exercise.id,
            "order": 1,
            "sets": 4,
            "reps": 12
        }
        
        serializer = WorkoutExerciseSerializer(data=data)
        if not serializer.is_valid():
            print(serializer.errors)
        self.assertTrue(serializer.is_valid())