"""Health Analyzer Service - Provides hive health analysis"""
from typing import Dict, List
from apps.sensor.models import SensorData
from apps.hive.models import Hive
from django.utils import timezone
from datetime import timedelta
from .hive_health import HiveHealthAnalyzer


class HealthAnalyzerService:
    """Service for analyzing hive health"""
    
    @staticmethod
    def analyze_hive_health(hive_id: int, hours: int = 24) -> Dict:
        """Comprehensive hive health analysis"""
        try:
            hive = Hive.objects.get(id=hive_id)
        except Hive.DoesNotExist:
            return {'error': 'Hive not found', 'status': 'error'}
        
        # Get recent sensor data
        time_threshold = timezone.now() - timedelta(hours=hours)
        sensor_data = SensorData.objects.filter(
            hive=hive,
            timestamp__gte=time_threshold
        ).order_by('timestamp')
        
        if not sensor_data.exists():
            return {
                'hive_id': hive.id,
                'status': 'no_data',
                'message': f'No sensor data in past {hours} hours'
            }
        
        # Extract readings by sensor type
        temp_readings = [s.value for s in sensor_data.filter(sensor_type='temperature')]
        humidity_readings = [s.value for s in sensor_data.filter(sensor_type='humidity')]
        weight_readings = [s.value for s in sensor_data.filter(sensor_type='weight')]
        sound_readings = [s.value for s in sensor_data.filter(sensor_type='sound')]
        
        analyzer = HiveHealthAnalyzer()
        
        # Analyze each parameter
        temp_analysis = analyzer.analyze_temperature_trend(temp_readings) if temp_readings else {}
        humidity_analysis = analyzer.analyze_humidity_trend(humidity_readings) if humidity_readings else {}
        weight_analysis = analyzer.analyze_weight_trend(weight_readings) if weight_readings else {}
        activity_analysis = analyzer.analyze_activity_level(sound_readings) if sound_readings else {}
        
        # Calculate stability scores (0-100)
        temp_stability = temp_analysis.get('stability', 50)
        humidity_stability = humidity_analysis.get('stability', 50)
        weight_score = HealthAnalyzerService._calculate_weight_score(weight_analysis)
        activity_score = HealthAnalyzerService._calculate_activity_score(activity_analysis)
        
        # Overall health score
        overall_score = analyzer.calculate_overall_health_score(
            temp_stability,
            humidity_stability,
            weight_score,
            activity_score
        )
        
        return {
            'hive_id': hive.id,
            'hive_name': hive.hive_id,
            'overall_health_score': overall_score,
            'status': HealthAnalyzerService._classify_health_status(overall_score),
            'analysis_period_hours': hours,
            'parameters': {
                'temperature': {
                    **temp_analysis,
                    'score': temp_stability,
                },
                'humidity': {
                    **humidity_analysis,
                    'score': humidity_stability,
                },
                'weight': {
                    **weight_analysis,
                    'score': weight_score,
                },
                'activity': {
                    **activity_analysis,
                    'score': activity_score,
                },
            },
            'readings_count': sensor_data.count(),
            'recommendations': HealthAnalyzerService._get_health_recommendations(overall_score),
        }
    
    @staticmethod
    def get_health_trend(hive_id: int, days: int = 7) -> Dict:
        """Get hive health trend over time"""
        try:
            hive = Hive.objects.get(id=hive_id)
        except Hive.DoesNotExist:
            return {'error': 'Hive not found'}
        
        # Get daily health scores
        daily_scores = []
        
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
            
            # Calculate daily score
            temp_readings = [s.value for s in sensor_data.filter(sensor_type='temperature')]
            humidity_readings = [s.value for s in sensor_data.filter(sensor_type='humidity')]
            
            analyzer = HiveHealthAnalyzer()
            temp_analysis = analyzer.analyze_temperature_trend(temp_readings) if temp_readings else {}
            humidity_analysis = analyzer.analyze_humidity_trend(humidity_readings) if humidity_readings else {}
            
            daily_score = analyzer.calculate_overall_health_score(
                temp_analysis.get('stability', 50),
                humidity_analysis.get('stability', 50),
                50,  # neutral weight score
                50,  # neutral activity score
            )
            
            daily_scores.append({
                'date': start_time.date().isoformat(),
                'score': round(daily_score, 2),
            })
        
        return {
            'hive_id': hive.id,
            'trend_days': days,
            'daily_scores': daily_scores,
            'average_score': round(sum(s['score'] for s in daily_scores) / len(daily_scores), 2) if daily_scores else 0,
            'trend': HealthAnalyzerService._calculate_trend(daily_scores),
        }
    
    @staticmethod
    def _calculate_weight_score(weight_analysis: Dict) -> float:
        """Calculate weight-based health score"""
        if not weight_analysis or not weight_analysis.get('trend'):
            return 50.0
        
        trend = weight_analysis.get('trend')
        if trend == 'positive':
            return 80.0
        elif trend == 'stable':
            return 70.0
        else:
            return 40.0
    
    @staticmethod
    def _calculate_activity_score(activity_analysis: Dict) -> float:
        """Calculate activity-based health score"""
        if not activity_analysis:
            return 50.0
        
        level = activity_analysis.get('activity_level', 'moderate')
        if level == 'high':
            return 90.0
        elif level == 'moderate':
            return 75.0
        else:
            return 40.0
    
    @staticmethod
    def _classify_health_status(score: float) -> str:
        """Classify health status"""
        if score >= 80:
            return 'excellent'
        elif score >= 60:
            return 'good'
        elif score >= 40:
            return 'fair'
        else:
            return 'poor'
    
    @staticmethod
    def _get_health_recommendations(score: float) -> List[str]:
        """Get recommendations based on health score"""
        recommendations = []
        
        if score >= 80:
            recommendations.append('Hive is in excellent condition - maintain current management')
            recommendations.append('Monitor for seasonal changes')
        elif score >= 60:
            recommendations.append('Hive health is good - monitor key parameters')
            recommendations.append('Check temperature and humidity stability')
        elif score >= 40:
            recommendations.append('Hive health needs attention')
            recommendations.append('Review environmental conditions')
            recommendations.append('Perform physical inspection')
        else:
            recommendations.append('URGENT: Hive health is critical')
            recommendations.append('Immediate action required - inspect hive')
            recommendations.append('Consider treatment options')
        
        return recommendations
    
    @staticmethod
    def _calculate_trend(daily_scores: List[Dict]) -> str:
        """Calculate trend from daily scores"""
        if len(daily_scores) < 2:
            return 'insufficient_data'
        
        first_half_avg = sum(s['score'] for s in daily_scores[:len(daily_scores)//2]) / max(1, len(daily_scores)//2)
        second_half_avg = sum(s['score'] for s in daily_scores[len(daily_scores)//2:]) / max(1, len(daily_scores) - len(daily_scores)//2)
        
        if second_half_avg > first_half_avg + 5:
            return 'improving'
        elif second_half_avg < first_half_avg - 5:
            return 'declining'
        else:
            return 'stable'
