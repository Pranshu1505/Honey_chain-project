"""Admin for batch"""
from django.contrib import admin
from .models import HoneyBatch

@admin.register(HoneyBatch)
class HoneyBatchAdmin(admin.ModelAdmin):
    list_display = ['batch_id', 'total_quantity', 'status', 'quality_score']
    list_filter = ['status', 'created_at']
    search_fields = ['batch_id']
