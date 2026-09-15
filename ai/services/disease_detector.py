"""Disease Detector Service - Detects potential hive diseases"""
from typing import Dict, List
from apps.sensor.models import SensorData
from apps.hive.models import Hive
from django.utils import timezone
from datetime import timedelta
from .disease_prediction import DiseasePredictionModel
import statistics


class DiseaseDetectorService:
    """Service for disease detection and prediction"""
    
    @staticmethod
    def detect_diseases(hive_id: int, hours: int = 48) -> Dict:
        """Detect potential diseases in hive"""
        try:
            hive = Hive.objects.get(id=hive_id)
        except Hive.DoesNotExist:
            return {'error': 'Hive not found'}
        
        # Get sensor data
        time_threshold = timezone.now() - timedelta(hours=hours)
        sensor_data = SensorData.objects.filter(
            hive=hive,
            timestamp__gte=time_threshold
        )
        
        if not sensor_data.exists():
            return {'error': f'No sensor data in past {hours} hours'}
        
        # Extract readings
        temp_readings = [s.value for s in sensor_data.filter(sensor_type='temperature')]
        humidity_readings = [s.value for s in sensor_data.filter(sensor_type='humidity')]
        weight_readings = [s.value for s in sensor_data.filter(sensor_type='weight')]
        sound_readings = [s.value for s in sensor_data.filter(sensor_type='sound')]
        
        # Calculate statistics
        avg_temp = statistics.mean(temp_readings) if temp_readings else 35
        avg_humidity = statistics.mean(humidity_readings) if humidity_readings else 70
        temp_std = statistics.stdev(temp_readings) if len(temp_readings) > 1 else 0
        avg_activity = statistics.mean(sound_readings) if sound_readings else 65
        
        # Calculate weight trend
        weight_trend = DiseaseDetectorService._calculate_weight_trend(weight_readings)
        
        # Prepare sensor data for prediction
        sensor_data_dict = {
            'avg_temp': avg_temp,
            'temp_std': temp_std,
            'avg_humidity': avg_humidity,
            'weight_trend': weight_trend,
            'avg_activity': avg_activity,
        }
        
        # Get disease predictions
        disease_predictions = DiseasePredictionModel.predict_all_diseases(sensor_data_dict)
        
        # Filter high-risk diseases
        high_risk_diseases = {
            name: data for name, data in disease_predictions.items()
            if data['risk_level'] in ['medium', 'high']
        }
        
        return {
            'hive_id': hive.id,
            'hive_name': hive.hive_id,
            'analysis_period_hours': hours,
            'all_predictions': disease_predictions,
            'high_risk_diseases': high_risk_diseases,
            'high_risk_count': len(high_risk_diseases),
            'alert_status': 'HIGH ALERT' if high_risk_diseases else 'NORMAL',
            'sensor_summary': {
                'avg_temperature': round(avg_temp, 2),
                'avg_humidity': round(avg_humidity, 2),
                'avg_activity': round(avg_activity, 2),
                'weight_trend_kg_per_day': round(weight_trend, 4),
            },
        }
    
    @staticmethod
    def get_disease_risk_timeline(hive_id: int, days: int = 7) -> Dict:
        """Get disease risk timeline over past days"""
        try:
            hive = Hive.objects.get(id=hive_id)
        except Hive.DoesNotExist:
            return {'error': 'Hive not found'}
        
        risk_timeline = []
        
        for i in range(days, 0, -1):
            start_time = timezone.now() - timedelta(days=i+1)
            end_time = timezone.now() - timedelta(days=i)
            
            sensor_data = SensorData.objects.filter(
                hive=hive,
                timestamp__gte=start_time,
                timestamp__lt=end_time
            )
            
            if not sensor_data.exists():
                continue
            
            # Calculate stats for the day
            temp_readings = [s.value for s in sensor_data.filter(sensor_type='temperature')]
            humidity_readings = [s.value for s in sensor_data.filter(sensor_type='humidity')]
            sound_readings = [s.value for s in sensor_data.filter(sensor_type='sound')]
            weight_readings = [s.value for s in sensor_data.filter(sensor_type='weight')]
            
            avg_temp = statistics.mean(temp_readings) if temp_readings else 35
            avg_humidity = statistics.mean(humidity_readings) if humidity_readings else 70
            avg_activity = statistics.mean(sound_readings) if sound_readings else 65
            weight_trend = DiseaseDetectorService._calculate_weight_trend(weight_readings)
            
            sensor_data_dict = {
                'avg_temp': avg_temp,
                'temp_std': statistics.stdev(temp_readings) if len(temp_readings) > 1 else 0,
                'avg_humidity': avg_humidity,
                'weight_trend': weight_trend,
                'avg_activity': avg_activity,
            }
            
            predictions = DiseasePredictionModel.predict_all_diseases(sensor_data_dict)
            
            # Calculate overall risk
            avg_risk = sum(
                (0.25 if d['risk_level'] == 'high' else 
                 0.15 if d['risk_level'] == 'medium' else 0.05)
                for d in predictions.values()
            ) / len(predictions) * 100 if predictions else 0
            
            risk_timeline.append({
                'date': start_time.date().isoformat(),
                'overall_risk_percent': round(avg_risk, 2),
                'top_risks': [
                    k for k, v in predictions.items()
                    if v['risk_level'] in ['medium', 'high']
                ][:3],
            })
        
        return {
            'hive_id': hive.id,
            'timeline_days': days,
            'risk_timeline': risk_timeline,
            'current_risk_status': risk_timeline[-1]['overall_risk_percent'] if risk_timeline else 0,
        }
    
    @staticmethod
    def _calculate_weight_trend(weight_readings: List[float]) -> float:
        """Calculate weight trend (kg/day)"""
        if not weight_readings or len(weight_readings) < 2:
            return 0.0
        
        # Assume readings are roughly evenly spaced
        total_change = weight_readings[-1] - weight_readings[0]
        days_passed = len(weight_readings) / 24  # Assume 24 readings per day
        
        return total_change / max(1, days_passed)
