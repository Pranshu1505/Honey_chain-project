"""
IoT Sensor Simulator
Generates realistic sensor data for testing and demonstration
"""
import random
import time
from datetime import datetime, timedelta
from typing import Dict, List
import json

class TemperatureSensor:
    """Temperature sensor simulator"""
    def __init__(self, min_temp=25, max_temp=40, hive_id="HIVE-001"):
        self.min_temp = min_temp
        self.max_temp = max_temp
        self.hive_id = hive_id
        self.current_temp = 32.5
        self.trend = random.choice([-0.1, 0, 0.1])
    
    def read(self) -> Dict:
        """Read sensor data"""
        # Simulate natural temperature fluctuation
        self.current_temp += self.trend
        self.current_temp = max(self.min_temp, min(self.max_temp, self.current_temp))
        
        # Occasionally change trend
        if random.random() < 0.1:
            self.trend = random.uniform(-0.2, 0.2)
        
        return {
            "sensor_type": "temperature",
            "sensor_id": f"SENSOR-TEMP-{self.hive_id}",
            "value": round(self.current_temp, 2),
            "unit": "°C",
            "timestamp": datetime.now().isoformat(),
            "hive_id": self.hive_id,
            "status": "normal" if self.min_temp < self.current_temp < self.max_temp else "alert"
        }


class HumiditySensor:
    """Humidity sensor simulator"""
    def __init__(self, min_humidity=50, max_humidity=80, hive_id="HIVE-001"):
        self.min_humidity = min_humidity
        self.max_humidity = max_humidity
        self.hive_id = hive_id
        self.current_humidity = 65.0
        self.trend = random.choice([-0.15, 0, 0.15])
    
    def read(self) -> Dict:
        """Read sensor data"""
        self.current_humidity += self.trend
        self.current_humidity = max(self.min_humidity, min(self.max_humidity, self.current_humidity))
        
        if random.random() < 0.1:
            self.trend = random.uniform(-0.3, 0.3)
        
        return {
            "sensor_type": "humidity",
            "sensor_id": f"SENSOR-HUMIDITY-{self.hive_id}",
            "value": round(self.current_humidity, 2),
            "unit": "%",
            "timestamp": datetime.now().isoformat(),
            "hive_id": self.hive_id,
            "status": "normal" if self.min_humidity < self.current_humidity < self.max_humidity else "alert"
        }


class WeightSensor:
    """Weight sensor simulator"""
    def __init__(self, min_weight=10, max_weight=20, hive_id="HIVE-001"):
        self.min_weight = min_weight
        self.max_weight = max_weight
        self.hive_id = hive_id
        self.current_weight = 15.2
        self.trend = random.uniform(0.01, 0.05)  # Honey accumulation
    
    def read(self) -> Dict:
        """Read sensor data"""
        # Simulate honey accumulation
        self.current_weight += self.trend
        if self.current_weight > self.max_weight:
            self.current_weight = self.max_weight
        
        return {
            "sensor_type": "weight",
            "sensor_id": f"SENSOR-WEIGHT-{self.hive_id}",
            "value": round(self.current_weight, 2),
            "unit": "kg",
            "timestamp": datetime.now().isoformat(),
            "hive_id": self.hive_id,
            "status": "normal" if self.min_weight < self.current_weight < self.max_weight else "alert"
        }


class SoundSensor:
    """Sound/Activity sensor simulator"""
    def __init__(self, baseline=65, hive_id="HIVE-001"):
        self.baseline = baseline
        self.hive_id = hive_id
    
    def read(self) -> Dict:
        """Read sensor data"""
        # Simulate normal bee activity with occasional spikes
        variance = random.uniform(-10, 10)
        if random.random() < 0.1:  # 10% chance of high activity
            variance = random.uniform(10, 20)
        
        value = self.baseline + variance
        value = max(50, min(95, value))  # Keep within realistic range
        
        return {
            "sensor_type": "sound",
            "sensor_id": f"SENSOR-SOUND-{self.hive_id}",
            "value": round(value, 2),
            "unit": "dB",
            "timestamp": datetime.now().isoformat(),
            "hive_id": self.hive_id,
            "status": "normal" if 60 < value < 90 else "alert"
        }


class HiveSimulator:
    """Simulates an entire hive with multiple sensors"""
    def __init__(self, hive_id="HIVE-001"):
        self.hive_id = hive_id
        self.temperature_sensor = TemperatureSensor(hive_id=hive_id)
        self.humidity_sensor = HumiditySensor(hive_id=hive_id)
        self.weight_sensor = WeightSensor(hive_id=hive_id)
        self.sound_sensor = SoundSensor(hive_id=hive_id)
        self.data_points = []
    
    def read_all_sensors(self) -> List[Dict]:
        """Read all sensors"""
        data = [
            self.temperature_sensor.read(),
            self.humidity_sensor.read(),
            self.weight_sensor.read(),
            self.sound_sensor.read()
        ]
        self.data_points.append({
            "timestamp": datetime.now().isoformat(),
            "readings": data
        })
        return data
    
    def get_hive_status(self) -> Dict:
        """Get overall hive status"""
        latest_readings = self.data_points[-1]["readings"] if self.data_points else []
        
        alerts = [r for r in latest_readings if r.get("status") == "alert"]
        
        return {
            "hive_id": self.hive_id,
            "timestamp": datetime.now().isoformat(),
            "sensor_count": 4,
            "alerts": len(alerts),
            "status": "warning" if alerts else "healthy",
            "readings_count": len(self.data_points)
        }


class IoTSimulator:
    """Main IoT simulator for multiple hives"""
    def __init__(self, hive_count=5):
        self.hives: Dict[str, HiveSimulator] = {}
        for i in range(1, hive_count + 1):
            hive_id = f"HIVE-{i:03d}"
            self.hives[hive_id] = HiveSimulator(hive_id=hive_id)
    
    def simulate_all(self) -> Dict:
        """Simulate all hives"""
        data = {
            "timestamp": datetime.now().isoformat(),
            "hives": {},
            "total_alerts": 0
        }
        
        for hive_id, hive in self.hives.items():
            readings = hive.read_all_sensors()
            status = hive.get_hive_status()
            
            data["hives"][hive_id] = {
                "status": status,
                "readings": readings
            }
            data["total_alerts"] += status["alerts"]
        
        return data
    
    def export_to_json(self, filename="iot_data.json"):
        """Export all data to JSON"""
        data = {
            "exported_at": datetime.now().isoformat(),
            "hives": {}
        }
        
        for hive_id, hive in self.hives.items():
            data["hives"][hive_id] = hive.data_points
        
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
        
        return filename
    
    def get_summary(self) -> Dict:
        """Get simulation summary"""
        total_readings = sum(len(h.data_points) for h in self.hives.values())
        total_data_points = sum(len(h.data_points) * 4 for h in self.hives.values())  # 4 sensors per hive
        
        return {
            "total_hives": len(self.hives),
            "total_readings": total_readings,
            "total_data_points": total_data_points,
            "hive_ids": list(self.hives.keys()),
            "simulation_active": True
        }


# Example usage
if __name__ == "__main__":
    simulator = IoTSimulator(hive_count=3)
    
    print("🍯 IoT Simulator Started")
    print("=" * 60)
    
    for i in range(5):
        print(f"\n📊 Reading {i+1}:")
        data = simulator.simulate_all()
        
        for hive_id, hive_data in data["hives"].items():
            status = hive_data["status"]
            print(f"  {hive_id}: {status['status'].upper()} - {status['alerts']} alerts")
        
        if i < 4:
            time.sleep(2)
    
    print("\n" + "=" * 60)
    print("📈 Simulation Summary:")
    summary = simulator.get_summary()
    for key, value in summary.items():
        print(f"  {key}: {value}")
    
    # Export data
    filename = simulator.export_to_json()
    print(f"\n✅ Data exported to {filename}")
