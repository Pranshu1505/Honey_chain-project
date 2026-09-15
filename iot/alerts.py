"""IoT Alerts - Monitor sensor data for anomalies and generate alerts"""
from typing import Dict, List
from apps.notifications.models import Notification
from apps.hive.models import Hive
from django.contrib.auth.models import User


class SensorAlertSystem:
    """Monitor sensor data and generate alerts for anomalies"""
    
    # Alert thresholds
    TEMP_MIN = 28.0
    TEMP_MAX = 42.0
    HUMIDITY_MIN = 40.0
    HUMIDITY_MAX = 85.0
    WEIGHT_MIN = 25.0  # Minimum hive weight warning
    SOUND_MIN = 35.0  # Minimum activity threshold
    
    ALERT_TYPES = {
        'temperature_high': 'High Temperature Alert',
        'temperature_low': 'Low Temperature Alert',
        'humidity_high': 'High Humidity Alert',
        'humidity_low': 'Low Humidity Alert',
        'weight_low': 'Low Hive Weight Alert',
        'sound_low': 'Low Hive Activity Alert',
        'sensor_offline': 'Sensor Offline Alert',
    }
    
    @staticmethod
    def check_temperature(hive_id: int, value: float) -> Dict:
        """Check temperature readings for anomalies"""
        alerts = []
        
        if value > SensorAlertSystem.TEMP_MAX:
            alerts.append({
                'type': 'temperature_high',
                'message': f'Temperature critically high: {value}°C',
                'severity': 'high',
            })
        elif value < SensorAlertSystem.TEMP_MIN:
            alerts.append({
                'type': 'temperature_low',
                'message': f'Temperature too low: {value}°C',
                'severity': 'medium',
            })
        
        return {'alerts': alerts, 'sensor_type': 'temperature'}
    
    @staticmethod
    def check_humidity(hive_id: int, value: float) -> Dict:
        """Check humidity readings for anomalies"""
        alerts = []
        
        if value > SensorAlertSystem.HUMIDITY_MAX:
            alerts.append({
                'type': 'humidity_high',
                'message': f'Humidity too high: {value}%',
                'severity': 'high',
            })
        elif value < SensorAlertSystem.HUMIDITY_MIN:
            alerts.append({
                'type': 'humidity_low',
                'message': f'Humidity too low: {value}%',
                'severity': 'medium',
            })
        
        return {'alerts': alerts, 'sensor_type': 'humidity'}
    
    @staticmethod
    def check_weight(hive_id: int, value: float) -> Dict:
        """Check hive weight for concerns"""
        alerts = []
        
        if value < SensorAlertSystem.WEIGHT_MIN:
            alerts.append({
                'type': 'weight_low',
                'message': f'Hive weight critically low: {value}kg',
                'severity': 'high',
            })
        
        return {'alerts': alerts, 'sensor_type': 'weight'}
    
    @staticmethod
    def check_sound(hive_id: int, value: float) -> Dict:
        """Check sound activity levels"""
        alerts = []
        
        if value < SensorAlertSystem.SOUND_MIN:
            alerts.append({
                'type': 'sound_low',
                'message': f'Hive activity abnormally low: {value}dB',
                'severity': 'medium',
            })
        
        return {'alerts': alerts, 'sensor_type': 'sound'}
    
    @staticmethod
    def process_sensor_reading(hive_id: int, sensor_type: str, value: float) -> List[Dict]:
        """Process sensor reading and generate alerts if needed"""
        checker_map = {
            'temperature': SensorAlertSystem.check_temperature,
            'humidity': SensorAlertSystem.check_humidity,
            'weight': SensorAlertSystem.check_weight,
            'sound': SensorAlertSystem.check_sound,
        }
        
        checker = checker_map.get(sensor_type)
        if not checker:
            return []
        
        result = checker(hive_id, value)
        
        # Create notifications for alerts
        alerts = []
        try:
            hive = Hive.objects.get(id=hive_id)
            if hive.beekeeper:
                for alert in result['alerts']:
                    alerts.append(alert)
                    # Create notification
                    Notification.objects.create(
                        recipient=hive.beekeeper.user,
                        title=SensorAlertSystem.ALERT_TYPES.get(alert['type'], 'Sensor Alert'),
                        message=alert['message'],
                        alert_type='sensor',
                        severity=alert['severity'],
                    )
        except Hive.DoesNotExist:
            pass
        
        return alerts
    
    @staticmethod
    def get_hive_health_status(hive_id: int) -> Dict:
        """Get overall health status of a hive based on recent sensor data"""
        from apps.sensor.models import SensorData
        from django.utils import timezone
        from datetime import timedelta
        
        try:
            hive = Hive.objects.get(id=hive_id)
        except Hive.DoesNotExist:
            return {'status': 'unknown', 'message': 'Hive not found'}
        
        # Get recent sensor data (last 24 hours)
        recent_data = SensorData.objects.filter(
            hive=hive,
            timestamp__gte=timezone.now() - timedelta(hours=24)
        )
        
        if not recent_data.exists():
            return {'status': 'no_data', 'message': 'No recent sensor data'}
        
        # Analyze sensor data
        health_score = 100
        issues = []
        
        temp_readings = recent_data.filter(sensor_type='temperature')
        if temp_readings.exists():
            avg_temp = sum(r.value for r in temp_readings) / temp_readings.count()
            if avg_temp > SensorAlertSystem.TEMP_MAX or avg_temp < SensorAlertSystem.TEMP_MIN:
                health_score -= 20
                issues.append(f'Temperature: {avg_temp:.1f}°C')
        
        humidity_readings = recent_data.filter(sensor_type='humidity')
        if humidity_readings.exists():
            avg_humidity = sum(r.value for r in humidity_readings) / humidity_readings.count()
            if avg_humidity > SensorAlertSystem.HUMIDITY_MAX or avg_humidity < SensorAlertSystem.HUMIDITY_MIN:
                health_score -= 15
                issues.append(f'Humidity: {avg_humidity:.1f}%')
        
        weight_readings = recent_data.filter(sensor_type='weight')
        if weight_readings.exists():
            latest_weight = weight_readings.latest('timestamp').value
            if latest_weight < SensorAlertSystem.WEIGHT_MIN:
                health_score -= 30
                issues.append(f'Weight: {latest_weight:.1f}kg')
        
        sound_readings = recent_data.filter(sensor_type='sound')
        if sound_readings.exists():
            avg_sound = sum(r.value for r in sound_readings) / sound_readings.count()
            if avg_sound < SensorAlertSystem.SOUND_MIN:
                health_score -= 20
                issues.append(f'Activity: {avg_sound:.1f}dB')
        
        # Determine status
        if health_score >= 80:
            status = 'healthy'
        elif health_score >= 60:
            status = 'warning'
        else:
            status = 'critical'
        
        return {
            'status': status,
            'health_score': max(0, health_score),
            'issues': issues,
            'message': f'Hive health: {status.upper()} (Score: {health_score}%)',
        }
