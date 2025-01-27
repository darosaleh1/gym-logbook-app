from django.urls import path
from logbook.views.workout_exercise_log_views import WorkoutLogDetailView, WorkoutLogListView, ExerciseLogView, PreviousExerciseLogsView


urlpatterns = [
    path('workout-logs/', WorkoutLogListView.as_view(), name='workout-log-list'),
    path('workout-logs/<int:pk>/', WorkoutLogDetailView.as_view(), name='workout-log-detail'),
    path('workout-logs/<int:workout_log_id>/exercises/', ExerciseLogView.as_view(), name='exercise-log'),
    path('exercises/<int:exercise_id>/previous-logs/', PreviousExerciseLogsView.as_view(), name='previous-exercise-logs'),
]