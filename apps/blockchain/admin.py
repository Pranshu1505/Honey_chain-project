"""Admin configuration for blockchain app"""
from django.contrib import admin
from .models import BlockchainTransaction, BlockchainRecord


@admin.register(BlockchainTransaction)
class BlockchainTransactionAdmin(admin.ModelAdmin):
    list_display = ['batch_id', 'transaction_type', 'status', 'user', 'timestamp']
    list_filter = ['transaction_type', 'status', 'timestamp']
    search_fields = ['batch_id', 'transaction_hash']
    readonly_fields = ['transaction_hash', 'timestamp']


@admin.register(BlockchainRecord)
class BlockchainRecordAdmin(admin.ModelAdmin):
    list_display = ['batch_id', 'origin', 'honey_type', 'quantity', 'quality_score']
    list_filter = ['honey_type', 'created_at']
    search_fields = ['batch_id', 'origin']
