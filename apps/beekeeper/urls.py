"""Beekeeper URLs"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ApiaryViewSet, BeekeeperProfileViewSet

router = DefaultRouter()
router.register(r'apiaries', ApiaryViewSet, basename='apiary')
router.register(r'profile', BeekeeperProfileViewSet, basename='profile')

urlpatterns = [
    path('', include(router.urls)),
]
