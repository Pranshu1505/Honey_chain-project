"""IoT API Routes - Handle sensor data ingestion and retrieval"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'iot'

urlpatterns = [
    # Sensor data endpoints
    path('sensors/data/', views.sensor_data_list, name='sensor_data_list'),
    path('sensors/data/<int:pk>/', views.sensor_data_detail, name='sensor_data_detail'),
    path('sensors/hive/<int:hive_id>/', views.hive_sensor_data, name='hive_sensor_data'),
    
    # Simulator endpoints
    path('simulator/start/', views.start_simulator, name='start_simulator'),
    path('simulator/stop/', views.stop_simulator, name='stop_simulator'),
    path('simulator/status/', views.simulator_status, name='simulator_status'),
    path('simulator/generate/', views.generate_sensor_data, name='generate_sensor_data'),
    
    # Alert endpoints
    path('alerts/', views.get_hive_alerts, name='get_hive_alerts'),
    path('health/<int:hive_id>/', views.get_hive_health, name='get_hive_health'),
]
