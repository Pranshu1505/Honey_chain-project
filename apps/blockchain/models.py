"""Blockchain models for transaction records"""
from django.db import models
from django.contrib.auth.models import User


class BlockchainTransaction(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('failed', 'Failed'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='blockchain_transactions')
    batch_id = models.CharField(max_length=255)
    transaction_hash = models.CharField(max_length=255, unique=True)
    transaction_type = models.CharField(max_length=100, choices=[
        ('batch_creation', 'Batch Creation'),
        ('quality_check', 'Quality Check'),
        ('processing', 'Processing'),
        ('packaging', 'Packaging'),
        ('shipment', 'Shipment'),
        ('delivery', 'Delivery'),
    ])
    data = models.JSONField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    block_number = models.IntegerField(null=True, blank=True)
    contract_address = models.CharField(max_length=255, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    confirmed_at = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        db_table = 'blockchain_transactions'
        ordering = ['-timestamp']
    
    def __str__(self):
        return f"{self.batch_id} - {self.transaction_type}"


class BlockchainRecord(models.Model):
    """Immutable record of honey batch on blockchain"""
    batch_id = models.CharField(max_length=255, unique=True)
    origin = models.CharField(max_length=255, help_text="Origin/Apiary")
    transaction_hash = models.CharField(max_length=255)
    block_number = models.IntegerField()
    honey_type = models.CharField(max_length=100, blank=True)
    quantity = models.FloatField(help_text="Quantity in kg")
    quality_score = models.IntegerField(default=0, help_text="Quality score 0-100")
    test_results = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'blockchain_records'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Batch {self.batch_id}"
