from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .serializers import ProductSerializer
from main.models import Product


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.filter(is_published=True)
    serializer_class = ProductSerializer
