"""Admin configuration for beekeeper app"""
from django.contrib import admin
from .models import Apiary, BeekeeperProfile


@admin.register(Apiary)
class ApiaryAdmin(admin.ModelAdmin):
    list_display = ['name', 'beekeeper', 'location', 'total_hives', 'created_at']
    list_filter = ['created_at', 'beekeeper']
    search_fields = ['name', 'location']


@admin.register(BeekeeperProfile)
class BeekeeperProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'years_of_experience', 'total_hives', 'avg_honey_yield']
    list_filter = ['created_at']
    search_fields = ['user__username', 'user__email']
