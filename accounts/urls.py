from django.urls import path
from .views import UserCreateAPIView, UserProfileAPIView, UserPasswordChangeAPIView, UserLogoutAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView
)

app_name = "accounts"
urlpatterns = [
    path('', UserCreateAPIView.as_view(), name='user-create'),
    path('login/', TokenObtainPairView.as_view(), name='user-login'),
    path('signup/', UserCreateAPIView.as_view(), name='signup'),
    path('logout/', UserLogoutAPIView.as_view(), name="logout"),
    path('password/', UserPasswordChangeAPIView.as_view(), name='password'),
    path('<str:username>/', UserProfileAPIView.as_view(), name='user-profile'),
]
