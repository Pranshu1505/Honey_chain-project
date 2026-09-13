"""Harvest serializers and views"""
from rest_framework import serializers, viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Harvest


class HarvestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Harvest
        fields = ['id', 'hive', 'harvest_date', 'quantity', 'honey_type', 'color_grade', 'notes', 'created_at']
        read_only_fields = ['id', 'created_at']


class HarvestViewSet(viewsets.ModelViewSet):
    serializer_class = HarvestSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Harvest.objects.filter(hive__apiary__beekeeper=self.request.user)
