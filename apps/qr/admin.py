"""Admin for QR"""
from django.contrib import admin
from .models import QRCode

@admin.register(QRCode)
class QRCodeAdmin(admin.ModelAdmin):
    list_display = ['batch', 'scans', 'created_at']
    list_filter = ['created_at']
    search_fields = ['batch__batch_id']
