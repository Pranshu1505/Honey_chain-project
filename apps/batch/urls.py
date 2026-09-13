"""Batch URLs"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HoneyBatchViewSet

router = DefaultRouter()
router.register(r'', HoneyBatchViewSet, basename='batch')

urlpatterns = [path('', include(router.urls))]
