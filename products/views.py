from functools import partial
from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .serializers import ProductsSerializer
from .models import Products

from rest_framework.pagination import PageNumberPagination

class ProductsListAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self, request):
        paginator = PageNumberPagination()
        paginator.page_size = 6
        
        products = Products.objects.all()
        result_page = paginator.paginate_queryset(products, request)
        serializer = ProductsSerializer(result_page, many=True)
        return Response(serializer.data)
        
    def post(self, request):
        serializer = ProductsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(username=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
    
    def put(self, request, productID):
        
        update = get_object_or_404(Products, id=productID)
        serializer = ProductsSerializer(update, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)