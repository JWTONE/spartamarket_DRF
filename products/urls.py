from django.urls import path

from products.models import Products  # 수정된 부분: Products -> Product로 변경
from .views import ProductsListAPIView


app_name = "products"
urlpatterns = [
    path('', ProductsListAPIView.as_view(), name='products'),
    path('<int:productID>/', ProductsListAPIView.as_view(), name='products_correction')
]
