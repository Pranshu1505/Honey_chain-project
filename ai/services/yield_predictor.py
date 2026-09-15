"""Yield Predictor Service - Predicts honey yield"""
from typing import Dict, List
from apps.sensor.models import SensorData
from apps.hive.models import Hive
from apps.harvest.models import Harvest
from django.utils import timezone
from datetime import timedelta
from .yield_prediction import YieldPredictionModel
import statistics


class YieldPredictorService:
    """Service for honey yield prediction"""
    
    @staticmethod
    def predict_yield(hive_id: int, season_start_date=None) -> Dict:
        """Predict honey yield for current season"""
        try:
            hive = Hive.objects.get(id=hive_id)
        except Hive.DoesNotExist:
            return {'error': 'Hive not found'}
        
        # Determine season start if not provided
        if not season_start_date:
            # Assume season starts Jan 1
            today = timezone.now().date()
            season_start_date = timezone.datetime(today.year, 1, 1).date()
        
        # Calculate days into season
        days_into_season = (timezone.now().date() - season_start_date).days
        
        # Get recent weight readings
        recent_data = SensorData.objects.filter(
            hive=hive,
            sensor_type='weight'
        ).order_by('-timestamp')[:100]  # Last 100 readings
        
        if not recent_data.exists():
            return {'error': 'No weight data available'}
        
        weight_readings = [s.value for s in recent_data.order_by('timestamp')]
        current_weight = weight_readings[-1] if weight_readings else 0
        
        # Calculate weight trend
        weight_trend = YieldPredictorService._calculate_daily_trend(weight_readings)
        
        # Get health score
        health_score = YieldPredictorService._estimate_health_score(hive_id)
        
        # Predict seasonal yield
        predictor = YieldPredictionModel()
        yield_prediction = predictor.predict_seasonal_yield(
            days_into_season,
            current_weight,
            weight_trend,
            health_score
        )
        
        # Add historical context
        historical_harvests = Harvest.objects.filter(hive=hive).order_by('-harvest_date')[:5]
        avg_historical_yield = (
            statistics.mean([h.quantity for h in historical_harvests])
            if historical_harvests.exists()
            else None
        )
        
        return {
            'hive_id': hive.id,
            'hive_name': hive.hive_id,
            'season_start_date': season_start_date.isoformat(),
            'prediction': yield_prediction,
            'health_score': health_score,
            'weight_trend_kg_per_day': round(weight_trend, 4),
            'average_historical_yield_kg': round(avg_historical_yield, 2) if avg_historical_yield else None,
            'previous_harvests': [
                {
                    'date': h.harvest_date.isoformat(),
                    'quantity_kg': h.quantity,
                    'honey_type': h.honey_type,
                }
                for h in historical_harvests
            ],
        }
    
    @staticmethod
    def predict_harvest_time(hive_id: int, season_start_date=None) -> Dict:
        """Predict optimal harvest time"""
        try:
            hive = Hive.objects.get(id=hive_id)
        except Hive.DoesNotExist:
            return {'error': 'Hive not found'}
        
        if not season_start_date:
            today = timezone.now().date()
            season_start_date = timezone.datetime(today.year, 1, 1).date()
        
        days_into_season = (timezone.now().date() - season_start_date).days
        
        # Get weight data
        recent_data = SensorData.objects.filter(
            hive=hive,
            sensor_type='weight'
        ).order_by('-timestamp')[:100]
        
        if not recent_data.exists():
            return {'error': 'No weight data available'}
        
        weight_readings = [s.value for s in recent_data.order_by('timestamp')]
        current_weight = weight_readings[-1]
        weight_trend = YieldPredictorService._calculate_daily_trend(weight_readings)
        health_score = YieldPredictorService._estimate_health_score(hive_id)
        
        # Predict harvest time
        predictor = YieldPredictionModel()
        harvest_prediction = predictor.predict_optimal_harvest_time(
            current_weight,
            weight_trend,
            health_score,
            days_into_season
        )
        
        return {
            'hive_id': hive.id,
            'hive_name': hive.hive_id,
            'harvest_prediction': harvest_prediction,
            'current_date': timezone.now().date().isoformat(),
        }
    
    @staticmethod
    def predict_weekly_yield(hive_id: int) -> Dict:
        """Predict this week's honey yield"""
        try:
            hive = Hive.objects.get(id=hive_id)
        except Hive.DoesNotExist:
            return {'error': 'Hive not found'}
        
        # Get last 7 days of weight data
        week_ago = timezone.now() - timedelta(days=7)
        week_data = SensorData.objects.filter(
            hive=hive,
            sensor_type='weight',
            timestamp__gte=week_ago
        ).order_by('timestamp')
        
        if week_data.count() < 2:
            return {'error': 'Insufficient data for weekly prediction'}
        
        weight_readings = [s.value for s in week_data]
        
        predictor = YieldPredictionModel()
        weekly_prediction = predictor.predict_weekly_yield(weight_readings)
        
        return {
            'hive_id': hive.id,
            'hive_name': hive.hive_id,
            'week_start': (timezone.now() - timedelta(days=7)).date().isoformat(),
            'week_end': timezone.now().date().isoformat(),
            'prediction': weekly_prediction,
            'readings_available': len(weight_readings),
        }
    
    @staticmethod
    def _calculate_daily_trend(weight_readings: List[float]) -> float:
        """Calculate daily weight trend"""
        if not weight_readings or len(weight_readings) < 2:
            return 0.0
        
        # Calculate average change between consecutive readings
        changes = [weight_readings[i+1] - weight_readings[i] for i in range(len(weight_readings)-1)]
        avg_change = statistics.mean(changes)
        
        # Assume readings are taken hourly or 2-3 times daily
        # Extrapolate to daily rate
        readings_per_day = 24 if len(weight_readings) > 7 else 3
        daily_trend = avg_change * readings_per_day
        
        return daily_trend
    
    @staticmethod
    def _estimate_health_score(hive_id: int) -> float:
        """Estimate hive health score from recent data"""
        try:
            from .health_analyzer import HealthAnalyzerService
            health_data = HealthAnalyzerService.analyze_hive_health(hive_id, hours=24)
            return health_data.get('overall_health_score', 50)
        except:
            return 50.0  # Default neutral score
