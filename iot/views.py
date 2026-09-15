"""IoT Views - Handle sensor data and simulator"""
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core.cache import cache
from apps.sensor.models import SensorData
from apps.sensor.serializers import SensorDataSerializer, SensorDataDetailSerializer
from apps.hive.models import Hive
from .sensor_generator import SensorGenerator
from .alerts import SensorAlertSystem
import logging

logger = logging.getLogger(__name__)


@api_view(['GET', 'POST'])
def sensor_data_list(request):
    """List all sensor data or create new"""
    if request.method == 'GET':
        data = SensorData.objects.all().order_by('-timestamp')[:100]
        serializer = SensorDataSerializer(data, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = SensorDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # Check for alerts
            alerts = SensorAlertSystem.process_sensor_reading(
                serializer.instance.hive.id,
                serializer.instance.sensor_type,
                serializer.instance.value
            )
            return Response({
                'data': serializer.data,
                'alerts': alerts
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def sensor_data_detail(request, pk):
    """Get specific sensor reading"""
    try:
        sensor = SensorData.objects.get(pk=pk)
    except SensorData.DoesNotExist:
        return Response({'error': 'Sensor data not found'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = SensorDataDetailSerializer(sensor)
    return Response(serializer.data)


@api_view(['GET'])
def hive_sensor_data(request, hive_id):
    """Get all sensor data for a specific hive"""
    try:
        hive = Hive.objects.get(id=hive_id)
    except Hive.DoesNotExist:
        return Response({'error': 'Hive not found'}, status=status.HTTP_404_NOT_FOUND)
    
    # Get sensor data by type
    sensor_types = request.query_params.get('sensor_type')
    limit = request.query_params.get('limit', 50)
    
    data = SensorData.objects.filter(hive=hive).order_by('-timestamp')[:limit]
    
    if sensor_types:
        types = sensor_types.split(',')
        data = data.filter(sensor_type__in=types)
    
    serializer = SensorDataSerializer(data, many=True)
    return Response({
        'hive_id': hive.id,
        'hive_name': hive.hive_id,
        'data': serializer.data,
        'count': len(serializer.data),
    })


@api_view(['GET', 'POST'])
def start_simulator(request):
    """Start IoT simulator"""
    if request.method == 'POST':
        cache.set('iot_simulator_running', True, timeout=86400)
        return Response({'message': 'IoT simulator started'})
    
    is_running = cache.get('iot_simulator_running', False)
    return Response({'simulator_running': is_running})


@api_view(['POST'])
def stop_simulator(request):
    """Stop IoT simulator"""
    cache.delete('iot_simulator_running')
    return Response({'message': 'IoT simulator stopped'})


@api_view(['GET'])
def simulator_status(request):
    """Get simulator status"""
    is_running = cache.get('iot_simulator_running', False)
    return Response({
        'simulator_running': is_running,
        'status': 'running' if is_running else 'stopped'
    })


@api_view(['POST'])
def generate_sensor_data(request):
    """Generate and save sensor data for testing"""
    hive_id = request.data.get('hive_id')
    sensor_type = request.data.get('sensor_type')  # Optional: specific sensor type
    
    try:
        hive = Hive.objects.get(id=hive_id)
    except Hive.DoesNotExist:
        return Response({'error': 'Hive not found'}, status=status.HTTP_404_NOT_FOUND)
    
    generated_data = []
    
    if sensor_type:
        # Generate specific sensor type
        sensors = {
            'temperature': lambda hid: SensorGenerator.generate_temperature(hid),
            'humidity': lambda hid: SensorGenerator.generate_humidity(hid),
            'weight': lambda hid: SensorGenerator.generate_weight(hid),
            'sound': lambda hid: SensorGenerator.generate_sound_activity(hid),
        }
        
        generator = sensors.get(sensor_type)
        if not generator:
            return Response({'error': 'Invalid sensor type'}, status=status.HTTP_400_BAD_REQUEST)
        
        data = generator(hive_id)
        sensor = SensorData.objects.create(
            hive=hive,
            sensor_type=data['sensor_type'],
            sensor_id=data['sensor_id'],
            value=data['value'],
            unit=data['unit']
        )
        generated_data.append(SensorDataSerializer(sensor).data)
    else:
        # Generate all sensor types
        all_sensors = SensorGenerator.generate_all_sensors(hive_id)
        for data in all_sensors:
            sensor = SensorData.objects.create(
                hive=hive,
                sensor_type=data['sensor_type'],
                sensor_id=data['sensor_id'],
                value=data['value'],
                unit=data['unit']
            )
            generated_data.append(SensorDataSerializer(sensor).data)
    
    return Response({
        'message': f'Generated {len(generated_data)} sensor reading(s)',
        'data': generated_data,
        'count': len(generated_data)
    }, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def get_hive_alerts(request):
    """Get alerts for specific hive or all hives"""
    hive_id = request.query_params.get('hive_id')
    
    if not hive_id:
        return Response({'error': 'hive_id parameter required'}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        hive = Hive.objects.get(id=hive_id)
    except Hive.DoesNotExist:
        return Response({'error': 'Hive not found'}, status=status.HTTP_404_NOT_FOUND)
    
    # Get recent sensor data
    from django.utils import timezone
    from datetime import timedelta
    
    recent_data = SensorData.objects.filter(
        hive=hive,
        timestamp__gte=timezone.now() - timedelta(hours=24)
    )
    
    alerts = []
    for sensor in recent_data:
        alert = SensorAlertSystem.process_sensor_reading(
            hive_id,
            sensor.sensor_type,
            sensor.value
        )
        alerts.extend(alert)
    
    return Response({
        'hive_id': hive.id,
        'alerts': alerts,
        'alert_count': len(alerts)
    })


@api_view(['GET'])
def get_hive_health(request, hive_id):
    """Get hive health status"""
    try:
        hive = Hive.objects.get(id=hive_id)
    except Hive.DoesNotExist:
        return Response({'error': 'Hive not found'}, status=status.HTTP_404_NOT_FOUND)
    
    health_status = SensorAlertSystem.get_hive_health_status(hive_id)
    
    return Response({
        'hive_id': hive.id,
        'hive_name': hive.hive_id,
        'health_status': health_status
    })
