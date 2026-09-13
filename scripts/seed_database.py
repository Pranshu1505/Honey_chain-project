"""
Database Seeding Script
Populates the database with sample data for testing and demonstration
Run with: python manage.py shell < seed_database.py
"""

import os
import django
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime, timedelta

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.dev')
django.setup()

from apps.beekeeper.models import BeekeeperProfile, Apiary
from apps.hive.models import Hive, HiveHealth
from apps.harvest.models import Harvest
from apps.batch.models import HoneyBatch
from apps.sensor.models import SensorData
from apps.processing.models import QualityTest, Processing
from apps.blockchain.models import BlockchainTransaction, BlockchainRecord
from apps.qr.models import QRCode
from apps.distributor.models import Distributor, Shipment, Inventory
from apps.retailer.models import Retailer, Product, Sale
from apps.consumer.models import Consumer, Purchase, Review
from apps.notifications.models import Notification, NotificationPreference


def seed_users():
    """Create sample users"""
    print("🔐 Creating Users...")
    
    users = {
        'beekeeper1': ('beekeeper1', 'pass123', 'Rajesh', 'Kumar', 'beekeeper1@honey.com'),
        'beekeeper2': ('beekeeper2', 'pass123', 'Priya', 'Singh', 'beekeeper2@honey.com'),
        'distributor1': ('distributor1', 'pass123', 'Rohan', 'Patel', 'dist@honey.com'),
        'retailer1': ('retailer1', 'pass123', 'Anita', 'Gupta', 'retail@honey.com'),
        'consumer1': ('consumer1', 'pass123', 'Amit', 'Sharma', 'consumer@honey.com'),
        'consumer2': ('consumer2', 'pass123', 'Neha', 'Verma', 'consumer2@honey.com'),
    }
    
    created_users = {}
    for username, (uname, pwd, fname, lname, email) in users.items():
        user, created = User.objects.get_or_create(
            username=uname,
            defaults={'email': email, 'first_name': fname, 'last_name': lname}
        )
        if created:
            user.set_password(pwd)
            user.save()
            print(f"  ✅ Created user: {uname}")
        created_users[username] = user
    
    return created_users


def seed_beekeepers(users):
    """Create beekeeper profiles"""
    print("\n🧑‍🌾 Creating Beekeeper Profiles...")
    
    beekeeper_data = [
        {
            'user': users['beekeeper1'],
            'years_of_experience': 8,
            'total_hives': 50,
            'avg_honey_yield': 15.5,
            'certification': 'ISO 9001 Certified'
        },
        {
            'user': users['beekeeper2'],
            'years_of_experience': 5,
            'total_hives': 30,
            'avg_honey_yield': 12.0,
            'certification': 'Organic Certified'
        },
    ]
    
    profiles = []
    for data in beekeeper_data:
        profile, created = BeekeeperProfile.objects.get_or_create(
            user=data['user'],
            defaults=data
        )
        if created:
            print(f"  ✅ Created beekeeper: {data['user'].first_name}")
        profiles.append(profile)
    
    return profiles


def seed_apiaries(users):
    """Create apiaries"""
    print("\n🏞️ Creating Apiaries...")
    
    apiary_data = [
        {
            'beekeeper': users['beekeeper1'],
            'name': 'Hill Valley Apiary',
            'location': 'Lucknow, Uttar Pradesh',
            'latitude': 26.8467,
            'longitude': 80.9462,
            'total_hives': 25,
            'description': 'Premium honey production facility'
        },
        {
            'beekeeper': users['beekeeper1'],
            'name': 'Green Hills Apiary',
            'location': 'Noida, Uttar Pradesh',
            'latitude': 28.5921,
            'longitude': 77.3707,
            'total_hives': 25,
            'description': 'Secondary apiary in Noida'
        },
        {
            'beekeeper': users['beekeeper2'],
            'name': 'Organic Bee Farm',
            'location': 'Jaipur, Rajasthan',
            'latitude': 26.9124,
            'longitude': 75.7873,
            'total_hives': 30,
            'description': 'Certified organic honey production'
        },
    ]
    
    apiaries = []
    for data in apiary_data:
        apiary, created = Apiary.objects.get_or_create(
            name=data['name'],
            beekeeper=data['beekeeper'],
            defaults=data
        )
        if created:
            print(f"  ✅ Created apiary: {data['name']}")
        apiaries.append(apiary)
    
    return apiaries


def seed_hives(apiaries):
    """Create hives"""
    print("\n🐝 Creating Hives...")
    
    hives = []
    hive_counter = 1
    
    for apiary in apiaries:
        for i in range(min(3, apiary.total_hives)):  # Create 3 hives per apiary
            hive_id = f"HIVE-{apiary.id:03d}-{i+1:03d}"
            hive, created = Hive.objects.get_or_create(
                hive_id=hive_id,
                apiary=apiary,
                defaults={
                    'name': f'Hive #{i+1}',
                    'hive_type': 'langstroth',
                    'installation_date': timezone.now().date() - timedelta(days=180),
                    'health_status': 'healthy',
                    'population': 40000 + (i * 5000),
                    'honey_frames': 8
                }
            )
            if created:
                print(f"  ✅ Created hive: {hive_id}")
            hives.append(hive)
    
    return hives


def seed_sensor_data(hives):
    """Create sensor data"""
    print("\n📡 Creating Sensor Data...")
    
    sensor_types = ['temperature', 'humidity', 'weight', 'sound']
    
    for hive in hives[:3]:  # Create data for first 3 hives
        for sensor_type in sensor_types:
            for day in range(7):  # Last 7 days
                timestamp = timezone.now() - timedelta(days=7-day)
                
                # Generate realistic values
                if sensor_type == 'temperature':
                    value = 32.5 + (day * 0.1)
                    unit = '°C'
                elif sensor_type == 'humidity':
                    value = 65.0 + (day * 0.2)
                    unit = '%'
                elif sensor_type == 'weight':
                    value = 14.0 + (day * 0.15)
                    unit = 'kg'
                else:  # sound
                    value = 75.0 + (day * 0.5)
                    unit = 'dB'
                
                sensor, created = SensorData.objects.get_or_create(
                    hive=hive,
                    sensor_type=sensor_type,
                    timestamp=timestamp,
                    defaults={
                        'sensor_id': f'SENSOR-{sensor_type.upper()}-{hive.id}',
                        'value': round(value, 2),
                        'unit': unit
                    }
                )
                if created and day == 6:  # Print only for latest
                    print(f"  ✅ Created {sensor_type} data for {hive.hive_id}")
    
    return None


def seed_hive_health(hives):
    """Create hive health records"""
    print("\n💚 Creating Hive Health Records...")
    
    for hive in hives[:3]:
        health, created = HiveHealth.objects.get_or_create(
            hive=hive,
            defaults={
                'temperature': 32.5,
                'humidity': 65.0,
                'weight': 15.2,
                'bee_activity': 85,
                'disease_risk': 'low'
            }
        )
        if created:
            print(f"  ✅ Created health record for {hive.hive_id}")


def seed_harvests(hives):
    """Create harvest records"""
    print("\n🍖 Creating Harvest Records...")
    
    harvests = []
    for hive in hives[:3]:
        for i in range(2):  # 2 harvests per hive
            harvest, created = Harvest.objects.get_or_create(
                hive=hive,
                harvest_date=(timezone.now() - timedelta(days=30-i*15)).date(),
                defaults={
                    'quantity': 12.5 + (i * 2),
                    'honey_type': 'multifloral',
                    'color_grade': 'amber',
                    'notes': f'Good quality harvest from {hive.apiary.name}'
                }
            )
            if created:
                print(f"  ✅ Created harvest for {hive.hive_id}")
            harvests.append(harvest)
    
    return harvests


def seed_batches(harvests):
    """Create honey batches"""
    print("\n📦 Creating Honey Batches...")
    
    batches = []
    batch_id_counter = 1001
    
    for i in range(min(3, len(harvests))):
        batch_id = f"BATCH-2026-{batch_id_counter + i}"
        batch, created = HoneyBatch.objects.get_or_create(
            batch_id=batch_id,
            defaults={
                'total_quantity': 50.0 + (i * 10),
                'honey_type': 'Premium Multifloral',
                'status': 'created'
            }
        )
        if created:
            batch.harvests.add(harvests[i])
            print(f"  ✅ Created batch: {batch_id}")
        batches.append(batch)
    
    return batches


def seed_quality_tests(batches):
    """Create quality test records"""
    print("\n✅ Creating Quality Test Records...")
    
    for batch in batches:
        test, created = QualityTest.objects.get_or_create(
            batch=batch,
            defaults={
                'acidity': 3.5,
                'moisture': 17.2,
                'color_intensity': 95,
                'aroma_grade': 'excellent',
                'is_approved': True
            }
        )
        if created:
            print(f"  ✅ Created quality test for {batch.batch_id}")


def seed_blockchain(batches, users):
    """Create blockchain records"""
    print("\n⛓️ Creating Blockchain Records...")
    
    admin_user = User.objects.filter(is_superuser=True).first() or users.get('beekeeper1')
    
    for batch in batches:
        # Create transaction
        import uuid
        tx_hash = '0x' + str(uuid.uuid4()).replace('-', '')[:64]
        
        tx, created = BlockchainTransaction.objects.get_or_create(
            batch_id=batch.batch_id,
            transaction_hash=tx_hash,
            defaults={
                'user': admin_user,
                'transaction_type': 'batch_creation',
                'data': {'batch_id': batch.batch_id},
                'status': 'confirmed',
                'block_number': 12345 + batches.index(batch)
            }
        )
        if created:
            print(f"  ✅ Created blockchain transaction for {batch.batch_id}")
        
        # Create record
        rec_hash = '0x' + str(uuid.uuid4()).replace('-', '')[:64]
        record, created = BlockchainRecord.objects.get_or_create(
            batch_id=batch.batch_id,
            defaults={
                'origin': 'Hill Valley Apiary, Lucknow',
                'transaction_hash': rec_hash,
                'block_number': 12345 + batches.index(batch),
                'honey_type': batch.honey_type,
                'quantity': batch.total_quantity,
                'quality_score': 90
            }
        )
        if created:
            print(f"  ✅ Created blockchain record for {batch.batch_id}")
        
        # Create QR code
        qr, created = QRCode.objects.get_or_create(
            batch=batch,
            defaults={
                'code_data': f'https://honeychain.example.com/verify/{batch.batch_id}',
                'scans': 0
            }
        )
        if created:
            print(f"  ✅ Created QR code for {batch.batch_id}")


def seed_distributors(users, batches):
    """Create distributor data"""
    print("\n🚚 Creating Distributors...")
    
    dist, created = Distributor.objects.get_or_create(
        user=users['distributor1'],
        defaults={
            'company_name': 'Premium Honey Distributors',
            'registration_number': 'DIST-2026-001',
            'location': 'Delhi',
            'phone': '9876543210',
            'email': 'dist@honey.com',
            'storage_capacity': 500.0
        }
    )
    if created:
        print(f"  ✅ Created distributor: {dist.company_name}")
    
    # Create shipment
    if batches:
        ship, created = Shipment.objects.get_or_create(
            distributor=dist,
            batch_id=batches[0].batch_id,
            defaults={
                'destination': 'Mumbai, Maharashtra',
                'quantity': batches[0].total_quantity,
                'expected_delivery': timezone.now() + timedelta(days=5),
                'status': 'in_transit',
                'tracking_number': 'TRACK-2026-001'
            }
        )
        if created:
            print(f"  ✅ Created shipment: {ship.tracking_number}")
        
        # Create inventory
        inv, created = Inventory.objects.get_or_create(
            distributor=dist,
            batch_id=batches[0].batch_id,
            defaults={
                'honey_type': batches[0].honey_type,
                'quantity': batches[0].total_quantity,
                'received_date': timezone.now(),
                'expiry_date': (timezone.now() + timedelta(days=365)).date(),
                'quality_score': 90,
                'storage_location': 'Warehouse A'
            }
        )
        if created:
            print(f"  ✅ Created inventory record")


def seed_retailers(users, batches):
    """Create retailer data"""
    print("\n🏪 Creating Retailers...")
    
    ret, created = Retailer.objects.get_or_create(
        user=users['retailer1'],
        defaults={
            'store_name': 'Organic Honey Store',
            'store_type': 'both',
            'location': 'Bangalore',
            'phone': '9876543211',
            'email': 'retail@honey.com'
        }
    )
    if created:
        print(f"  ✅ Created retailer: {ret.store_name}")
    
    # Create product
    if batches:
        prod, created = Product.objects.get_or_create(
            retailer=ret,
            batch_id=batches[0].batch_id,
            defaults={
                'name': 'Premium Multifloral Honey 500g',
                'honey_type': batches[0].honey_type,
                'price': 500.0,
                'quantity_available': 100.0,
                'quality_score': 90
            }
        )
        if created:
            print(f"  ✅ Created product: {prod.name}")
        
        # Create sale
        sale, created = Sale.objects.get_or_create(
            product=prod,
            customer_name='Rajesh Sharma',
            defaults={
                'quantity': 5.0,
                'total_amount': 2500.0,
                'payment_method': 'online'
            }
        )
        if created:
            print(f"  ✅ Created sale transaction")


def seed_consumers(users, batches):
    """Create consumer data"""
    print("\n👤 Creating Consumers...")
    
    for username in ['consumer1', 'consumer2']:
        cons, created = Consumer.objects.get_or_create(
            user=users[username],
            defaults={
                'phone': '9876543212',
                'address': '123 Main Street',
                'city': 'Bangalore',
                'state': 'Karnataka',
                'postal_code': '560001'
            }
        )
        if created:
            print(f"  ✅ Created consumer: {users[username].first_name}")


def seed_notifications(users):
    """Create notification preferences"""
    print("\n🔔 Creating Notification Preferences...")
    
    for username in ['consumer1', 'consumer2']:
        pref, created = NotificationPreference.objects.get_or_create(
            user=users[username],
            defaults={
                'email_notifications': True,
                'push_notifications': True,
                'notify_shipments': True,
                'notify_quality': True,
                'notify_health': True
            }
        )
        if created:
            print(f"  ✅ Created notification preferences")


def main():
    """Run all seeding functions"""
    print("\n" + "="*60)
    print("  🍯 HONEY CHAIN DATABASE SEEDING")
    print("="*60)
    
    try:
        users = seed_users()
        profiles = seed_beekeepers(users)
        apiaries = seed_apiaries(users)
        hives = seed_hives(apiaries)
        seed_sensor_data(hives)
        seed_hive_health(hives)
        harvests = seed_harvests(hives)
        batches = seed_batches(harvests)
        seed_quality_tests(batches)
        seed_blockchain(batches, users)
        seed_distributors(users, batches)
        seed_retailers(users, batches)
        seed_consumers(users, batches)
        seed_notifications(users)
        
        print("\n" + "="*60)
        print("  ✅ DATABASE SEEDING COMPLETE!")
        print("="*60 + "\n")
        
    except Exception as e:
        print(f"\n❌ Error during seeding: {str(e)}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
