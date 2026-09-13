"""Admin for processing"""
from django.contrib import admin
from .models import Processing, QualityTest

@admin.register(Processing)
class ProcessingAdmin(admin.ModelAdmin):
    list_display = ['batch', 'processor', 'temperature', 'duration']

@admin.register(QualityTest)
class QualityTestAdmin(admin.ModelAdmin):
    list_display = ['batch', 'acidity', 'moisture', 'is_approved']
