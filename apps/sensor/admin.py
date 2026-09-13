"""Admin for sensor"""
from django.contrib import admin
from .models import SensorData

@admin.register(SensorData)
class SensorDataAdmin(admin.ModelAdmin):
    list_display = ['hive', 'sensor_type', 'value', 'unit', 'timestamp']
    list_filter = ['sensor_type', 'timestamp']
    search_fields = ['hive__hive_id', 'sensor_id']
