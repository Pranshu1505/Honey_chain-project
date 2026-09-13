from django.contrib import admin
from .models import Retailer, Product, Sale

@admin.register(Retailer)
class RetailerAdmin(admin.ModelAdmin):
    list_display = ['store_name', 'store_type', 'location', 'status', 'rating', 'created_at']
    list_filter = ['store_type', 'status', 'created_at']
    search_fields = ['store_name', 'location']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'honey_type', 'price', 'quantity_available', 'is_available', 'created_at']
    list_filter = ['honey_type', 'is_available', 'created_at']
    search_fields = ['name', 'batch_id', 'honey_type']

@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ['id', 'quantity', 'total_amount', 'customer_name', 'status', 'sale_date']
    list_filter = ['status', 'payment_method', 'sale_date']
    search_fields = ['customer_name', 'customer_email']
