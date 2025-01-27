from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Exercise, Workout, WorkoutExercise



class WorkoutExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutExercise
        fields = ['id', 'workout', 'exercise','order', 'sets', 'reps']
        read_only_fields = ['workout']

class WorkoutSerializer(serializers.ModelSerializer):
    exercises = WorkoutExerciseSerializer(source='workoutexercise_set', many=True)

    class Meta:
        model = Workout
        fields = ['id','name','description','exercises']
        read_only_fields = ['created_by']
    
    def create(self, validated_data):
        exercises_data = validated_data.pop('workoutexercise_set')
        workout = Workout.objects.create(
            created_by=self.context['request'].user,
            **validated_data
        )
        for exercise_data in exercises_data:
            WorkoutExercise.objects.create(workout=workout, **exercise_data)
        return workout
    
    def update(self,instance,validated_data):
        exercises_data = validated_data.pop('workoutexercise_set')
        instance.workoutexercise_set.all().delete()
        for exercise_data in exercises_data:
            WorkoutExercise.objects.create(workout=instance, **exercise_data)

        return super().update(instance,validated_data)
    


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ('id','name','description','is_custom','created_by','rest_period')
        read_only_fields = ['created_by']

    def create(self, validated_data):
        validated_data['created_by'] = self.context['request'].user
        return super().create(validated_data)
    
    def validate(self,data):

        if Exercise.objects.filter(
            created_by=self.context['request'].user,
            name__iexact=data['name']
        ).exists():
            raise serializers.ValidationError({"name": "You already have an exercise with this name"})
        return data
    

class UserSerializer(serializers.ModelSerializer):
    email = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True)
    confirm_password=  serializers.CharField(write_only=True, required=True)


    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'confirm_password')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    
    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords do not match.")
        return data
    
    def validate_email(self,value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with this email already exists.")
        return value

    
    def create(self, validated_data):
        validated_data.pop('confirm_password')
        return User.objects.create_user(**validated_data)