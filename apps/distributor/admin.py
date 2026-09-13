from django.contrib import admin
from .models import Distributor, Shipment, Inventory

@admin.register(Distributor)
class DistributorAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'registration_number', 'location', 'status', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['company_name', 'registration_number']

@admin.register(Shipment)
class ShipmentAdmin(admin.ModelAdmin):
    list_display = ['tracking_number', 'batch_id', 'status', 'shipment_date', 'expected_delivery']
    list_filter = ['status', 'shipment_date']
    search_fields = ['tracking_number', 'batch_id']

@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ['batch_id', 'honey_type', 'quantity', 'status', 'received_date']
    list_filter = ['status', 'honey_type', 'received_date']
    search_fields = ['batch_id', 'honey_type']
