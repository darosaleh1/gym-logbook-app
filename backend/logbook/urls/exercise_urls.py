from django.urls import path
from logbook.views.exercise_views import ExerciseListView
urlpatterns = [
    path('exercises/',ExerciseListView.as_view(), name='exercise_list')
]