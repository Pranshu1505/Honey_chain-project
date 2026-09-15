"""Serializers for Core app - Base serializers"""
from rest_framework import serializers


class BaseSerializerMixin(serializers.Serializer):
    """Mixin for common serializer fields"""
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)


class StatusSerializer(serializers.Serializer):
    """Status check serializer"""
    status = serializers.CharField()
    message = serializers.CharField()
    timestamp = serializers.DateTimeField()
    version = serializers.CharField(required=False)
