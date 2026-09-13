"""Beekeeper models"""
from django.db import models
from django.contrib.auth.models import User


class Apiary(models.Model):
    """Represents a beekeeper's apiary (bee farm)"""
    beekeeper = models.ForeignKey(User, on_delete=models.CASCADE, related_name='apiaries')
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    total_hives = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'apiaries'
        ordering = ['-created_at']
    
    def __str__(self):
        return self.name


class BeekeeperProfile(models.Model):
    """Extended beekeeper profile"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='beekeeper_profile')
    years_of_experience = models.IntegerField(default=0)
    total_hives = models.IntegerField(default=0)
    avg_honey_yield = models.FloatField(default=0.0, help_text="Average honey yield in kg per year")
    certification = models.CharField(max_length=255, blank=True)
    bank_account = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'beekeeper_profiles'
    
    def __str__(self):
        return f"{self.user.get_full_name()} - Beekeeper"
