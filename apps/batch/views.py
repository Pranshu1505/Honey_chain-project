"""Batch serializers and views"""
from rest_framework import serializers, viewsets
from rest_framework.permissions import IsAuthenticated
from .models import HoneyBatch


class HoneyBatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = HoneyBatch
        fields = ['id', 'batch_id', 'total_quantity', 'honey_type', 'status', 'quality_score', 
                  'batch_blockchain_hash', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']


class HoneyBatchViewSet(viewsets.ModelViewSet):
    serializer_class = HoneyBatchSerializer
    permission_classes = [IsAuthenticated]
    queryset = HoneyBatch.objects.all()
