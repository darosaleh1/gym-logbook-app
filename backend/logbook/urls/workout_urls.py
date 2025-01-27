from django.urls import path
from logbook.views.workout_views import WorkoutListView, WorkoutDetailView, WorkoutExercisesView

urlpatterns = [
    path('workouts/', WorkoutListView.as_view(), name="workout_list" ),
    path('workouts/<int:pk>/', WorkoutDetailView.as_view(), name="workout_detail"),
    path('workouts/<int:pk>/exercises/', WorkoutExercisesView.as_view(), name="workout_exercises"),
]