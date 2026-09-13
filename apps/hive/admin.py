"""Admin configuration for hive app"""
from django.contrib import admin
from .models import Hive, HiveHealth


@admin.register(Hive)
class HiveAdmin(admin.ModelAdmin):
    list_display = ['hive_id', 'name', 'apiary', 'health_status', 'population', 'created_at']
    list_filter = ['health_status', 'hive_type', 'created_at']
    search_fields = ['hive_id', 'name']


@admin.register(HiveHealth)
class HiveHealthAdmin(admin.ModelAdmin):
    list_display = ['hive', 'temperature', 'humidity', 'disease_risk', 'last_updated']
    list_filter = ['disease_risk', 'last_updated']
    search_fields = ['hive__hive_id']
