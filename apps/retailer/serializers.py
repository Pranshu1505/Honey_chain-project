from rest_framework import serializers
from .models import Retailer, Product, Sale

class RetailerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Retailer
        fields = ['id', 'user', 'store_name', 'store_type', 'location', 'phone', 'email', 'website',
                 'status', 'rating', 'total_sales', 'created_at', 'updated_at']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'retailer', 'name', 'batch_id', 'honey_type', 'price', 'quantity_available',
                 'unit', 'description', 'quality_score', 'certification', 'is_available', 'created_at', 'updated_at']

class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = ['id', 'product', 'quantity', 'total_amount', 'customer_name', 'customer_phone',
                 'customer_email', 'sale_date', 'delivery_date', 'status', 'payment_method', 'notes',
                 'created_at', 'updated_at']
