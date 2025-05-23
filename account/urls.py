from django.urls import path
from account.views import RegisterView, LoginView, LogOut
from .views import Test

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)



urlpatterns = [
    path('regis', RegisterView.as_view(), name='register'),
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('test/', Test.as_view(), name='test'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogOut.as_view(), name='logout'),
]