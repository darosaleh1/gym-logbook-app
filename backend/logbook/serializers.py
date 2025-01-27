from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Exercise, Workout, WorkoutExercise, WorkoutPlanDay, WorkoutPlan


from rest_framework import serializers
from .models import WorkoutLog, ExerciseLog

class ExerciseLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseLog
        fields = ['id', 'exercise', 'set_number', 'weight', 'reps', 'completed_at']
        read_only_fields = ['workout_log', 'completed_at']

class WorkoutLogSerializer(serializers.ModelSerializer):
    exercise_logs = ExerciseLogSerializer(many=True, read_only=True)

    class Meta:
        model = WorkoutLog
        fields = ['id', 'workout', 'workout_plan', 'date', 'completed', 'exercise_logs']
        read_only_fields = ['user']

class WorkoutPlanDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutPlanDay
        fields = ['id', 'day_of_week', 'workout', 'is_rest_day']
        read_only_fields = ['workout_plan']

class WorkoutPlanSerializer(serializers.ModelSerializer):
    schedule = WorkoutPlanDaySerializer(source='workoutplanday_set', many=True, read_only=True)

    class Meta:
        model = WorkoutPlan
        fields = ['id', 'name', 'start_date', 'weeks_duration', 'is_active', 'schedule']
        read_only_fields = ['created_by']
    
    def create(self, validated_data):
        workout_plan = WorkoutPlan.objects.create(
            created_by = self.context['request'].user,
            **validated_data
        )

        for day in range(1,8):
            WorkoutPlanDay.objects.create(
                workout_plan=workout_plan,
                day_of_week=day,
                is_rest_day=True
            )
        return workout_plan


class WorkoutExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutExercise
        fields = ['id','exercise', 'order', 'sets', 'reps']

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