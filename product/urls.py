from django.urls import path, include
from .views import ProductViewSet, MaterialViewSet, ColorViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register(r'product', viewset=ProductViewSet, basename='products')
router.register(r'material', viewset=MaterialViewSet, basename='material')
router.register(r'color', viewset=ColorViewSet, basename='color')

urlpatterns = [ 
    path('v1/', include(router.urls))
]