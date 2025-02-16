# Generated by Django 5.1.1 on 2025-01-27 21:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logbook', '0005_workoutplan_workoutplanday'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkoutLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('completed', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('workout', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='logbook.workout')),
                ('workout_plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='logbook.workoutplan')),
            ],
        ),
        migrations.CreateModel(
            name='ExerciseLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('set_number', models.IntegerField()),
                ('weight', models.DecimalField(decimal_places=2, max_digits=6)),
                ('reps', models.IntegerField()),
                ('completed_at', models.DateTimeField(auto_now_add=True)),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='logbook.exercise')),
                ('workout_log', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='logbook.workoutlog')),
            ],
        ),
    ]
