from django.urls import path
from .views import EmailTokenObtainPairView, RegisterView

urlpatterns = [
    path('token/', EmailTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register/', RegisterView.as_view(), name='register'),
]
