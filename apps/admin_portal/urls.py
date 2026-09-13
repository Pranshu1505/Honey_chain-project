"""Admin Portal URLs"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AdminReportViewSet, AuditLogViewSet, AdminDashboardViewSet

router = DefaultRouter()
router.register(r'reports', AdminReportViewSet, basename='report')
router.register(r'audit-logs', AuditLogViewSet, basename='audit-log')
router.register(r'dashboard', AdminDashboardViewSet, basename='dashboard')

urlpatterns = [path('', include(router.urls))]
