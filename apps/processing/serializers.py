"""Serializers for Processing app"""
from rest_framework import serializers
from .models import Processing, QualityTest


class ProcessingSerializer(serializers.ModelSerializer):
    processor_name = serializers.CharField(source='processor.username', read_only=True)
    
    class Meta:
        model = Processing
        fields = [
            'id', 'batch', 'processor', 'processor_name', 'temperature',
            'duration', 'notes', 'completed_at', 'created_at'
        ]
        read_only_fields = ['id', 'created_at']


class QualityTestSerializer(serializers.ModelSerializer):
    tester_name = serializers.CharField(source='tester.username', read_only=True)
    
    class Meta:
        model = QualityTest
        fields = [
            'id', 'batch', 'tester', 'tester_name', 'acidity', 'moisture',
            'color_intensity', 'aroma_grade', 'is_approved', 'test_date'
        ]
        read_only_fields = ['id', 'test_date']


class ProcessingDetailSerializer(serializers.ModelSerializer):
    processor_name = serializers.CharField(source='processor.username', read_only=True)
    quality_test = QualityTestSerializer(read_only=True)
    
    class Meta:
        model = Processing
        fields = [
            'id', 'batch', 'processor', 'processor_name', 'temperature',
            'duration', 'notes', 'quality_test', 'completed_at', 'created_at'
        ]
        read_only_fields = ['id', 'created_at']
