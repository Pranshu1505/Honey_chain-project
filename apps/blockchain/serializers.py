"""Blockchain serializers"""
from rest_framework import serializers
from .models import BlockchainTransaction, BlockchainRecord


class BlockchainTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlockchainTransaction
        fields = ['id', 'batch_id', 'transaction_hash', 'transaction_type', 'data', 'status', 
                  'block_number', 'contract_address', 'timestamp', 'confirmed_at']
        read_only_fields = ['id', 'timestamp', 'confirmed_at']


class BlockchainRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlockchainRecord
        fields = ['id', 'batch_id', 'origin', 'transaction_hash', 'block_number', 'honey_type',
                  'quantity', 'quality_score', 'test_results', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
