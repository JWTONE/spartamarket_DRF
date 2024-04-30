from django.urls import path
from .views import UserCreateAPIView, UserLoginAPIView, UserProfileAPIView

urlpatterns = [
    path('api/accounts', UserCreateAPIView.as_view(), name='user-create'),
    path('api/accounts/login', UserLoginAPIView.as_view(), name='user-login'),
    path('api/accounts/<str:username>', UserProfileAPIView.as_view(), name='user-profile'),
]
