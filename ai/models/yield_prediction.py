"""Yield Prediction Model - Predict honey yield from sensor and historical data"""
from typing import Dict, List
import statistics


class YieldPredictionModel:
    """Predict honey yield based on hive conditions"""
    
    def __init__(self):
        # Average honey yield per hive: 30-60 kg per season
        self.base_yield = 45  # kg
        self.season_length_days = 180  # typical active season
    
    def predict_seasonal_yield(self, 
                              days_into_season: int,
                              current_weight: float,
                              weight_trend: float,
                              health_score: float) -> Dict:
        """Predict seasonal honey yield"""
        
        # Extrapolate based on current weight gain and remaining time
        days_remaining = max(1, self.season_length_days - days_into_season)
        
        if days_into_season > 0:
            # kg/day * remaining days
            projected_additional_yield = weight_trend * days_remaining
            total_projected_yield = current_weight + projected_additional_yield
        else:
            total_projected_yield = self.base_yield
        
        # Adjust based on health score (lower health = lower yield)
        health_multiplier = health_score / 100.0
        adjusted_yield = total_projected_yield * health_multiplier
        
        # Ensure reasonable bounds
        adjusted_yield = min(80, max(5, adjusted_yield))
        
        confidence = self._calculate_confidence(days_into_season)
        
        return {
            'projected_yield_kg': round(adjusted_yield, 2),
            'current_weight_kg': round(current_weight, 2),
            'daily_growth_kg': round(weight_trend, 4),
            'days_into_season': days_into_season,
            'days_remaining': days_remaining,
            'health_adjusted': round(adjusted_yield, 2),
            'confidence_percent': confidence,
            'yield_quality': self._classify_yield_quality(adjusted_yield),
        }
    
    def predict_weekly_yield(self, weight_readings_past_week: List[float]) -> Dict:
        """Predict weekly honey accumulation"""
        if not weight_readings_past_week or len(weight_readings_past_week) < 2:
            return {'weekly_yield': 0, 'trend': 'insufficient_data'}
        
        # Calculate weight gain over the week
        weekly_gain = weight_readings_past_week[-1] - weight_readings_past_week[0]
        
        # Calculate daily average
        daily_avg = weekly_gain / 7 if len(weight_readings_past_week) == 8 else 0
        
        return {
            'weekly_yield_kg': round(weekly_gain, 2),
            'daily_average_kg': round(daily_avg, 4),
            'trend': 'increasing' if weekly_gain > 0 else 'decreasing' if weekly_gain < 0 else 'stable',
            'growth_potential': self._assess_growth_potential(weekly_gain),
        }
    
    def predict_optimal_harvest_time(self,
                                     current_weight: float,
                                     weight_trend: float,
                                     health_score: float,
                                     days_into_season: int) -> Dict:
        """Predict optimal harvest timing"""
        
        # Ideal harvest weight: 50-60 kg
        ideal_harvest_min = 50
        ideal_harvest_max = 60
        
        if current_weight >= ideal_harvest_max:
            harvest_readiness = 'ready'
            days_to_harvest = 0
        else:
            # Calculate days needed to reach ideal harvest weight
            weight_needed = ideal_harvest_min - current_weight
            if weight_trend > 0:
                days_to_harvest = int(weight_needed / weight_trend) if weight_trend > 0 else 30
            else:
                days_to_harvest = 30
        
        # Consider season timing
        season_progress = (days_into_season / self.season_length_days) * 100
        
        return {
            'harvest_readiness': harvest_readiness,
            'current_weight_kg': round(current_weight, 2),
            'target_weight_kg': round(ideal_harvest_max, 2),
            'days_to_harvest': max(0, days_to_harvest),
            'season_progress_percent': round(season_progress, 2),
            'recommended_action': self._get_harvest_recommendation(
                current_weight, harvest_readiness, season_progress
            ),
        }
    
    def predict_nectar_flow_period(self, historical_data: List[Dict]) -> Dict:
        """Predict peak nectar flow periods"""
        if not historical_data or len(historical_data) < 10:
            return {'prediction': 'insufficient_data'}
        
        # Analyze weight gains over time periods
        daily_gains = []
        for i in range(1, len(historical_data)):
            gain = historical_data[i].get('weight', 0) - historical_data[i-1].get('weight', 0)
            daily_gains.append(gain)
        
        if not daily_gains:
            return {'prediction': 'no_data'}
        
        avg_gain = statistics.mean(daily_gains)
        max_gain = max(daily_gains)
        
        return {
            'average_daily_gain_kg': round(avg_gain, 4),
            'peak_daily_gain_kg': round(max_gain, 4),
            'flow_intensity': self._classify_nectar_flow(avg_gain),
        }
    
    @staticmethod
    def _calculate_confidence(days_into_season: int) -> int:
        """Calculate prediction confidence based on data availability"""
        if days_into_season < 10:
            return 30
        elif days_into_season < 30:
            return 50
        elif days_into_season < 60:
            return 70
        else:
            return 85
    
    @staticmethod
    def _classify_yield_quality(yield_kg: float) -> str:
        """Classify yield quality"""
        if yield_kg >= 60:
            return 'excellent'
        elif yield_kg >= 45:
            return 'good'
        elif yield_kg >= 30:
            return 'fair'
        elif yield_kg >= 15:
            return 'poor'
        else:
            return 'very_poor'
    
    @staticmethod
    def _assess_growth_potential(weekly_gain: float) -> str:
        """Assess growth potential"""
        if weekly_gain > 3:
            return 'high'
        elif weekly_gain > 1:
            return 'moderate'
        elif weekly_gain > 0:
            return 'low'
        else:
            return 'declining'
    
    @staticmethod
    def _classify_nectar_flow(daily_gain: float) -> str:
        """Classify nectar flow intensity"""
        if daily_gain >= 2.0:
            return 'strong_flow'
        elif daily_gain >= 1.0:
            return 'moderate_flow'
        elif daily_gain >= 0.2:
            return 'light_flow'
        else:
            return 'no_flow'
    
    @staticmethod
    def _get_harvest_recommendation(weight: float, readiness: str, season_progress: float) -> str:
        """Get harvest recommendation"""
        if readiness == 'ready':
            return 'Harvest now - hive is at optimal weight'
        elif season_progress > 80:
            return 'Consider harvesting soon - season is ending'
        elif season_progress > 60 and weight > 35:
            return 'Prepare for harvest - mid-to-late season'
        else:
            return 'Continue monitoring - early in season'
