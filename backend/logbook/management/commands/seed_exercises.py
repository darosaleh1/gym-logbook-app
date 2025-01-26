from django.core.management.base import BaseCommand
from logbook.models import Exercise
from django.contrib.auth.models import User
from logbook.data.default_exercises import DEFAULT_EXERCISES

class Command(BaseCommand):
    help = 'Seed database with default exercises'

    def handle(self, *args, **kwargs):
        # Create a system user if it doesn't exist
        system_user, created = User.objects.get_or_create(
            username='system',
            defaults={
                'is_staff': True,
                'is_superuser': False,
                'email': 'system@example.com'
            }
        )

        exercises_created = 0
        exercises_updated = 0

        for exercise_data in DEFAULT_EXERCISES:
            exercise, created = Exercise.objects.update_or_create(
                name=exercise_data['name'],
                defaults={
                    'description': exercise_data['description'],
                    'rest_period': exercise_data['rest_period'],
                    'is_custom': False,
                    'created_by': system_user
                }
            )

            if created:
                exercises_created += 1
            else:
                exercises_updated += 1

        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully added {exercises_created} exercises and updated {exercises_updated} exercises'
            )
        )