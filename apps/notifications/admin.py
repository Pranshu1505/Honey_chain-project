from django.contrib import admin
from .models import Notification, Alert, NotificationPreference

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'notification_type', 'status', 'priority', 'created_at']
    list_filter = ['notification_type', 'status', 'priority', 'created_at']
    search_fields = ['title', 'message', 'user__username']

@admin.register(Alert)
class AlertAdmin(admin.ModelAdmin):
    list_display = ['alert_type', 'title', 'severity', 'is_resolved', 'created_at']
    list_filter = ['alert_type', 'severity', 'is_resolved', 'created_at']
    search_fields = ['title', 'description', 'alert_type']

@admin.register(NotificationPreference)
class NotificationPreferenceAdmin(admin.ModelAdmin):
    list_display = ['user', 'email_notifications', 'sms_notifications', 'push_notifications']
    list_filter = ['email_notifications', 'sms_notifications', 'push_notifications']
    search_fields = ['user__username', 'user__email']
