"""Sensor models for IoT data collection"""
from django.db import models
from apps.hive.models import Hive


class SensorData(models.Model):
    SENSOR_TYPE_CHOICES = [
        ('temperature', 'Temperature'),
        ('humidity', 'Humidity'),
        ('weight', 'Weight'),
        ('sound', 'Sound Activity'),
    ]
    
    hive = models.ForeignKey(Hive, on_delete=models.CASCADE, related_name='sensor_data')
    sensor_type = models.CharField(max_length=50, choices=SENSOR_TYPE_CHOICES)
    sensor_id = models.CharField(max_length=100)
    value = models.FloatField()
    unit = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'sensor_data'
        ordering = ['-timestamp']
        indexes = [
            models.Index(fields=['hive', '-timestamp']),
            models.Index(fields=['sensor_type']),
        ]
    
    def __str__(self):
        return f"{self.sensor_type} - {self.value} {self.unit}"
