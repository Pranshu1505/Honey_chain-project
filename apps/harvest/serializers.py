"""Serializers for Harvest app"""
from rest_framework import serializers
from .models import Harvest


class HarvestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Harvest
        fields = [
            'id', 'hive', 'harvest_date', 'quantity', 'honey_type',
            'color_grade', 'notes', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class HarvestDetailSerializer(serializers.ModelSerializer):
    hive_name = serializers.CharField(source='hive.hive_id', read_only=True)
    
    class Meta:
        model = Harvest
        fields = [
            'id', 'hive', 'hive_name', 'harvest_date', 'quantity', 'honey_type',
            'color_grade', 'notes', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']
