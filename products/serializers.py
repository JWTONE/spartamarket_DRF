from rest_framework import serializers
from .models import Products
from django.contrib.auth import authenticate

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['title', 'content', 'images', 'price']

