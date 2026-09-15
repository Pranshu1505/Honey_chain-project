"""Serializers for QR app"""
from rest_framework import serializers
from .models import QRCode


class QRCodeSerializer(serializers.ModelSerializer):
    batch_id = serializers.CharField(source='batch.batch_id', read_only=True)
    
    class Meta:
        model = QRCode
        fields = ['id', 'batch', 'batch_id', 'code_data', 'qr_image', 'scans', 'created_at']
        read_only_fields = ['id', 'created_at', 'scans']


class QRCodeDetailSerializer(serializers.ModelSerializer):
    batch_id = serializers.CharField(source='batch.batch_id', read_only=True)
    batch_details = serializers.SerializerMethodField()
    
    class Meta:
        model = QRCode
        fields = ['id', 'batch', 'batch_id', 'batch_details', 'code_data', 'qr_image', 'scans', 'created_at']
        read_only_fields = ['id', 'created_at', 'scans']
    
    def get_batch_details(self, obj):
        return {
            'batch_id': obj.batch.batch_id,
            'honey_type': obj.batch.honey_type,
            'total_quantity': obj.batch.total_quantity,
            'status': obj.batch.status
        }
