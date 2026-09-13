"""Harvest models"""
from django.db import models
from apps.hive.models import Hive


class Harvest(models.Model):
    hive = models.ForeignKey(Hive, on_delete=models.CASCADE, related_name='harvests')
    harvest_date = models.DateField()
    quantity = models.FloatField(help_text="Quantity in kg")
    honey_type = models.CharField(max_length=100, choices=[
        ('raw', 'Raw'),
        ('processed', 'Processed'),
        ('organic', 'Organic'),
        ('multifloral', 'Multifloral'),
    ])
    color_grade = models.CharField(max_length=50, choices=[
        ('extra_light', 'Extra Light'),
        ('light', 'Light'),
        ('amber', 'Amber'),
        ('dark', 'Dark'),
    ], blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'harvests'
        ordering = ['-harvest_date']
    
    def __str__(self):
        return f"Harvest from {self.hive.hive_id} on {self.harvest_date}"
