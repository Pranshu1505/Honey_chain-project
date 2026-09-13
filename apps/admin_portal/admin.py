"""Admin configuration for admin_portal"""
from django.contrib import admin
from .models import AdminReport, AuditLog


@admin.register(AdminReport)
class AdminReportAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_by', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title']


@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
    list_display = ['user', 'action', 'resource_type', 'resource_id', 'timestamp']
    list_filter = ['action', 'timestamp']
    search_fields = ['user__username', 'resource_type']
    readonly_fields = ['timestamp', 'user', 'action', 'resource_type', 'resource_id', 'details']
