"""Admin for harvest"""
from django.contrib import admin
from .models import Harvest

@admin.register(Harvest)
class HarvestAdmin(admin.ModelAdmin):
    list_display = ['hive', 'harvest_date', 'quantity', 'honey_type', 'color_grade']
    list_filter = ['honey_type', 'harvest_date']
    search_fields = ['hive__hive_id']
