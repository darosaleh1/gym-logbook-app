from django.urls import path, include

urlpatterns = [
    path('auth/', include('logbook.urls.auth_urls')),
    path('', include('logbook.urls.exercise_urls')),
]