"""Hive serializers"""
from rest_framework import serializers
from .models import Hive, HiveHealth


class HiveHealthSerializer(serializers.ModelSerializer):
    class Meta:
        model = HiveHealth
        fields = ['temperature', 'humidity', 'weight', 'bee_activity', 'disease_risk', 'last_updated']
        read_only_fields = ['last_updated']


class HiveSerializer(serializers.ModelSerializer):
    health_metrics = HiveHealthSerializer(read_only=True)
    
    class Meta:
        model = Hive
        fields = ['id', 'hive_id', 'name', 'hive_type', 'apiary', 'installation_date', 'last_inspection',
                  'health_status', 'population', 'honey_frames', 'health_metrics', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
