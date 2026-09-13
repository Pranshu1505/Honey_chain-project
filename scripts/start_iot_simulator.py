#!/usr/bin/env python
"""
IoT Simulator - Generates realistic sensor data
Usage: python start_iot_simulator.py
"""
import sys
import time
from iot.simulator import IoTSimulator


def run_continuous_simulation():
    """Run continuous IoT simulation"""
    simulator = IoTSimulator(hive_count=5)
    
    print("\n" + "="*70)
    print("  🍯 HONEY CHAIN - IoT SIMULATOR")
    print("="*70)
    print("\n📊 Starting simulation with 5 hives...")
    print("Each hive has 4 sensors: Temperature, Humidity, Weight, Sound")
    print("\nPress Ctrl+C to stop\n")
    
    iteration = 0
    try:
        while True:
            iteration += 1
            print(f"\n📈 Reading #{iteration} - {time.strftime('%H:%M:%S')}")
            print("-" * 70)
            
            data = simulator.simulate_all()
            
            for hive_id, hive_data in data["hives"].items():
                status = hive_data["status"]
                readings = hive_data["readings"]
                
                print(f"\n  {hive_id}:")
                print(f"    Status: {status['status'].upper()}")
                print(f"    Alerts: {status['alerts']}")
                
                for reading in readings:
                    sensor_type = reading['sensor_type']
                    value = reading['value']
                    unit = reading['unit']
                    status_val = reading['status']
                    
                    status_emoji = "✅" if status_val == "normal" else "⚠️"
                    print(f"    {status_emoji} {sensor_type.capitalize()}: {value} {unit}")
            
            print(f"\n  Total Alerts: {data['total_alerts']}")
            
            # Export every 10 iterations
            if iteration % 10 == 0:
                filename = simulator.export_to_json(f"iot_data_export_{iteration}.json")
                print(f"  💾 Data exported to {filename}")
            
            # Wait before next reading
            time.sleep(5)
    
    except KeyboardInterrupt:
        print("\n\n" + "="*70)
        print("  ⏹️ Simulation stopped")
        print("="*70)
        
        summary = simulator.get_summary()
        print("\n📊 Simulation Summary:")
        print(f"  Total Hives: {summary['total_hives']}")
        print(f"  Total Readings: {summary['total_readings']}")
        print(f"  Total Data Points: {summary['total_data_points']}")
        
        filename = simulator.export_to_json("iot_data_final.json")
        print(f"  Final data exported to {filename}")
        print()


def run_demo():
    """Run demo with predefined iterations"""
    simulator = IoTSimulator(hive_count=3)
    
    print("\n" + "="*70)
    print("  🍯 HONEY CHAIN - IoT SIMULATOR (DEMO)")
    print("="*70)
    print("\n📊 Demo: 10 readings from 3 hives\n")
    
    for i in range(10):
        print(f"\n📈 Reading #{i+1}")
        print("-" * 70)
        
        data = simulator.simulate_all()
        
        for hive_id, hive_data in data["hives"].items():
            status = hive_data["status"]
            readings = hive_data["readings"]
            
            print(f"\n  {hive_id}: {status['status'].upper()}")
            
            for reading in readings:
                sensor_type = reading['sensor_type']
                value = reading['value']
                unit = reading['unit']
                print(f"    • {sensor_type.capitalize()}: {value} {unit}")
        
        if i < 9:
            time.sleep(1)
    
    print("\n" + "="*70)
    print("  ✅ Demo Complete")
    print("="*70)
    
    # Export data
    filename = simulator.export_to_json()
    print(f"\n📊 Data exported to: {filename}")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--demo":
        run_demo()
    else:
        run_continuous_simulation()
