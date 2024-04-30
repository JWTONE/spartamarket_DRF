from django.urls import path

from products.models import Products  # 수정된 부분: Products -> Product로 변경
from .views import ProductsListAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = "products"
urlpatterns = [
    path('', ProductsListAPIView.as_view(), name='products'),
    path('products/',ProductsListAPIView.as_view(), name='products_view'),
    path('products/', ProductsListAPIView.as_view(), name='products_correction')
]
