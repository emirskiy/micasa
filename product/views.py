from django.shortcuts import render
from .models import Product, Color, Material
from .serializers import ProductSerializer, ColorSerializer, MaterialSerializer
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated


# Create your views here.


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['name']
    search_fields = ['name']


class ColorViewSet(viewsets.ModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['name']
    search_fields = ['name']


class MaterialViewSet(viewsets.ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['material']
    search_fields = ['material']