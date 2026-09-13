"""Hive models"""
from django.db import models
from apps.beekeeper.models import Apiary


class Hive(models.Model):
    HEALTH_STATUS_CHOICES = [
        ('healthy', 'Healthy'),
        ('warning', 'Warning'),
        ('critical', 'Critical'),
    ]
    
    apiary = models.ForeignKey(Apiary, on_delete=models.CASCADE, related_name='hives')
    hive_id = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=255)
    hive_type = models.CharField(max_length=50, choices=[
        ('langstroth', 'Langstroth'),
        ('topbar', 'Top-bar'),
        ('warre', 'Warré'),
    ])
    installation_date = models.DateField()
    last_inspection = models.DateField(null=True, blank=True)
    health_status = models.CharField(max_length=20, choices=HEALTH_STATUS_CHOICES, default='healthy')
    population = models.IntegerField(default=0, help_text="Number of bees")
    honey_frames = models.IntegerField(default=0)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'hives'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.hive_id} - {self.name}"


class HiveHealth(models.Model):
    """Health metrics for a hive"""
    hive = models.OneToOneField(Hive, on_delete=models.CASCADE, related_name='health_metrics')
    temperature = models.FloatField(help_text="Temperature in Celsius")
    humidity = models.FloatField(help_text="Humidity in percentage")
    weight = models.FloatField(help_text="Weight in kg")
    bee_activity = models.IntegerField(help_text="Bee activity level 0-100")
    disease_risk = models.CharField(max_length=50, choices=[
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ], default='low')
    last_updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'hive_health'
    
    def __str__(self):
        return f"Health metrics for {self.hive.hive_id}"
