"""Blockchain URLs"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BlockchainTransactionViewSet, BlockchainRecordViewSet

router = DefaultRouter()
router.register(r'transactions', BlockchainTransactionViewSet, basename='transaction')
router.register(r'records', BlockchainRecordViewSet, basename='record')

urlpatterns = [
    path('', include(router.urls)),
]
