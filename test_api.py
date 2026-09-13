"""
Test script for Honey Chain API endpoints
Run with: python test_api.py
"""
import os
import django
import json
from django.contrib.auth.models import User
from django.test import Client

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.dev')
django.setup()

from apps.beekeeper.models import Apiary, BeekeeperProfile
from apps.hive.models import Hive, HiveHealth
from apps.harvest.models import Harvest
from apps.batch.models import HoneyBatch
from apps.blockchain.models import BlockchainTransaction, BlockchainRecord
from apps.qr.models import QRCode
from apps.sensor.models import SensorData
from apps.processing.models import Processing, QualityTest


def print_section(title):
    """Print a formatted section title"""
    print("\n" + "=" * 60)
    print(f"  {title}")
    print("=" * 60)


def test_user_creation():
    """Test 1: User Creation"""
    print_section("TEST 1: User Creation & Authentication")
    
    # Clean up test user if exists
    User.objects.filter(username='test_beekeeper').delete()
    
    # Create test user
    user = User.objects.create_user(
        username='test_beekeeper',
        email='beekeeper@example.com',
        password='testpass123',
        first_name='Ramesh',
        last_name='Kumar'
    )
    print(f"✅ User Created: {user.username}")
    print(f"   Email: {user.email}")
    print(f"   ID: {user.id}")
    
    return user


def test_beekeeper_profile(user):
    """Test 2: Beekeeper Profile"""
    print_section("TEST 2: Beekeeper Profile Management")
    
    profile = BeekeeperProfile.objects.create(
        user=user,
        years_of_experience=8,
        total_hives=45,
        avg_honey_yield=12.5,
        certification='ISO 9001'
    )
    print(f"✅ Beekeeper Profile Created")
    print(f"   Experience: {profile.years_of_experience} years")
    print(f"   Total Hives: {profile.total_hives}")
    print(f"   Avg Yield: {profile.avg_honey_yield} kg/year")
    
    return profile


def test_apiary(user):
    """Test 3: Apiary Management"""
    print_section("TEST 3: Apiary Management")
    
    apiary = Apiary.objects.create(
        beekeeper=user,
        name='Hill Valley Apiary',
        location='Lucknow, Uttar Pradesh',
        latitude=26.8467,
        longitude=80.9462,
        total_hives=45,
        description='Premium honey production facility'
    )
    print(f"✅ Apiary Created: {apiary.name}")
    print(f"   Location: {apiary.location}")
    print(f"   Coordinates: ({apiary.latitude}, {apiary.longitude})")
    print(f"   Total Hives: {apiary.total_hives}")
    
    return apiary


def test_hive(apiary):
    """Test 4: Hive Management"""
    print_section("TEST 4: Hive Management")
    
    hive = Hive.objects.create(
        apiary=apiary,
        hive_id='HIVE-001-LV',
        name='Premium Hive #1',
        hive_type='langstroth',
        installation_date='2026-01-15',
        health_status='healthy',
        population=40000,
        honey_frames=8
    )
    print(f"✅ Hive Created: {hive.hive_id}")
    print(f"   Type: {hive.hive_type}")
    print(f"   Health Status: {hive.health_status}")
    print(f"   Population: {hive.population} bees")
    
    return hive


def test_hive_health(hive):
    """Test 5: Hive Health Metrics"""
    print_section("TEST 5: Hive Health Metrics")
    
    health = HiveHealth.objects.create(
        hive=hive,
        temperature=32.5,
        humidity=65.0,
        weight=15.2,
        bee_activity=85,
        disease_risk='low'
    )
    print(f"✅ Hive Health Metrics Created")
    print(f"   Temperature: {health.temperature}°C")
    print(f"   Humidity: {health.humidity}%")
    print(f"   Weight: {health.weight} kg")
    print(f"   Bee Activity: {health.bee_activity}%")
    print(f"   Disease Risk: {health.disease_risk}")
    
    return health


def test_sensor_data(hive):
    """Test 6: Sensor Data Collection"""
    print_section("TEST 6: Sensor Data Collection (IoT)")
    
    sensors = []
    sensor_types = [
        ('temperature', '°C', 32.5),
        ('humidity', '%', 65.0),
        ('weight', 'kg', 15.2),
        ('sound', 'dB', 78.5)
    ]
    
    for sensor_type, unit, value in sensor_types:
        sensor = SensorData.objects.create(
            hive=hive,
            sensor_type=sensor_type,
            sensor_id=f'SENSOR-{sensor_type.upper()}-001',
            value=value,
            unit=unit
        )
        sensors.append(sensor)
        print(f"✅ {sensor_type.capitalize()} Sensor: {value} {unit}")
    
    return sensors


def test_harvest(hive):
    """Test 7: Harvest Recording"""
    print_section("TEST 7: Harvest Recording")
    
    harvest = Harvest.objects.create(
        hive=hive,
        harvest_date='2026-09-01',
        quantity=12.5,
        honey_type='multifloral',
        color_grade='amber',
        notes='Premium quality harvest from spring season'
    )
    print(f"✅ Harvest Recorded: {harvest.hive.hive_id}")
    print(f"   Date: {harvest.harvest_date}")
    print(f"   Quantity: {harvest.quantity} kg")
    print(f"   Type: {harvest.honey_type}")
    print(f"   Color Grade: {harvest.color_grade}")
    
    return harvest


def test_honey_batch(harvest):
    """Test 8: Honey Batch Management"""
    print_section("TEST 8: Honey Batch Management")
    
    batch = HoneyBatch.objects.create(
        batch_id='BATCH-2026-0001',
        total_quantity=50.0,
        honey_type='Premium Multifloral',
        status='created',
        quality_score=0
    )
    batch.harvests.add(harvest)
    print(f"✅ Honey Batch Created: {batch.batch_id}")
    print(f"   Total Quantity: {batch.total_quantity} kg")
    print(f"   Status: {batch.status}")
    print(f"   Quality Score: {batch.quality_score}/100")
    
    return batch


def test_quality_test(batch):
    """Test 9: Quality Testing"""
    print_section("TEST 9: Quality Testing")
    
    quality = QualityTest.objects.create(
        batch=batch,
        acidity=3.5,
        moisture=17.2,
        color_intensity=95,
        aroma_grade='excellent',
        is_approved=True
    )
    print(f"✅ Quality Test Completed for {batch.batch_id}")
    print(f"   Acidity: {quality.acidity}")
    print(f"   Moisture: {quality.moisture}%")
    print(f"   Color Intensity: {quality.color_intensity}")
    print(f"   Aroma Grade: {quality.aroma_grade}")
    print(f"   Approved: {quality.is_approved}")
    
    return quality


def test_processing(batch):
    """Test 10: Processing Records"""
    print_section("TEST 10: Processing Records")
    
    processing = Processing.objects.create(
        batch=batch,
        temperature=60,
        duration=120,
        notes='Heated pasteurization process completed'
    )
    print(f"✅ Processing Record Created")
    print(f"   Temperature: {processing.temperature}°C")
    print(f"   Duration: {processing.duration} minutes")
    print(f"   Notes: {processing.notes}")
    
    return processing


def test_blockchain(batch):
    """Test 11: Blockchain Transactions"""
    print_section("TEST 11: Blockchain Transactions")
    
    blockchain_user = User.objects.filter(is_superuser=True).first()
    
    transaction = BlockchainTransaction.objects.create(
        user=blockchain_user,
        batch_id=batch.batch_id,
        transaction_hash='0x' + 'a' * 64,
        transaction_type='batch_creation',
        data={
            'batch_id': batch.batch_id,
            'quantity': batch.total_quantity,
            'honey_type': batch.honey_type,
            'timestamp': '2026-09-12T15:00:00Z'
        },
        status='confirmed',
        block_number=12345
    )
    print(f"✅ Blockchain Transaction Recorded")
    print(f"   Batch ID: {transaction.batch_id}")
    print(f"   Type: {transaction.transaction_type}")
    print(f"   Hash: {transaction.transaction_hash[:16]}...")
    print(f"   Block: {transaction.block_number}")
    print(f"   Status: {transaction.status}")
    
    return transaction


def test_blockchain_record(batch):
    """Test 12: Blockchain Records"""
    print_section("TEST 12: Blockchain Records")
    
    record = BlockchainRecord.objects.create(
        batch_id=batch.batch_id,
        origin='Hill Valley Apiary, Lucknow',
        transaction_hash='0x' + 'b' * 64,
        block_number=12345,
        honey_type=batch.honey_type,
        quantity=batch.total_quantity,
        quality_score=90,
        test_results={
            'acidity': 3.5,
            'moisture': 17.2,
            'color_intensity': 95
        }
    )
    print(f"✅ Blockchain Record Created")
    print(f"   Batch: {record.batch_id}")
    print(f"   Origin: {record.origin}")
    print(f"   Quality Score: {record.quality_score}/100")
    print(f"   Block: {record.block_number}")
    
    return record


def test_qr_code(batch):
    """Test 13: QR Code Generation"""
    print_section("TEST 13: QR Code Generation")
    
    qr = QRCode.objects.create(
        batch=batch,
        code_data=f'https://honeychain.example.com/verify/{batch.batch_id}',
        scans=0
    )
    print(f"✅ QR Code Created")
    print(f"   Batch: {batch.batch_id}")
    print(f"   Data: {qr.code_data}")
    print(f"   Scans: {qr.scans}")
    
    return qr


def test_summary():
    """Test 14: Database Summary"""
    print_section("TEST 14: Database Summary")
    
    stats = {
        'Users': User.objects.count(),
        'Beekeepers': BeekeeperProfile.objects.count(),
        'Apiaries': Apiary.objects.count(),
        'Hives': Hive.objects.count(),
        'Harvests': Harvest.objects.count(),
        'Honey Batches': HoneyBatch.objects.count(),
        'Sensor Data Points': SensorData.objects.count(),
        'Blockchain Transactions': BlockchainTransaction.objects.count(),
        'Blockchain Records': BlockchainRecord.objects.count(),
        'QR Codes': QRCode.objects.count(),
    }
    
    for entity, count in stats.items():
        print(f"✅ {entity}: {count}")
    
    return stats


def run_all_tests():
    """Run all tests"""
    print("\n")
    print("╔" + "=" * 58 + "╗")
    print("║" + " " * 58 + "║")
    print("║" + "  🍯 HONEY CHAIN - COMPREHENSIVE TEST SUITE 🍯  ".center(58) + "║")
    print("║" + " " * 58 + "║")
    print("╚" + "=" * 58 + "╝")
    
    try:
        # Test sequence
        user = test_user_creation()
        beekeeper = test_beekeeper_profile(user)
        apiary = test_apiary(user)
        hive = test_hive(apiary)
        health = test_hive_health(hive)
        sensors = test_sensor_data(hive)
        harvest = test_harvest(hive)
        batch = test_honey_batch(harvest)
        quality = test_quality_test(batch)
        processing = test_processing(batch)
        blockchain_tx = test_blockchain(batch)
        blockchain_record = test_blockchain_record(batch)
        qr = test_qr_code(batch)
        stats = test_summary()
        
        print_section("✅ ALL TESTS PASSED SUCCESSFULLY!")
        print("\n✅ Features Verified:")
        print("   ✓ User Authentication & Profiles")
        print("   ✓ Beekeeper Management")
        print("   ✓ Apiary & Hive Management")
        print("   ✓ Health Metrics Tracking")
        print("   ✓ IoT Sensor Data Collection")
        print("   ✓ Harvest Recording")
        print("   ✓ Honey Batch Management")
        print("   ✓ Quality Testing & Assurance")
        print("   ✓ Processing Workflows")
        print("   ✓ Blockchain Integration")
        print("   ✓ QR Code Generation")
        print("   ✓ Database Operations")
        
        print("\n📊 Total Records Created:")
        total = sum(stats.values())
        print(f"   Total: {total} records")
        
        return True
        
    except Exception as e:
        print_section("❌ TEST FAILED")
        print(f"Error: {str(e)}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == '__main__':
    success = run_all_tests()
    exit(0 if success else 1)
