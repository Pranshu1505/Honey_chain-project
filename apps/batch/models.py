"""Batch models"""
from django.db import models
from apps.harvest.models import Harvest


class HoneyBatch(models.Model):
    STATUS_CHOICES = [
        ('created', 'Created'),
        ('quality_tested', 'Quality Tested'),
        ('approved', 'Approved'),
        ('processing', 'Processing'),
        ('packaged', 'Packaged'),
        ('shipped', 'Shipped'),
    ]
    
    batch_id = models.CharField(max_length=50, unique=True)
    harvests = models.ManyToManyField(Harvest, related_name='batches')
    total_quantity = models.FloatField(help_text="Total quantity in kg")
    honey_type = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='created')
    
    quality_score = models.IntegerField(default=0, help_text="0-100")
    batch_blockchain_hash = models.CharField(max_length=255, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'honey_batches'
        ordering = ['-created_at']
    
    def __str__(self):
        return self.batch_id
