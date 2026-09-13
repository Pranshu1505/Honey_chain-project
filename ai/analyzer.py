"""
AI Health Analysis Module
Provides health predictions, disease detection, and yield forecasting for hives
"""
from typing import Dict, List, Tuple
from datetime import datetime, timedelta
import json
import math


class HiveHealthAnalyzer:
    """Analyzes hive health based on sensor data"""
    
    HEALTH_THRESHOLDS = {
        "temperature": {"min": 28, "max": 38, "optimal": 32.5},
        "humidity": {"min": 55, "max": 75, "optimal": 65},
        "weight": {"min": 10, "max": 20, "optimal": 15},
        "sound": {"min": 60, "max": 90, "optimal": 75},
    }
    
    def __init__(self):
        self.health_history = []
    
    def analyze_readings(self, readings: List[Dict]) -> Dict:
        """Analyze sensor readings"""
        analysis = {
            "timestamp": datetime.now().isoformat(),
            "overall_health": "healthy",
            "health_score": 100,
            "metrics": {},
            "alerts": [],
            "recommendations": []
        }
        
        sensor_readings = {r["sensor_type"]: r for r in readings}
        total_score = 0
        metric_count = 0
        
        for sensor_type, thresholds in self.HEALTH_THRESHOLDS.items():
            if sensor_type in sensor_readings:
                reading = sensor_readings[sensor_type]
                value = reading["value"]
                
                # Calculate score for this metric
                if thresholds["min"] <= value <= thresholds["max"]:
                    score = 100
                    status = "good"
                else:
                    # Penalize based on deviation
                    distance_from_optimal = abs(value - thresholds["optimal"])
                    max_deviation = max(
                        thresholds["optimal"] - thresholds["min"],
                        thresholds["max"] - thresholds["optimal"]
                    )
                    score = max(50, 100 - (distance_from_optimal / max_deviation * 50))
                    status = "warning" if score > 75 else "critical"
                
                analysis["metrics"][sensor_type] = {
                    "value": value,
                    "unit": reading["unit"],
                    "score": round(score, 2),
                    "status": status,
                    "optimal_range": f"{thresholds['min']}-{thresholds['max']}"
                }
                
                total_score += score
                metric_count += 1
                
                # Add alerts
                if status == "critical":
                    analysis["alerts"].append({
                        "sensor": sensor_type,
                        "value": value,
                        "message": self._get_alert_message(sensor_type, value, thresholds)
                    })
        
        # Calculate overall health score
        if metric_count > 0:
            analysis["health_score"] = round(total_score / metric_count, 2)
        
        # Determine overall health status
        if analysis["health_score"] >= 85:
            analysis["overall_health"] = "healthy"
        elif analysis["health_score"] >= 70:
            analysis["overall_health"] = "warning"
        else:
            analysis["overall_health"] = "critical"
        
        # Add recommendations
        analysis["recommendations"] = self._get_recommendations(analysis)
        
        self.health_history.append(analysis)
        return analysis
    
    def _get_alert_message(self, sensor_type: str, value: float, thresholds: Dict) -> str:
        """Generate alert message"""
        if value < thresholds["min"]:
            direction = "low"
        else:
            direction = "high"
        
        messages = {
            "temperature": f"Hive temperature is too {direction} ({value}°C). Ensure proper ventilation.",
            "humidity": f"Humidity level is too {direction} ({value}%). Adjust hive ventilation.",
            "weight": f"Hive weight is too {direction} ({value}kg). Check for disease or starvation.",
            "sound": f"Activity level is too {direction} ({value}dB). May indicate disease or stress.",
        }
        
        return messages.get(sensor_type, f"{sensor_type} is out of range")
    
    def _get_recommendations(self, analysis: Dict) -> List[str]:
        """Generate recommendations based on analysis"""
        recommendations = []
        
        if analysis["overall_health"] == "critical":
            recommendations.append("🚨 Immediate intervention required - Schedule inspection")
        
        for sensor_type, metric in analysis["metrics"].items():
            if metric["status"] == "warning":
                if sensor_type == "temperature":
                    recommendations.append("📌 Check hive ventilation and internal temperature")
                elif sensor_type == "humidity":
                    recommendations.append("📌 Improve moisture management in hive")
                elif sensor_type == "weight":
                    recommendations.append("📌 Monitor honey production and bee population")
                elif sensor_type == "sound":
                    recommendations.append("📌 Investigate unusual bee activity")
        
        if analysis["overall_health"] == "healthy":
            recommendations.append("✅ Hive is in excellent condition")
        
        return recommendations
    
    def get_health_trend(self, hours: int = 24) -> Dict:
        """Get health trend over time"""
        if not self.health_history:
            return {"error": "No history available"}
        
        recent_history = self.health_history[-min(len(self.health_history), hours):]
        
        return {
            "period_hours": hours,
            "data_points": len(recent_history),
            "health_scores": [h["health_score"] for h in recent_history],
            "average_health": round(sum(h["health_score"] for h in recent_history) / len(recent_history), 2),
            "trend": "improving" if recent_history[-1]["health_score"] > recent_history[0]["health_score"] else "declining"
        }


class DiseasePredictor:
    """Predicts potential diseases based on sensor patterns"""
    
    DISEASE_PATTERNS = {
        "varroa_mites": {
            "symptoms": ["low_activity", "weight_loss", "temperature_fluctuation"],
            "indicators": {
                "sound": (50, 65),  # Low activity
                "weight": (8, 12),  # Weight loss
                "temperature": (30, 34)  # Fluctuating
            },
            "confidence_threshold": 0.7
        },
        "american_foulbrood": {
            "symptoms": ["bad_smell", "discolored_brood", "low_population"],
            "indicators": {
                "sound": (40, 60),  # Reduced activity
                "weight": (9, 13),  # Poor honey production
            },
            "confidence_threshold": 0.6
        },
        "colony_collapse": {
            "symptoms": ["sudden_population_drop", "hive_abandonment"],
            "indicators": {
                "sound": (30, 50),  # Very low activity
                "weight": (10, 15),  # Declining weight
            },
            "confidence_threshold": 0.75
        },
        "nosema": {
            "symptoms": ["dysentery", "reduced_lifespan", "low_brood"],
            "indicators": {
                "temperature": (25, 30),  # Lower than optimal
                "humidity": (70, 85),  # Higher humidity
            },
            "confidence_threshold": 0.65
        }
    }
    
    def predict_diseases(self, readings: List[Dict]) -> Dict:
        """Predict potential diseases"""
        predictions = {
            "timestamp": datetime.now().isoformat(),
            "diseases": [],
            "overall_risk": "low"
        }
        
        sensor_data = {r["sensor_type"]: r["value"] for r in readings}
        
        for disease_name, disease_info in self.DISEASE_PATTERNS.items():
            confidence = self._calculate_confidence(sensor_data, disease_info["indicators"])
            
            if confidence >= disease_info["confidence_threshold"]:
                predictions["diseases"].append({
                    "disease": disease_name,
                    "confidence": round(confidence * 100, 2),
                    "risk_level": self._get_risk_level(confidence),
                    "symptoms": disease_info["symptoms"],
                    "recommended_action": self._get_treatment(disease_name)
                })
        
        if predictions["diseases"]:
            max_confidence = max(d["confidence"] for d in predictions["diseases"])
            if max_confidence > 80:
                predictions["overall_risk"] = "critical"
            elif max_confidence > 60:
                predictions["overall_risk"] = "high"
            else:
                predictions["overall_risk"] = "moderate"
        
        return predictions
    
    def _calculate_confidence(self, sensor_data: Dict, indicators: Dict) -> float:
        """Calculate disease confidence score"""
        matches = 0
        total_indicators = len(indicators)
        
        for sensor_type, (min_val, max_val) in indicators.items():
            if sensor_type in sensor_data:
                value = sensor_data[sensor_type]
                if min_val <= value <= max_val:
                    matches += 1
        
        return matches / total_indicators if total_indicators > 0 else 0
    
    def _get_risk_level(self, confidence: float) -> str:
        """Get risk level from confidence"""
        if confidence >= 0.8:
            return "critical"
        elif confidence >= 0.65:
            return "high"
        elif confidence >= 0.5:
            return "moderate"
        else:
            return "low"
    
    def _get_treatment(self, disease: str) -> str:
        """Get recommended treatment"""
        treatments = {
            "varroa_mites": "Apply mite treatment, monitor closely, consider hive split",
            "american_foulbrood": "⚠️ CRITICAL: Requires professional intervention, possible hive destruction",
            "colony_collapse": "Investigate cause, feed if necessary, consider queen replacement",
            "nosema": "Improve hive ventilation, add protein, treat with medication"
        }
        return treatments.get(disease, "Consult with beekeeping expert")


class YieldPredictor:
    """Predicts honey yield based on historical data"""
    
    def __init__(self):
        self.historical_data = []
    
    def predict_yield(self, hive_weight_progression: List[float], days_until_harvest: int = 30) -> Dict:
        """Predict honey yield"""
        if len(hive_weight_progression) < 2:
            return {"error": "Insufficient data for prediction"}
        
        # Calculate average daily weight gain
        daily_gains = [hive_weight_progression[i+1] - hive_weight_progression[i] 
                       for i in range(len(hive_weight_progression)-1)]
        avg_daily_gain = sum(daily_gains) / len(daily_gains)
        
        # Predict final weight
        current_weight = hive_weight_progression[-1]
        predicted_weight = current_weight + (avg_daily_gain * days_until_harvest)
        
        # Assume honey is about 60% of total weight
        estimated_honey = predicted_weight * 0.6
        
        # Confidence based on consistency of gains
        gain_variance = sum((g - avg_daily_gain) ** 2 for g in daily_gains) / len(daily_gains)
        confidence = max(0.3, 1 - (gain_variance / max(abs(avg_daily_gain), 0.1)))
        
        return {
            "prediction_date": datetime.now().isoformat(),
            "current_weight": round(current_weight, 2),
            "estimated_harvest_weight": round(predicted_weight, 2),
            "estimated_honey_yield": round(estimated_honey, 2),
            "average_daily_gain": round(avg_daily_gain, 2),
            "days_until_harvest": days_until_harvest,
            "confidence": round(confidence * 100, 2),
            "recommendation": self._get_yield_recommendation(estimated_honey, confidence)
        }
    
    def _get_yield_recommendation(self, estimated_yield: float, confidence: float) -> str:
        """Get recommendation based on yield prediction"""
        if estimated_yield > 15:
            base_rec = "✅ Excellent yield expected"
        elif estimated_yield > 10:
            base_rec = "✅ Good yield expected"
        elif estimated_yield > 5:
            base_rec = "⚠️ Moderate yield, consider feeding"
        else:
            base_rec = "❌ Low yield expected, immediate intervention needed"
        
        if confidence < 0.5:
            base_rec += " (Low confidence - more data needed)"
        
        return base_rec


# Example usage
if __name__ == "__main__":
    # Sample sensor readings
    sample_readings = [
        {"sensor_type": "temperature", "value": 32.5, "unit": "°C"},
        {"sensor_type": "humidity", "value": 65.0, "unit": "%"},
        {"sensor_type": "weight", "value": 15.2, "unit": "kg"},
        {"sensor_type": "sound", "value": 78.5, "unit": "dB"},
    ]
    
    # Health analysis
    analyzer = HiveHealthAnalyzer()
    health = analyzer.analyze_readings(sample_readings)
    print("\n🏥 Health Analysis:")
    print(f"  Overall Health: {health['overall_health']}")
    print(f"  Health Score: {health['health_score']}/100")
    
    # Disease prediction
    predictor = DiseasePredictor()
    diseases = predictor.predict_diseases(sample_readings)
    print("\n🦠 Disease Prediction:")
    print(f"  Overall Risk: {diseases['overall_risk']}")
    if diseases["diseases"]:
        for disease in diseases["diseases"]:
            print(f"  - {disease['disease']}: {disease['confidence']}% ({disease['risk_level']})")
    else:
        print("  ✅ No diseases detected")
    
    # Yield prediction
    yield_pred = YieldPredictor()
    weight_progression = [13.5, 14.0, 14.5, 15.0, 15.2, 15.5]
    yield_est = yield_pred.predict_yield(weight_progression)
    print("\n🍯 Yield Prediction:")
    print(f"  Estimated Yield: {yield_est['estimated_honey_yield']}kg")
    print(f"  Confidence: {yield_est['confidence']}%")
