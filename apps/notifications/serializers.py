from rest_framework import serializers
from .models import Notification, Alert, NotificationPreference

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id', 'user', 'notification_type', 'title', 'message', 'related_id', 'status',
                 'priority', 'read_at', 'created_at', 'updated_at']

class AlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alert
        fields = ['id', 'alert_type', 'title', 'description', 'severity', 'related_object',
                 'affected_users', 'is_resolved', 'resolution_notes', 'created_at', 'resolved_at', 'updated_at']

class NotificationPreferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationPreference
        fields = ['id', 'user', 'email_notifications', 'sms_notifications', 'push_notifications',
                 'notify_shipments', 'notify_quality', 'notify_health', 'notify_inventory',
                 'notify_orders', 'quiet_hours_start', 'quiet_hours_end', 'created_at', 'updated_at']
