"""Hive Health Analysis Model - AI-powered health assessment"""
from typing import Dict, List
import statistics


class HiveHealthAnalyzer:
    """Analyze hive health from sensor data"""
    
    def __init__(self):
        self.health_indicators = {
            'temperature_stability': 0.0,
            'humidity_stability': 0.0,
            'weight_trend': 0.0,
            'activity_level': 0.0,
            'overall_score': 0.0,
        }
    
    def analyze_temperature_trend(self, readings: List[float]) -> Dict:
        """Analyze temperature trend"""
        if not readings:
            return {'stability': 0, 'avg_temp': 0, 'trend': 'unknown'}
        
        avg = statistics.mean(readings)
        std_dev = statistics.stdev(readings) if len(readings) > 1 else 0
        
        # Ideal temperature for bees: 32-37°C
        ideal_min, ideal_max = 32, 37
        stability = max(0, 100 - (std_dev * 10))
        
        return {
            'average': round(avg, 2),
            'std_dev': round(std_dev, 2),
            'stability': round(stability, 2),
            'ideal_range': f'{ideal_min}-{ideal_max}°C',
            'status': self._get_status(avg, ideal_min, ideal_max),
        }
    
    def analyze_humidity_trend(self, readings: List[float]) -> Dict:
        """Analyze humidity trend"""
        if not readings:
            return {'stability': 0, 'avg_humidity': 0, 'trend': 'unknown'}
        
        avg = statistics.mean(readings)
        std_dev = statistics.stdev(readings) if len(readings) > 1 else 0
        
        # Ideal humidity: 60-80%
        ideal_min, ideal_max = 60, 80
        stability = max(0, 100 - (std_dev * 5))
        
        return {
            'average': round(avg, 2),
            'std_dev': round(std_dev, 2),
            'stability': round(stability, 2),
            'ideal_range': f'{ideal_min}-{ideal_max}%',
            'status': self._get_status(avg, ideal_min, ideal_max),
        }
    
    def analyze_weight_trend(self, readings: List[float]) -> Dict:
        """Analyze weight trend (honey accumulation)"""
        if not readings:
            return {'trend': 'unknown', 'growth_rate': 0}
        
        if len(readings) < 2:
            return {
                'current_weight': readings[0],
                'trend': 'insufficient_data',
                'growth_rate': 0,
            }
        
        # Calculate trend
        growth_rates = []
        for i in range(1, len(readings)):
            growth = readings[i] - readings[i-1]
            growth_rates.append(growth)
        
        avg_growth = statistics.mean(growth_rates)
        
        return {
            'current_weight': round(readings[-1], 2),
            'initial_weight': round(readings[0], 2),
            'total_gain': round(readings[-1] - readings[0], 2),
            'average_growth_rate': round(avg_growth, 4),
            'trend': 'positive' if avg_growth > 0 else 'negative' if avg_growth < 0 else 'stable',
        }
    
    def analyze_activity_level(self, sound_readings: List[float]) -> Dict:
        """Analyze hive activity level"""
        if not sound_readings:
            return {'activity': 'unknown', 'level': 0}
        
        avg_activity = statistics.mean(sound_readings)
        
        return {
            'average_activity': round(avg_activity, 2),
            'min_activity': round(min(sound_readings), 2),
            'max_activity': round(max(sound_readings), 2),
            'activity_level': self._classify_activity(avg_activity),
        }
    
    def calculate_overall_health_score(self, 
                                       temperature_stability: float,
                                       humidity_stability: float,
                                       weight_trend: float,
                                       activity_level: float) -> float:
        """Calculate overall health score (0-100)"""
        weights = {
            'temperature': 0.3,
            'humidity': 0.3,
            'weight': 0.2,
            'activity': 0.2,
        }
        
        score = (
            (temperature_stability * weights['temperature']) +
            (humidity_stability * weights['humidity']) +
            (weight_trend * weights['weight']) +
            (activity_level * weights['activity'])
        )
        
        return round(min(100, max(0, score)), 2)
    
    @staticmethod
    def _get_status(value: float, min_val: float, max_val: float) -> str:
        """Get status based on value and range"""
        if min_val <= value <= max_val:
            return 'optimal'
        elif min_val - 5 <= value <= max_val + 5:
            return 'warning'
        else:
            return 'critical'
    
    @staticmethod
    def _classify_activity(avg_activity: float) -> str:
        """Classify activity level"""
        if avg_activity < 50:
            return 'low'
        elif 50 <= avg_activity < 70:
            return 'moderate'
        else:
            return 'high'
