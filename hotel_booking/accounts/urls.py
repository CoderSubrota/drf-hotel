from django.urls import path
from accounts.views import RegisterView, ActivateUserView,VerifyTokenView
from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('', RegisterView.as_view(), name='register'),
    path('activate/<uidb64>/<token>/', ActivateUserView.as_view(), name='activate'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', VerifyTokenView.as_view(), name='token_verify'),
]
