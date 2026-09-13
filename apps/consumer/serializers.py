from rest_framework import serializers
from .models import Consumer, Purchase, Review

class ConsumerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consumer
        fields = ['id', 'user', 'phone', 'address', 'city', 'state', 'postal_code',
                 'preferences', 'loyalty_points', 'total_purchases', 'created_at', 'updated_at']

class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = ['id', 'consumer', 'product_name', 'batch_id', 'quantity', 'price', 'total_amount',
                 'purchase_date', 'delivery_date', 'status', 'payment_method', 'rating', 'review',
                 'created_at', 'updated_at']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'purchase', 'rating', 'title', 'content', 'verified_purchase',
                 'helpful_count', 'created_at', 'updated_at']
