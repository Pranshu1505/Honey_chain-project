"""Processing models"""
from django.db import models
from apps.batch.models import HoneyBatch
from django.contrib.auth.models import User


class Processing(models.Model):
    batch = models.OneToOneField(HoneyBatch, on_delete=models.CASCADE, related_name='processing')
    processor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='processed_batches')
    temperature = models.FloatField(help_text="Processing temperature in Celsius")
    duration = models.IntegerField(help_text="Processing duration in minutes")
    notes = models.TextField(blank=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'processing'


class QualityTest(models.Model):
    batch = models.OneToOneField(HoneyBatch, on_delete=models.CASCADE, related_name='quality_test')
    tester = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    acidity = models.FloatField()
    moisture = models.FloatField()
    color_intensity = models.IntegerField()
    aroma_grade = models.CharField(max_length=50)
    is_approved = models.BooleanField(default=False)
    test_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'quality_tests'
