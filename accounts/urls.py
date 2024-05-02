from django.urls import path
from .views import UserCreateAPIView, UserProfileAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = "accounts"
urlpatterns = [
    path('', UserCreateAPIView.as_view(), name='user-create'),
    path('login/', TokenObtainPairView.as_view(), name='user-login'),
    path('signup/', UserCreateAPIView.as_view(), name='signup'),
    path('logout/', TokenRefreshView.as_view(), name="logout"),
    path('<str:username>/', UserProfileAPIView.as_view(), name='user-profile'),
]
