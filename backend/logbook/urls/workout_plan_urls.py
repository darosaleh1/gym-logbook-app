from django.urls import path
from logbook.views.workout_plan_views import WorkoutPlanListView,WorkoutPlanDetailView,WorkoutPlanScheduleView


urlpatterns = [
    path('workout-plans/', WorkoutPlanListView.as_view(), name='workout-plan-list'),
    path('workout-plans/<int:pk>/', WorkoutPlanDetailView.as_view(), name='workout-plan-detail'),
    path('workout-plans/<int:pk>/schedule/', WorkoutPlanScheduleView.as_view(), name='workout-plan-schedule'),
]