"""IoT Sensor Generator - Simulates realistic sensor data"""
import random
from datetime import datetime
from decimal import Decimal


class SensorGenerator:
    """Generate realistic sensor data for testing"""
    
    @staticmethod
    def generate_temperature(hive_id: int, base_temp: float = 35.0) -> dict:
        """Generate temperature sensor data"""
        variation = random.uniform(-2, 2)
        return {
            'sensor_type': 'temperature',
            'sensor_id': f'TEMP_{hive_id}_{int(datetime.now().timestamp())}',
            'value': round(base_temp + variation, 2),
            'unit': '°C',
            'hive_id': hive_id,
        }
    
    @staticmethod
    def generate_humidity(hive_id: int, base_humidity: float = 65.0) -> dict:
        """Generate humidity sensor data"""
        variation = random.uniform(-5, 5)
        value = min(100, max(0, base_humidity + variation))
        return {
            'sensor_type': 'humidity',
            'sensor_id': f'HUM_{hive_id}_{int(datetime.now().timestamp())}',
            'value': round(value, 2),
            'unit': '%',
            'hive_id': hive_id,
        }
    
    @staticmethod
    def generate_weight(hive_id: int, base_weight: float = 40.0) -> dict:
        """Generate weight sensor data"""
        variation = random.uniform(-0.5, 0.5)
        return {
            'sensor_type': 'weight',
            'sensor_id': f'WEIGHT_{hive_id}_{int(datetime.now().timestamp())}',
            'value': round(base_weight + variation, 2),
            'unit': 'kg',
            'hive_id': hive_id,
        }
    
    @staticmethod
    def generate_sound_activity(hive_id: int) -> dict:
        """Generate sound activity sensor data"""
        return {
            'sensor_type': 'sound',
            'sensor_id': f'SOUND_{hive_id}_{int(datetime.now().timestamp())}',
            'value': round(random.uniform(40, 80), 2),
            'unit': 'dB',
            'hive_id': hive_id,
        }
    
    @staticmethod
    def generate_all_sensors(hive_id: int) -> list:
        """Generate all sensor readings for a hive"""
        return [
            SensorGenerator.generate_temperature(hive_id),
            SensorGenerator.generate_humidity(hive_id),
            SensorGenerator.generate_weight(hive_id),
            SensorGenerator.generate_sound_activity(hive_id),
        ]
