from django.shortcuts import render
from .models import Product, Color, Material
from .serializers import ProductSerializer, ColorSerializer, MaterialSerializer
from rest_framework import viewsets, filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class AllAPIListPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 10000



class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = []
    authentication_classes = []
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['name']
    search_fields = ['name']
    pagination_class = AllAPIListPagination


class ColorViewSet(viewsets.ModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer
    permission_classes = []
    authentication_classes = []
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['name']
    pagination_class = AllAPIListPagination


class MaterialViewSet(viewsets.ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
    permission_classes = []
    authentication_classes = []
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['material']
    search_fields = ['material']
    pagination_class = AllAPIListPagination



