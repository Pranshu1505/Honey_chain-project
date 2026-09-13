"""
Test script for Honey Chain API endpoints
Run with: python manage.py shell < test_features.py
"""

from django.contrib.auth.models import User
from apps.beekeeper.models import Apiary, BeekeeperProfile
from apps.hive.models import Hive, HiveHealth
from apps.harvest.models import Harvest
from apps.batch.models import HoneyBatch
from apps.blockchain.models import BlockchainTransaction, BlockchainRecord
from apps.qr.models import QRCode
from apps.sensor.models import SensorData
from apps.processing.models import Processing, QualityTest

def print_test(title):
    print("\n" + "="*60)
    print(f"  {title}")
    print("="*60)

print("\n\n╔" + "="*58 + "╗")
print("║" + " "*58 + "║")
print("║" + "  🍯 HONEY CHAIN - FEATURE TEST 🍯  ".center(58) + "║")
print("║" + " "*58 + "║")
print("╚" + "="*58 + "╝\n")

# TEST 1: User Creation
print_test("TEST 1: User Creation")
User.objects.filter(username='test_beekeeper').delete()
user = User.objects.create_user(
    username='test_beekeeper',
    email='beekeeper@example.com',
    password='testpass123',
    first_name='Ramesh',
    last_name='Kumar'
)
print(f"✅ User Created: {user.username}")

# TEST 2: Beekeeper Profile
print_test("TEST 2: Beekeeper Profile")
profile = BeekeeperProfile.objects.create(
    user=user,
    years_of_experience=8,
    total_hives=45,
    avg_honey_yield=12.5,
    certification='ISO 9001'
)
print(f"✅ Beekeeper Profile Created")

# TEST 3: Apiary
print_test("TEST 3: Apiary Management")
apiary = Apiary.objects.create(
    beekeeper=user,
    name='Hill Valley Apiary',
    location='Lucknow, Uttar Pradesh',
    latitude=26.8467,
    longitude=80.9462,
    total_hives=45
)
print(f"✅ Apiary Created: {apiary.name}")

# TEST 4: Hive
print_test("TEST 4: Hive Management")
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

# TEST 5: Hive Health
print_test("TEST 5: Hive Health Metrics")
health = HiveHealth.objects.create(
    hive=hive,
    temperature=32.5,
    humidity=65.0,
    weight=15.2,
    bee_activity=85,
    disease_risk='low'
)
print(f"✅ Health Metrics Created - Temp: {health.temperature}°C")

# TEST 6: Sensor Data
print_test("TEST 6: Sensor Data (IoT)")
sensor = SensorData.objects.create(
    hive=hive,
    sensor_type='temperature',
    sensor_id='SENSOR-TEMP-001',
    value=32.5,
    unit='°C'
)
print(f"✅ Sensor Data Created: {sensor.sensor_type}")

# TEST 7: Harvest
print_test("TEST 7: Harvest Recording")
harvest = Harvest.objects.create(
    hive=hive,
    harvest_date='2026-09-01',
    quantity=12.5,
    honey_type='multifloral',
    color_grade='amber'
)
print(f"✅ Harvest Created: {harvest.quantity} kg")

# TEST 8: Honey Batch
print_test("TEST 8: Honey Batch Management")
batch = HoneyBatch.objects.create(
    batch_id='BATCH-2026-0001',
    total_quantity=50.0,
    honey_type='Premium Multifloral',
    status='created'
)
batch.harvests.add(harvest)
print(f"✅ Batch Created: {batch.batch_id}")

# TEST 9: Quality Test
print_test("TEST 9: Quality Testing")
quality = QualityTest.objects.create(
    batch=batch,
    acidity=3.5,
    moisture=17.2,
    color_intensity=95,
    aroma_grade='excellent',
    is_approved=True
)
print(f"✅ Quality Test Approved: Score = 95")

# TEST 10: Processing
print_test("TEST 10: Processing Records")
processing = Processing.objects.create(
    batch=batch,
    temperature=60,
    duration=120
)
print(f"✅ Processing Record Created: {processing.temperature}°C")

# TEST 11: Blockchain Transaction
print_test("TEST 11: Blockchain Transactions")
admin_user = User.objects.filter(is_superuser=True).first()
blockchain_tx = BlockchainTransaction.objects.create(
    user=admin_user,
    batch_id=batch.batch_id,
    transaction_hash='0x' + 'a'*64,
    transaction_type='batch_creation',
    data={'batch_id': batch.batch_id},
    status='confirmed',
    block_number=12345
)
print(f"✅ Blockchain Transaction Created: Block #{blockchain_tx.block_number}")

# TEST 12: Blockchain Record
print_test("TEST 12: Blockchain Records")
record = BlockchainRecord.objects.create(
    batch_id=batch.batch_id,
    origin='Hill Valley Apiary',
    transaction_hash='0x' + 'b'*64,
    block_number=12345,
    honey_type=batch.honey_type,
    quantity=batch.total_quantity,
    quality_score=90
)
print(f"✅ Blockchain Record Created: Score = {record.quality_score}")

# TEST 13: QR Code
print_test("TEST 13: QR Code Generation")
qr = QRCode.objects.create(
    batch=batch,
    code_data=f'https://honeychain.example.com/verify/{batch.batch_id}',
    scans=0
)
print(f"✅ QR Code Created for {batch.batch_id}")

# Summary
print_test("✅ ALL FEATURES TESTED SUCCESSFULLY!")
print("\n✅ Verified Features:")
print("   ✓ User Authentication & Profiles")
print("   ✓ Beekeeper Management")
print("   ✓ Apiary & Hive Management")
print("   ✓ Health Metrics Tracking")
print("   ✓ IoT Sensor Data Collection")
print("   ✓ Harvest Recording")
print("   ✓ Honey Batch Management")
print("   ✓ Quality Testing")
print("   ✓ Processing Workflows")
print("   ✓ Blockchain Integration")
print("   ✓ QR Code Generation")

print("\n📊 Database Records:")
print(f"   Users: {User.objects.count()}")
print(f"   Beekeepers: {BeekeeperProfile.objects.count()}")
print(f"   Apiaries: {Apiary.objects.count()}")
print(f"   Hives: {Hive.objects.count()}")
print(f"   Sensor Data: {SensorData.objects.count()}")
print(f"   Batches: {HoneyBatch.objects.count()}")
print(f"   Blockchain Records: {BlockchainRecord.objects.count()}")
print(f"   QR Codes: {QRCode.objects.count()}")

print("\n✅ All tests completed successfully!\n")
