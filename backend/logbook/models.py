from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator


# Create your models here.





class Exercise(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    is_custom = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    rest_period = models.IntegerField(
        help_text="Rest period in seconds",
        validators=[MinValueValidator(0)]
        )
    
    class Meta:
        unique_together = ['name', 'created_by']

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    exercises = models.ManyToManyField(Exercise, through='WorkoutExercise')

class WorkoutPlan(models.Model):
    name = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField()
    weeks_duration = models.IntegerField()
    is_active = models.BooleanField(default=True)

class WorkoutPlanDay(models.Model):
    DAY_CHOICES = [
        (1, 'Day 1'),
        (2, 'Day 2'),
        (3, 'Day 3'),
        (4, 'Day 4'),
        (5, 'Day 5'),
        (6, 'Day 6'),
        (7, 'Day 7'),
    ]
    workout_plan = models.ForeignKey(WorkoutPlan, on_delete=models.CASCADE)
    day_of_week = models.IntegerField(choices=DAY_CHOICES)
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, null=True, blank=True)
    is_rest_day = models.BooleanField(default=False)


class WorkoutExercise(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    order = models.IntegerField(validators=[MinValueValidator(1)])
    sets = models.IntegerField(validators=[MinValueValidator(1)])
    reps = models.IntegerField(validators=[MinValueValidator(1)])

    class Meta:
        ordering = ['order']

class WorkoutLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    workout_plan = models.ForeignKey(WorkoutPlan, on_delete=models.CASCADE)
    date = models.DateField()
    completed = models.BooleanField(default=False)

class ExerciseLog(models.Model):
    workout_log = models.ForeignKey(WorkoutLog, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    set_number = models.IntegerField()
    weight = models.DecimalField(max_digits=6, decimal_places=2)
    reps = models.IntegerField()
    completed_at = models.DateTimeField(auto_now_add=True)