"""Sensor serializers and views"""
from rest_framework import serializers, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import SensorData


class SensorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorData
        fields = ['id', 'hive', 'sensor_type', 'sensor_id', 'value', 'unit', 'timestamp']
        read_only_fields = ['id', 'timestamp']


class SensorDataViewSet(viewsets.ModelViewSet):
    serializer_class = SensorDataSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return SensorData.objects.filter(hive__apiary__beekeeper=self.request.user)
    
    @action(detail=False, methods=['get'])
    def latest(self, request):
        """Get latest sensor data for all hives of current user"""
        hives = request.user.apiaries.all().values_list('hives__id', flat=True)
        
        latest_data = {}
        for sensor_type in ['temperature', 'humidity', 'weight']:
            data = SensorData.objects.filter(
                hive__id__in=hives,
                sensor_type=sensor_type
            ).order_by('-timestamp').first()
            if data:
                latest_data[sensor_type] = SensorDataSerializer(data).data
        
        return Response(latest_data)
