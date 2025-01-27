from django.urls import path, include

urlpatterns = [
    path('auth/', include('logbook.urls.auth_urls')),
    path('', include('logbook.urls.exercise_urls')),
    path('', include('logbook.urls.workout_urls')),
    path('', include('logbook.urls.workout_plan_urls')),
    path('', include('logbook.urls.workout_exercise_log_urls'))
]