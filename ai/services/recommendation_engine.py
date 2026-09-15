"""Recommendation Engine - Provides actionable recommendations"""
from typing import Dict, List
from .health_analyzer import HealthAnalyzerService
from .disease_detector import DiseaseDetectorService
from .yield_predictor import YieldPredictorService


class RecommendationEngine:
    """Engine for generating actionable beekeeping recommendations"""
    
    @staticmethod
    def generate_hive_recommendations(hive_id: int) -> Dict:
        """Generate comprehensive recommendations for a hive"""
        
        # Get all analysis data
        health_analysis = HealthAnalyzerService.analyze_hive_health(hive_id, hours=48)
        disease_analysis = DiseaseDetectorService.detect_diseases(hive_id, hours=48)
        yield_prediction = YieldPredictorService.predict_yield(hive_id)
        
        if 'error' in health_analysis:
            return {'error': 'Unable to generate recommendations - insufficient data'}
        
        recommendations = {
            'hive_id': hive_id,
            'generated_at': __import__('django.utils.timezone', fromlist=['now']).now().isoformat(),
            'priority_actions': [],
            'seasonal_tasks': [],
            'monitoring_focus': [],
            'resources': [],
        }
        
        # Generate priority actions based on analysis
        overall_health = health_analysis.get('overall_health_score', 50)
        
        if overall_health < 40:
            recommendations['priority_actions'].append({
                'priority': 'CRITICAL',
                'action': 'Conduct immediate physical inspection',
                'reason': 'Hive health score critically low',
                'timeframe': 'Within 24 hours',
            })
        
        # Disease-based recommendations
        if disease_analysis.get('high_risk_diseases'):
            high_risk = disease_analysis['high_risk_diseases']
            for disease, data in high_risk.items():
                recommendations['priority_actions'].append({
                    'priority': 'HIGH' if data['risk_level'] == 'high' else 'MEDIUM',
                    'action': f'Monitor for {disease.replace("_", " ").title()}',
                    'reason': f'Risk level: {data["risk_level"]} ({data["probability"]}%)',
                    'recommendations': data.get('recommendations', []),
                })
        
        # Harvest-based recommendations
        if yield_prediction.get('prediction'):
            harvest_pred = yield_prediction['prediction']
            harvest_readiness = harvest_pred.get('harvest_readiness', 'unknown')
            
            if harvest_readiness == 'ready':
                recommendations['seasonal_tasks'].append({
                    'task': 'Prepare for honey harvest',
                    'timing': 'Immediately',
                    'details': f"Hive at optimal weight: {harvest_pred.get('current_weight_kg', 0)}kg",
                })
            else:
                days_to_harvest = harvest_pred.get('days_to_harvest', 0)
                recommendations['seasonal_tasks'].append({
                    'task': 'Monitor for harvest readiness',
                    'timing': f"In approximately {days_to_harvest} days",
                    'details': f"Current weight: {harvest_pred.get('current_weight_kg', 0)}kg",
                })
        
        # Temperature and humidity recommendations
        params = health_analysis.get('parameters', {})
        
        temp_data = params.get('temperature', {})
        if temp_data.get('status') == 'critical':
            recommendations['monitoring_focus'].append({
                'parameter': 'Temperature',
                'current_avg': temp_data.get('average'),
                'ideal_range': temp_data.get('ideal_range'),
                'action': 'Adjust hive ventilation and placement',
            })
        
        humidity_data = params.get('humidity', {})
        if humidity_data.get('status') == 'critical':
            recommendations['monitoring_focus'].append({
                'parameter': 'Humidity',
                'current_avg': humidity_data.get('average'),
                'ideal_range': humidity_data.get('ideal_range'),
                'action': 'Improve ventilation or add moisture barriers',
            })
        
        # General resources
        recommendations['resources'] = [
            {
                'title': 'Hive Health Monitoring',
                'description': 'Regular sensor monitoring helps detect issues early',
                'action': 'Check sensor data daily',
            },
            {
                'title': 'Varroa Mite Management',
                'description': 'Most common threat to hive health',
                'action': 'Use integrated pest management strategies',
            },
            {
                'title': 'Seasonal Management',
                'description': 'Different seasons require different approaches',
                'action': 'Adjust management based on season',
            },
        ]
        
        return recommendations
    
    @staticmethod
    def get_quick_recommendations(hive_id: int) -> List[str]:
        """Get quick, actionable recommendations"""
        
        health = HealthAnalyzerService.analyze_hive_health(hive_id, hours=24)
        diseases = DiseaseDetectorService.detect_diseases(hive_id, hours=24)
        
        recommendations = []
        
        # Health-based
        if health.get('overall_health_score', 100) < 50:
            recommendations.append('⚠️ Hive health is compromised - inspect immediately')
        
        # Disease-based
        if diseases.get('high_risk_count', 0) > 0:
            high_risk = list(diseases.get('high_risk_diseases', {}).keys())[:1]
            if high_risk:
                disease_name = high_risk[0].replace('_', ' ').title()
                recommendations.append(f'🦠 High risk of {disease_name} - monitor closely')
        
        # Activity-based
        activity = health.get('parameters', {}).get('activity', {})
        if activity.get('activity_level') == 'low':
            recommendations.append('🐝 Low hive activity detected - check for issues')
        
        # Default
        if not recommendations:
            recommendations.append('✅ Hive appears to be in good condition')
        
        return recommendations
    
    @staticmethod
    def get_seasonal_recommendations(season: str) -> Dict:
        """Get recommendations based on season"""
        
        seasonal_guides = {
            'spring': {
                'tasks': [
                    'Provide protein supplements as brood rearing increases',
                    'Monitor for varroa mites',
                    'Add honey supers for nectar storage',
                    'Prepare for swarm season',
                    'Check honey stores and replace if needed',
                ],
                'monitoring': ['Brood pattern', 'Disease signs', 'Swarming behavior'],
                'focus': 'Colony buildup and preparation for honey flow',
            },
            'summer': {
                'tasks': [
                    'Maintain adequate ventilation',
                    'Manage honey supers',
                    'Monitor disease and pests',
                    'Keep water source available',
                    'Avoid unnecessary hive disturbances',
                ],
                'monitoring': ['Nectar flow', 'Colony strength', 'Disease'],
                'focus': 'Maximize honey production',
            },
            'fall': {
                'tasks': [
                    'Harvest honey at peak',
                    'Treat for varroa mites',
                    'Provide winter food stores',
                    'Consolidate hives if needed',
                    'Prepare for winter',
                ],
                'monitoring': ['Food stores', 'Hive strength', 'Pest levels'],
                'focus': 'Prepare colony for winter dormancy',
            },
            'winter': {
                'tasks': [
                    'Minimize hive disturbance',
                    'Monitor food consumption',
                    'Ensure proper ventilation',
                    'Protect from extreme weather',
                    'Plan for spring season',
                ],
                'monitoring': ['Cluster size', 'Food consumption', 'Pest activity'],
                'focus': 'Ensure colony survival through dormancy',
            },
        }
        
        return seasonal_guides.get(season, {'error': 'Unknown season'})
