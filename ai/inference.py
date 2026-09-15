"""Inference Engine - Main AI inference and recommendation generation"""
from typing import Dict
from .services.health_analyzer import HealthAnalyzerService
from .services.disease_detector import DiseaseDetectorService
from .services.yield_predictor import YieldPredictorService
from .services.recommendation_engine import RecommendationEngine
from .preprocessing.sensor_preprocessing import SensorPreprocessor


class InferenceEngine:
    """Main AI inference engine for honey chain"""
    
    @staticmethod
    def analyze_hive(hive_id: int) -> Dict:
        """Comprehensive hive analysis"""
        return {
            'hive_id': hive_id,
            'health': HealthAnalyzerService.analyze_hive_health(hive_id),
            'diseases': DiseaseDetectorService.detect_diseases(hive_id),
            'yield': YieldPredictorService.predict_yield(hive_id),
        }
    
    @staticmethod
    def get_recommendations(hive_id: int) -> Dict:
        """Get AI-powered recommendations for a hive"""
        return RecommendationEngine.generate_hive_recommendations(hive_id)
    
    @staticmethod
    def quick_health_check(hive_id: int) -> Dict:
        """Quick hive health check"""
        health = HealthAnalyzerService.analyze_hive_health(hive_id, hours=24)
        
        if 'error' in health:
            return health
        
        return {
            'hive_id': hive_id,
            'health_score': health.get('overall_health_score'),
            'status': health.get('status'),
            'quick_tips': RecommendationEngine.get_quick_recommendations(hive_id),
        }
    
    @staticmethod
    def validate_and_preprocess(sensor_data: Dict) -> Dict:
        """Validate and preprocess sensor data"""
        processed = {}
        
        for sensor_type, readings in sensor_data.items():
            if not readings:
                continue
            
            # Clean readings
            cleaned = SensorPreprocessor.clean_sensor_readings(readings)
            
            # Validate
            if not cleaned:
                processed[sensor_type] = {
                    'valid': False,
                    'error': 'All readings filtered as invalid'
                }
                continue
            
            # Prepare features
            processed[sensor_type] = {
                'valid': True,
                'cleaned_readings': cleaned,
                'features': SensorPreprocessor.prepare_features({sensor_type: cleaned})
            }
        
        return processed
