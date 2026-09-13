"""Processing URLs"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProcessingViewSet, QualityTestViewSet

router = DefaultRouter()
router.register(r'quality-test', QualityTestViewSet, basename='quality-test')
router.register(r'', ProcessingViewSet, basename='processing')

urlpatterns = [path('', include(router.urls))]
