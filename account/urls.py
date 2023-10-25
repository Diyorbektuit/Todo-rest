from django.urls import path
from .views import RegistrationView, CustomTokenObtainPairView, CustomTokenRefreshView

urlpatterns = [
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
    path('api/register/', RegistrationView.as_view(), name='registration'),
]
