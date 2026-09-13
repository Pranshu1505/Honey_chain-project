"""Beekeeper serializers"""
from rest_framework import serializers
from .models import Apiary, BeekeeperProfile


class ApiarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Apiary
        fields = ['id', 'name', 'location', 'latitude', 'longitude', 'total_hives', 'description', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']


class BeekeeperProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = BeekeeperProfile
        fields = ['id', 'user', 'years_of_experience', 'total_hives', 'avg_honey_yield', 'certification', 'bank_account', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
