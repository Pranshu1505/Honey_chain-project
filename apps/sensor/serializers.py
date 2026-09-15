"""Serializers for Sensor app"""
from rest_framework import serializers
from .models import SensorData


class SensorDataSerializer(serializers.ModelSerializer):
    hive_id = serializers.CharField(source='hive.hive_id', read_only=True)
    
    class Meta:
        model = SensorData
        fields = [
            'id', 'hive', 'hive_id', 'sensor_type', 'sensor_id',
            'value', 'unit', 'timestamp'
        ]
        read_only_fields = ['id', 'timestamp']


class SensorDataDetailSerializer(serializers.ModelSerializer):
    hive_id = serializers.CharField(source='hive.hive_id', read_only=True)
    hive_location = serializers.CharField(source='hive.location', read_only=True)
    
    class Meta:
        model = SensorData
        fields = [
            'id', 'hive', 'hive_id', 'hive_location', 'sensor_type', 'sensor_id',
            'value', 'unit', 'timestamp'
        ]
        read_only_fields = ['id', 'timestamp']


class SensorDataBulkSerializer(serializers.ListSerializer):
    child = SensorDataSerializer()
    
    def create(self, validated_data):
        return [SensorData.objects.create(**item) for item in validated_data]
