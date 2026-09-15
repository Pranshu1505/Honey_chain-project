"""Disease Prediction Model - Predict hive diseases from sensor data"""
from typing import Dict, List, Tuple
import math


class DiseasePredictionModel:
    """ML-based disease prediction for beehives"""
    
    # Disease indicators
    DISEASES = {
        'varroa_mite': {
            'indicators': ['low_activity', 'weight_loss', 'temperature_instability'],
            'weight_threshold': -0.05,  # kg/day loss
            'activity_threshold': 45,  # dB
        },
        'nosema': {
            'indicators': ['low_activity', 'humidity_imbalance', 'weight_loss'],
            'humidity_min': 40,
            'humidity_max': 90,
        },
        'european_foulbrood': {
            'indicators': ['temperature_instability', 'humidity_high', 'low_activity'],
            'temp_threshold': 2.0,  # std dev
            'humidity_threshold': 80,
        },
        'chalk_brood': {
            'indicators': ['humidity_high', 'temperature_low'],
            'humidity_threshold': 85,
            'temp_threshold': 30,
        },
        'small_hive_beetle': {
            'indicators': ['weight_loss', 'low_activity', 'temperature_low'],
            'weight_threshold': -0.1,
        },
    }
    
    @staticmethod
    def predict_varroa_mite(weight_trend: float, avg_activity: float) -> Tuple[float, str]:
        """Predict varroa mite infestation probability"""
        probability = 0.0
        
        # Weight loss indicator
        if weight_trend < -0.05:
            probability += 30
        
        # Low activity indicator
        if avg_activity < 45:
            probability += 25
        
        # Cap at 100
        probability = min(100, max(0, probability))
        
        risk_level = DiseasePredictionModel._classify_risk(probability)
        return probability, risk_level
    
    @staticmethod
    def predict_nosema(weight_trend: float, avg_humidity: float, avg_activity: float) -> Tuple[float, str]:
        """Predict nosema disease probability"""
        probability = 0.0
        
        # Weight loss indicator
        if weight_trend < -0.03:
            probability += 25
        
        # Humidity imbalance (too high or too low)
        if avg_humidity < 40 or avg_humidity > 90:
            probability += 25
        
        # Low activity
        if avg_activity < 50:
            probability += 20
        
        probability = min(100, max(0, probability))
        risk_level = DiseasePredictionModel._classify_risk(probability)
        return probability, risk_level
    
    @staticmethod
    def predict_foulbrood(temp_std: float, avg_humidity: float, avg_activity: float) -> Tuple[float, str]:
        """Predict European foulbrood probability"""
        probability = 0.0
        
        # Temperature instability
        if temp_std > 2.0:
            probability += 20
        
        # High humidity
        if avg_humidity > 80:
            probability += 25
        
        # Low activity
        if avg_activity < 45:
            probability += 20
        
        probability = min(100, max(0, probability))
        risk_level = DiseasePredictionModel._classify_risk(probability)
        return probability, risk_level
    
    @staticmethod
    def predict_chalk_brood(avg_humidity: float, avg_temp: float) -> Tuple[float, str]:
        """Predict chalk brood probability"""
        probability = 0.0
        
        # High humidity
        if avg_humidity > 85:
            probability += 35
        
        # Low temperature
        if avg_temp < 30:
            probability += 20
        
        probability = min(100, max(0, probability))
        risk_level = DiseasePredictionModel._classify_risk(probability)
        return probability, risk_level
    
    @staticmethod
    def predict_small_hive_beetle(weight_trend: float, avg_activity: float, avg_temp: float) -> Tuple[float, str]:
        """Predict small hive beetle infestation probability"""
        probability = 0.0
        
        # Weight loss
        if weight_trend < -0.1:
            probability += 30
        
        # Low activity
        if avg_activity < 40:
            probability += 20
        
        # Low temperature (beetles prefer cooler areas)
        if avg_temp < 32:
            probability += 15
        
        probability = min(100, max(0, probability))
        risk_level = DiseasePredictionModel._classify_risk(probability)
        return probability, risk_level
    
    @staticmethod
    def predict_all_diseases(sensor_data: Dict) -> Dict[str, Dict]:
        """Predict all diseases at once"""
        predictions = {}
        
        weight_trend = sensor_data.get('weight_trend', 0)
        avg_activity = sensor_data.get('avg_activity', 60)
        avg_temp = sensor_data.get('avg_temp', 35)
        avg_humidity = sensor_data.get('avg_humidity', 70)
        temp_std = sensor_data.get('temp_std', 1.0)
        
        # Varroa mite
        prob, risk = DiseasePredictionModel.predict_varroa_mite(weight_trend, avg_activity)
        predictions['varroa_mite'] = {
            'probability': round(prob, 2),
            'risk_level': risk,
            'recommendations': ['Inspect for red mites', 'Check adult bee mortality']
        }
        
        # Nosema
        prob, risk = DiseasePredictionModel.predict_nosema(weight_trend, avg_humidity, avg_activity)
        predictions['nosema'] = {
            'probability': round(prob, 2),
            'risk_level': risk,
            'recommendations': ['Monitor bee dysentery', 'Check for nosema spores']
        }
        
        # Foulbrood
        prob, risk = DiseasePredictionModel.predict_foulbrood(temp_std, avg_humidity, avg_activity)
        predictions['foulbrood'] = {
            'probability': round(prob, 2),
            'risk_level': risk,
            'recommendations': ['Check larvae for disease', 'Monitor brood pattern']
        }
        
        # Chalk brood
        prob, risk = DiseasePredictionModel.predict_chalk_brood(avg_humidity, avg_temp)
        predictions['chalk_brood'] = {
            'probability': round(prob, 2),
            'risk_level': risk,
            'recommendations': ['Reduce hive humidity', 'Improve ventilation']
        }
        
        # Small hive beetle
        prob, risk = DiseasePredictionModel.predict_small_hive_beetle(weight_trend, avg_activity, avg_temp)
        predictions['small_hive_beetle'] = {
            'probability': round(prob, 2),
            'risk_level': risk,
            'recommendations': ['Check bottom board traps', 'Monitor for beetle damage']
        }
        
        return predictions
    
    @staticmethod
    def _classify_risk(probability: float) -> str:
        """Classify risk level based on probability"""
        if probability < 25:
            return 'low'
        elif 25 <= probability < 60:
            return 'medium'
        else:
            return 'high'
