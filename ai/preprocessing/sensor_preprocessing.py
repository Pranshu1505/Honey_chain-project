"""Sensor Data Preprocessing - Clean and prepare sensor data for AI"""
from typing import List, Dict
import statistics


class SensorPreprocessor:
    """Preprocesses raw sensor data for AI analysis"""
    
    @staticmethod
    def clean_sensor_readings(readings: List[float], remove_outliers: bool = True) -> List[float]:
        """Clean sensor readings by removing outliers and invalid values"""
        
        if not readings:
            return []
        
        # Remove None and negative values
        valid_readings = [r for r in readings if r is not None and r >= 0]
        
        if not valid_readings:
            return []
        
        if not remove_outliers or len(valid_readings) < 3:
            return valid_readings
        
        # Remove outliers using IQR method
        sorted_readings = sorted(valid_readings)
        q1 = sorted_readings[len(sorted_readings) // 4]
        q3 = sorted_readings[3 * len(sorted_readings) // 4]
        iqr = q3 - q1
        
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr
        
        cleaned = [r for r in valid_readings if lower_bound <= r <= upper_bound]
        
        return cleaned if cleaned else valid_readings
    
    @staticmethod
    def interpolate_missing_values(readings: List[float], max_gap: int = 3) -> List[float]:
        """Interpolate missing values in sensor readings"""
        
        if len(readings) < 2:
            return readings
        
        interpolated = []
        
        for i, reading in enumerate(readings):
            interpolated.append(reading)
            
            # Check for gap to next reading
            if i < len(readings) - 1:
                next_reading = readings[i + 1]
                if abs(next_reading - reading) > max_gap:
                    # Linear interpolation
                    mid_value = (reading + next_reading) / 2
                    interpolated.append(mid_value)
        
        return interpolated
    
    @staticmethod
    def normalize_readings(readings: List[float], 
                          min_val: float = 0, 
                          max_val: float = 100) -> List[float]:
        """Normalize readings to a specific range"""
        
        if not readings:
            return []
        
        data_min = min(readings)
        data_max = max(readings)
        data_range = data_max - data_min
        
        if data_range == 0:
            # All values are the same
            return [(min_val + max_val) / 2] * len(readings)
        
        normalized = [
            min_val + (r - data_min) / data_range * (max_val - min_val)
            for r in readings
        ]
        
        return normalized
    
    @staticmethod
    def aggregate_readings(readings: List[float], window_size: int = 5) -> List[float]:
        """Aggregate readings using moving average"""
        
        if len(readings) < window_size:
            return readings
        
        aggregated = []
        for i in range(len(readings) - window_size + 1):
            window = readings[i:i + window_size]
            avg = statistics.mean(window)
            aggregated.append(avg)
        
        return aggregated
    
    @staticmethod
    def prepare_features(sensor_data: Dict[str, List[float]]) -> Dict[str, float]:
        """Prepare features from raw sensor data for ML models"""
        
        features = {}
        
        for sensor_type, readings in sensor_data.items():
            if not readings:
                continue
            
            # Clean data
            cleaned = SensorPreprocessor.clean_sensor_readings(readings)
            
            if not cleaned:
                continue
            
            # Calculate statistics
            features[f'{sensor_type}_mean'] = statistics.mean(cleaned)
            features[f'{sensor_type}_std'] = statistics.stdev(cleaned) if len(cleaned) > 1 else 0
            features[f'{sensor_type}_min'] = min(cleaned)
            features[f'{sensor_type}_max'] = max(cleaned)
            features[f'{sensor_type}_range'] = max(cleaned) - min(cleaned)
            
            # Calculate trend
            if len(cleaned) > 1:
                trend = cleaned[-1] - cleaned[0]
                features[f'{sensor_type}_trend'] = trend
        
        return features
    
    @staticmethod
    def validate_sensor_data(hive_id: int, sensor_type: str, value: float) -> Dict:
        """Validate sensor data before storing"""
        
        validation_rules = {
            'temperature': {'min': -10, 'max': 50, 'unit': '°C'},
            'humidity': {'min': 0, 'max': 100, 'unit': '%'},
            'weight': {'min': 5, 'max': 100, 'unit': 'kg'},
            'sound': {'min': 20, 'max': 100, 'unit': 'dB'},
        }
        
        if sensor_type not in validation_rules:
            return {'valid': False, 'error': 'Unknown sensor type'}
        
        rules = validation_rules[sensor_type]
        
        if value < rules['min'] or value > rules['max']:
            return {
                'valid': False,
                'error': f'{sensor_type} reading out of range ({rules["min"]}-{rules["max"]} {rules["unit"]})',
                'value': value,
            }
        
        return {'valid': True, 'value': value, 'sensor_type': sensor_type}
