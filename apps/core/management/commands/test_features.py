"""
Management command to test all features
Run with: python manage.py test_features
"""
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from apps.beekeeper.models import Apiary, BeekeeperProfile
from apps.hive.models import Hive, HiveHealth
from apps.harvest.models import Harvest
from apps.batch.models import HoneyBatch
from apps.blockchain.models import BlockchainTransaction, BlockchainRecord
from apps.qr.models import QRCode
from apps.sensor.models import SensorData
from apps.processing.models import Processing, QualityTest
from apps.distributor.models import Distributor, Shipment, Inventory
from apps.retailer.models import Retailer, Product, Sale
from apps.consumer.models import Consumer, Purchase, Review
from apps.notifications.models import Notification, NotificationPreference


class Command(BaseCommand):
    help = 'Test all Honey Chain features'

    def handle(self, *args, **options):
        import time
        import uuid
        
        self.stdout.write("\n\n" + "="*60)
        self.stdout.write("  🍯 HONEY CHAIN - COMPREHENSIVE FEATURE TEST 🍯")
        self.stdout.write("="*60)
        
        try:
            # Generate unique test data suffix
            test_id = str(int(time.time()))
            
            # Clean up old test data
            User.objects.filter(username__startswith='test_').delete()
            HoneyBatch.objects.all().delete()
            BlockchainTransaction.objects.all().delete()
            BlockchainRecord.objects.all().delete()
            
            # TEST 1: User Creation
            self.stdout.write("\n✓ TEST 1: User Creation & Authentication")
            user = User.objects.create_user(
                username='test_beekeeper',
                email='beekeeper@example.com',
                password='testpass123',
                first_name='Ramesh',
                last_name='Kumar'
            )
            self.stdout.write(f"  ✅ User '{user.username}' created")
            
            # TEST 2: Beekeeper Profile
            self.stdout.write("\n✓ TEST 2: Beekeeper Profile Management")
            profile = BeekeeperProfile.objects.create(
                user=user,
                years_of_experience=8,
                total_hives=45,
                avg_honey_yield=12.5,
                certification='ISO 9001'
            )
            self.stdout.write(f"  ✅ Beekeeper profile created")
            
            # TEST 3: Apiary
            self.stdout.write("\n✓ TEST 3: Apiary Management")
            apiary = Apiary.objects.create(
                beekeeper=user,
                name='Hill Valley Apiary',
                location='Lucknow, Uttar Pradesh',
                latitude=26.8467,
                longitude=80.9462,
                total_hives=45
            )
            self.stdout.write(f"  ✅ Apiary '{apiary.name}' created")
            
            # TEST 4: Hive
            self.stdout.write("\n✓ TEST 4: Hive Management")
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
            self.stdout.write(f"  ✅ Hive '{hive.hive_id}' created")
            
            # TEST 5: Hive Health
            self.stdout.write("\n✓ TEST 5: Hive Health Metrics")
            health = HiveHealth.objects.create(
                hive=hive,
                temperature=32.5,
                humidity=65.0,
                weight=15.2,
                bee_activity=85,
                disease_risk='low'
            )
            self.stdout.write(f"  ✅ Health metrics created")
            
            # TEST 6: Sensor Data
            self.stdout.write("\n✓ TEST 6: IoT Sensor Data Collection")
            sensors_data = []
            for sensor_type, unit, value in [
                ('temperature', '°C', 32.5),
                ('humidity', '%', 65.0),
                ('weight', 'kg', 15.2),
                ('sound', 'dB', 78.5)
            ]:
                sensor = SensorData.objects.create(
                    hive=hive,
                    sensor_type=sensor_type,
                    sensor_id=f'SENSOR-{sensor_type.upper()}-001',
                    value=value,
                    unit=unit
                )
                sensors_data.append(sensor)
            self.stdout.write(f"  ✅ {len(sensors_data)} sensor data points created")
            
            # TEST 7: Harvest
            self.stdout.write("\n✓ TEST 7: Harvest Recording")
            harvest = Harvest.objects.create(
                hive=hive,
                harvest_date='2026-09-01',
                quantity=12.5,
                honey_type='multifloral',
                color_grade='amber'
            )
            self.stdout.write(f"  ✅ Harvest recorded: {harvest.quantity} kg")
            
            # TEST 8: Honey Batch
            self.stdout.write("\n✓ TEST 8: Honey Batch Management")
            batch_id = f'BATCH-{test_id}'
            batch = HoneyBatch.objects.create(
                batch_id=batch_id,
                total_quantity=50.0,
                honey_type='Premium Multifloral',
                status='created'
            )
            batch.harvests.add(harvest)
            self.stdout.write(f"  ✅ Batch '{batch.batch_id}' created")
            
            # TEST 9: Quality Test
            self.stdout.write("\n✓ TEST 9: Quality Testing & Assurance")
            quality = QualityTest.objects.create(
                batch=batch,
                acidity=3.5,
                moisture=17.2,
                color_intensity=95,
                aroma_grade='excellent',
                is_approved=True
            )
            self.stdout.write(f"  ✅ Quality test completed")
            
            # TEST 10: Processing
            self.stdout.write("\n✓ TEST 10: Processing Workflows")
            processing = Processing.objects.create(
                batch=batch,
                temperature=60,
                duration=120
            )
            self.stdout.write(f"  ✅ Processing record created")
            
            # TEST 11: Blockchain Transaction
            self.stdout.write("\n✓ TEST 11: Blockchain Transactions ⛓️")
            admin_user = User.objects.filter(is_superuser=True).first()
            tx_hash = '0x' + str(uuid.uuid4()).replace('-', '')[:64]
            blockchain_tx = BlockchainTransaction.objects.create(
                user=admin_user,
                batch_id=batch.batch_id,
                transaction_hash=tx_hash,
                transaction_type='batch_creation',
                data={'batch_id': batch.batch_id},
                status='confirmed',
                block_number=12345
            )
            self.stdout.write(f"  ✅ Blockchain transaction created")
            
            # TEST 12: Blockchain Record
            self.stdout.write("\n✓ TEST 12: Blockchain Records")
            record_hash = '0x' + str(uuid.uuid4()).replace('-', '')[:64]
            record = BlockchainRecord.objects.create(
                batch_id=batch.batch_id,
                origin='Hill Valley Apiary',
                transaction_hash=record_hash,
                block_number=12345,
                honey_type=batch.honey_type,
                quantity=batch.total_quantity,
                quality_score=90
            )
            self.stdout.write(f"  ✅ Blockchain record created")
            
            # TEST 13: QR Code
            self.stdout.write("\n✓ TEST 13: QR Code Generation")
            qr = QRCode.objects.create(
                batch=batch,
                code_data=f'https://honeychain.example.com/verify/{batch.batch_id}',
                scans=0
            )
            self.stdout.write(f"  ✅ QR code created")
            
            # TEST 14: Distributor
            self.stdout.write("\n✓ TEST 14: Distributor Management")
            distributor_user = User.objects.create_user(
                username='distributor1',
                email='distributor@example.com',
                password='dist123',
                first_name='Rajesh',
                last_name='Singh'
            )
            distributor = Distributor.objects.create(
                user=distributor_user,
                company_name='Premium Honey Distributors',
                registration_number='DIST-001',
                location='Delhi',
                phone='9876543210',
                email='dist@example.com',
                storage_capacity=500.0
            )
            self.stdout.write(f"  ✅ Distributor '{distributor.company_name}' created")
            
            # TEST 15: Shipment
            self.stdout.write("\n✓ TEST 15: Shipment Tracking")
            from django.utils import timezone
            shipment = Shipment.objects.create(
                distributor=distributor,
                batch_id=batch.batch_id,
                destination='Mumbai, Maharashtra',
                quantity=batch.total_quantity,
                expected_delivery=timezone.now(),
                status='in_transit',
                tracking_number='TRACK-001'
            )
            self.stdout.write(f"  ✅ Shipment created: {shipment.tracking_number}")
            
            # TEST 16: Inventory
            self.stdout.write("\n✓ TEST 16: Distributor Inventory")
            from datetime import timedelta
            inventory = Inventory.objects.create(
                distributor=distributor,
                batch_id=batch.batch_id,
                honey_type=batch.honey_type,
                quantity=batch.total_quantity,
                received_date=timezone.now(),
                expiry_date=(timezone.now() + timedelta(days=365)).date(),
                quality_score=90,
                storage_location='Warehouse A'
            )
            self.stdout.write(f"  ✅ Inventory created: {inventory.quantity}kg in stock")
            
            # TEST 17: Retailer
            self.stdout.write("\n✓ TEST 17: Retailer Management")
            retailer_user = User.objects.create_user(
                username='retailer1',
                email='retailer@example.com',
                password='ret123',
                first_name='Pavan',
                last_name='Patel'
            )
            retailer = Retailer.objects.create(
                user=retailer_user,
                store_name='Organic Honey Store',
                store_type='both',
                location='Bangalore',
                phone='9876543211',
                email='retail@example.com'
            )
            self.stdout.write(f"  ✅ Retailer '{retailer.store_name}' created")
            
            # TEST 18: Product
            self.stdout.write("\n✓ TEST 18: Retail Products")
            product = Product.objects.create(
                retailer=retailer,
                name='Premium Multifloral Honey 500g',
                batch_id=batch.batch_id,
                honey_type=batch.honey_type,
                price=500.0,
                quantity_available=100.0,
                quality_score=90
            )
            self.stdout.write(f"  ✅ Product '{product.name}' created")
            
            # TEST 19: Sale
            self.stdout.write("\n✓ TEST 19: Retail Sales")
            sale = Sale.objects.create(
                product=product,
                quantity=5.0,
                total_amount=2500.0,
                customer_name='Amit Kumar',
                customer_email='customer@example.com',
                payment_method='online'
            )
            self.stdout.write(f"  ✅ Sale completed: {sale.quantity}kg @ ₹{sale.total_amount}")
            
            # TEST 20: Consumer
            self.stdout.write("\n✓ TEST 20: Consumer Management")
            consumer_user = User.objects.create_user(
                username='consumer1',
                email='consumer@example.com',
                password='cons123',
                first_name='Anita',
                last_name='Gupta'
            )
            consumer = Consumer.objects.create(
                user=consumer_user,
                phone='9876543212',
                address='123 Main Street',
                city='Bangalore',
                state='Karnataka',
                postal_code='560001'
            )
            self.stdout.write(f"  ✅ Consumer created: {consumer.user.username}")
            
            # TEST 21: Purchase
            self.stdout.write("\n✓ TEST 21: Consumer Purchases")
            purchase = Purchase.objects.create(
                consumer=consumer,
                product_name=product.name,
                batch_id=batch.batch_id,
                quantity=2.0,
                price=500.0,
                total_amount=1000.0,
                payment_method='card'
            )
            self.stdout.write(f"  ✅ Purchase created: {purchase.quantity}kg")
            
            # TEST 22: Review
            self.stdout.write("\n✓ TEST 22: Product Reviews")
            review = Review.objects.create(
                purchase=purchase,
                rating=5,
                title='Excellent Quality Honey!',
                content='Best honey I have ever tasted. Highly recommended!'
            )
            self.stdout.write(f"  ✅ Review created: {review.rating} stars")
            
            # TEST 23: Notifications
            self.stdout.write("\n✓ TEST 23: Notifications System")
            notification = Notification.objects.create(
                user=consumer_user,
                notification_type='order',
                title='Order Confirmed',
                message='Your order has been confirmed and will be delivered soon',
                priority='high'
            )
            self.stdout.write(f"  ✅ Notification created: {notification.title}")
            
            # TEST 24: Notification Preferences
            self.stdout.write("\n✓ TEST 24: Notification Preferences")
            pref = NotificationPreference.objects.create(
                user=consumer_user,
                email_notifications=True,
                push_notifications=True
            )
            self.stdout.write(f"  ✅ Notification preferences set for {consumer_user.username}")
            
            # Summary
            self.stdout.write("\n" + "="*60)
            self.stdout.write("  ✅ ALL 24 FEATURES TESTED SUCCESSFULLY! ✅")
            self.stdout.write("="*60)
            
            print("\n📊 DATABASE STATISTICS:")
            print(f"  • Users: {User.objects.count()}")
            print(f"  • Beekeepers: {BeekeeperProfile.objects.count()}")
            print(f"  • Apiaries: {Apiary.objects.count()}")
            print(f"  • Hives: {Hive.objects.count()}")
            print(f"  • Harvests: {Harvest.objects.count()}")
            print(f"  • Honey Batches: {HoneyBatch.objects.count()}")
            print(f"  • Sensor Data Points: {SensorData.objects.count()}")
            print(f"  • Quality Tests: {QualityTest.objects.count()}")
            print(f"  • Processing Records: {Processing.objects.count()}")
            print(f"  • Blockchain Transactions: {BlockchainTransaction.objects.count()}")
            print(f"  • Blockchain Records: {BlockchainRecord.objects.count()}")
            print(f"  • QR Codes: {QRCode.objects.count()}")
            print(f"  • Distributors: {Distributor.objects.count()}")
            print(f"  • Shipments: {Shipment.objects.count()}")
            print(f"  • Inventory Records: {Inventory.objects.count()}")
            print(f"  • Retailers: {Retailer.objects.count()}")
            print(f"  • Products: {Product.objects.count()}")
            print(f"  • Sales: {Sale.objects.count()}")
            print(f"  • Consumers: {Consumer.objects.count()}")
            print(f"  • Purchases: {Purchase.objects.count()}")
            print(f"  • Reviews: {Review.objects.count()}")
            print(f"  • Notifications: {Notification.objects.count()}")
            
            self.stdout.write(self.style.SUCCESS("\n✅ All tests passed successfully!\n"))
            
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"\n❌ Test failed: {str(e)}"))
            import traceback
            traceback.print_exc()

