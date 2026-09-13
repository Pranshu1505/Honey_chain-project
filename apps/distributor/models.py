from django.db import models
from django.contrib.auth.models import User

class Distributor(models.Model):
    """Distributor model"""
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('suspended', 'Suspended'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='distributor_profile')
    company_name = models.CharField(max_length=255)
    registration_number = models.CharField(max_length=50, unique=True)
    location = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    storage_capacity = models.DecimalField(max_digits=10, decimal_places=2, help_text='Storage capacity in kg')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
    certification = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.company_name


class Shipment(models.Model):
    """Shipment tracking model"""
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_transit', 'In Transit'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    ]
    
    distributor = models.ForeignKey(Distributor, on_delete=models.CASCADE, related_name='shipments')
    batch_id = models.CharField(max_length=50)
    destination = models.CharField(max_length=255)
    quantity = models.DecimalField(max_digits=10, decimal_places=2, help_text='Quantity in kg')
    shipment_date = models.DateTimeField(auto_now_add=True)
    expected_delivery = models.DateTimeField()
    actual_delivery = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    tracking_number = models.CharField(max_length=50, unique=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-shipment_date']
    
    def __str__(self):
        return f"Shipment {self.tracking_number}"


class Inventory(models.Model):
    """Distributor inventory model"""
    distributor = models.ForeignKey(Distributor, on_delete=models.CASCADE, related_name='inventory')
    batch_id = models.CharField(max_length=50)
    honey_type = models.CharField(max_length=100)
    quantity = models.DecimalField(max_digits=10, decimal_places=2, help_text='Quantity in kg')
    received_date = models.DateTimeField()
    expiry_date = models.DateField()
    quality_score = models.IntegerField(default=0)
    storage_location = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=[('in_stock', 'In Stock'), ('sold', 'Sold')], default='in_stock')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-received_date']
        unique_together = ('distributor', 'batch_id')
    
    def __str__(self):
        return f"{self.batch_id} - {self.quantity}kg"
