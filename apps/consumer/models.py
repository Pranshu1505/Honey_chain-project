from django.db import models
from django.contrib.auth.models import User

class Consumer(models.Model):
    """Consumer model"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='consumer_profile')
    phone = models.CharField(max_length=20)
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    preferences = models.JSONField(default=dict, blank=True, help_text='User preferences and dietary info')
    loyalty_points = models.IntegerField(default=0)
    total_purchases = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.user.get_full_name()}"


class Purchase(models.Model):
    """Consumer purchase model"""
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
        ('refunded', 'Refunded'),
    ]
    
    consumer = models.ForeignKey(Consumer, on_delete=models.CASCADE, related_name='purchases')
    product_name = models.CharField(max_length=255)
    batch_id = models.CharField(max_length=50)
    quantity = models.DecimalField(max_digits=10, decimal_places=2, help_text='In kg')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    payment_method = models.CharField(max_length=50, choices=[('cash', 'Cash'), ('card', 'Card'), ('online', 'Online')])
    rating = models.IntegerField(null=True, blank=True, help_text='1-5 star rating')
    review = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-purchase_date']
    
    def __str__(self):
        return f"Purchase #{self.id} - {self.consumer.user.username}"


class Review(models.Model):
    """Product review model"""
    purchase = models.OneToOneField(Purchase, on_delete=models.CASCADE, related_name='detailed_review')
    rating = models.IntegerField(choices=[(i, f'{i} Stars') for i in range(1, 6)])
    title = models.CharField(max_length=200)
    content = models.TextField()
    verified_purchase = models.BooleanField(default=True)
    helpful_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-helpful_count', '-created_at']
    
    def __str__(self):
        return f"Review for Purchase #{self.purchase.id}"
