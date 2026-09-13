from django.contrib import admin
from .models import Consumer, Purchase, Review

@admin.register(Consumer)
class ConsumerAdmin(admin.ModelAdmin):
    list_display = ['user', 'city', 'loyalty_points', 'total_purchases', 'created_at']
    list_filter = ['city', 'state', 'created_at']
    search_fields = ['user__username', 'user__email', 'city']

@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ['id', 'consumer', 'product_name', 'quantity', 'total_amount', 'status', 'purchase_date']
    list_filter = ['status', 'payment_method', 'purchase_date']
    search_fields = ['consumer__user__username', 'product_name', 'batch_id']

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'purchase', 'rating', 'title', 'verified_purchase', 'helpful_count']
    list_filter = ['rating', 'verified_purchase', 'created_at']
    search_fields = ['title', 'content']
