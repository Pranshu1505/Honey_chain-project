from rest_framework import serializers
from .models import Distributor, Shipment, Inventory

class DistributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Distributor
        fields = ['id', 'user', 'company_name', 'registration_number', 'location', 'phone', 
                 'email', 'storage_capacity', 'status', 'certification', 'created_at', 'updated_at']

class ShipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipment
        fields = ['id', 'distributor', 'batch_id', 'destination', 'quantity', 'shipment_date',
                 'expected_delivery', 'actual_delivery', 'status', 'tracking_number', 'notes', 
                 'created_at', 'updated_at']

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ['id', 'distributor', 'batch_id', 'honey_type', 'quantity', 'received_date',
                 'expiry_date', 'quality_score', 'storage_location', 'status', 'created_at', 'updated_at']
