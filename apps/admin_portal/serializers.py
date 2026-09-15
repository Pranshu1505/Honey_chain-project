"""Serializers for Admin Portal app"""
from rest_framework import serializers
from .models import AdminReport, AuditLog


class AdminReportSerializer(serializers.ModelSerializer):
    created_by_name = serializers.CharField(source='created_by.username', read_only=True)
    
    class Meta:
        model = AdminReport
        fields = [
            'id', 'title', 'description', 'report_data', 'created_by',
            'created_by_name', 'created_at'
        ]
        read_only_fields = ['id', 'created_at']


class AuditLogSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.username', read_only=True)
    
    class Meta:
        model = AuditLog
        fields = [
            'id', 'user', 'user_name', 'action', 'resource_type',
            'resource_id', 'details', 'timestamp'
        ]
        read_only_fields = ['id', 'timestamp']


class AdminReportDetailSerializer(serializers.ModelSerializer):
    created_by_name = serializers.CharField(source='created_by.username', read_only=True)
    created_by_email = serializers.CharField(source='created_by.email', read_only=True)
    
    class Meta:
        model = AdminReport
        fields = [
            'id', 'title', 'description', 'report_data', 'created_by',
            'created_by_name', 'created_by_email', 'created_at'
        ]
        read_only_fields = ['id', 'created_at']
