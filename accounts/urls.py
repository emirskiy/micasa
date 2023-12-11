from django.urls import path, include
from rest_framework.routers import DefaultRouter
from accounts import views
from .views import UserViewSet

router = DefaultRouter()
router.register('user', UserViewSet)

urlpatterns = [
    path('login/', views.LoginApiView.as_view(), name='login'),
    # path('register/', views.RegisterAPIView.as_view(), name='register')
]