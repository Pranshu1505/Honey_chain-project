"""Serializers for Batch app"""
from rest_framework import serializers
from .models import HoneyBatch


class HoneyBatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = HoneyBatch
        fields = [
            'id', 'batch_id', 'harvests', 'total_quantity', 'honey_type',
            'status', 'quality_score', 'batch_blockchain_hash', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at', 'batch_blockchain_hash']


class HoneyBatchDetailSerializer(serializers.ModelSerializer):
    harvests = serializers.StringRelatedField(many=True, read_only=True)
    
    class Meta:
        model = HoneyBatch
        fields = [
            'id', 'batch_id', 'harvests', 'total_quantity', 'honey_type',
            'status', 'quality_score', 'batch_blockchain_hash', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at', 'batch_blockchain_hash']
