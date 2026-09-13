# 🍯 HONEY CHAIN - GETTING STARTED GUIDE

**Complete guide combining setup, next steps, and usage instructions in one file.**

---

## 📋 TABLE OF CONTENTS

1. [Initial Setup (5 minutes)](#initial-setup)
2. [Next Steps After Setup](#next-steps)
3. [How to Use Each Module](#how-to-use)
4. [Common Workflows](#workflows)
5. [API Usage Examples](#api-examples)
6. [Troubleshooting](#troubleshooting)

---

## 🚀 INITIAL SETUP (5 MINUTES)

### Step 1: Navigate to Project
```bash
cd honey_chain
```

### Step 2: Create & Activate Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install All Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Setup Database
```bash
# Create migration files
python manage.py makemigrations

# Apply migrations to database
python manage.py migrate

# Create admin account
python manage.py createsuperuser
# Enter: admin
# Password: admin123
```

### Step 5: Start Development Server
```bash
python manage.py runserver
```

**Access points:**
- Admin Panel: http://localhost:8000/admin/ (admin/admin123)
- API Root: http://localhost:8000/api/
- Beekeeper API: http://localhost:8000/api/beekeeper/profiles/

---

## ✅ NEXT STEPS AFTER SETUP

### Step 1: Verify Everything Works (5 minutes)

**Run Comprehensive Tests:**
```bash
python manage.py test_features
```

**Expected Output:**
```
✅ Test 1: User Creation
✅ Test 2: Beekeeper Profile
... (all 24 tests)
✅ ALL TESTS PASSED: 24/24
```

If all tests pass ✅, your system is ready!

### Step 2: Seed Sample Data (Optional, 2 minutes)

Create 50+ realistic test records:
```bash
python manage.py shell < scripts/seed_database.py
```

**What gets created:**
- 6 sample users
- 2 beekeeper profiles
- 3 apiaries with hives
- Sensor data for 7 days (28+ readings)
- 2-3 harvests per hive
- Blockchain records
- Distributor/Retailer/Consumer data

### Step 3: Explore Admin Panel (5 minutes)

1. Go to: http://localhost:8000/admin/
2. Login: admin / admin123
3. Click on each app to see:
   - Beekeeper → BeekeeperProfiles, Apiaries
   - Hive → Hives, Health records
   - Sensor → Sensor data
   - Batch → Honey batches
   - Processing → Quality tests
   - Blockchain → Transactions & records
   - And 7 more apps...

### Step 4: Test API Endpoints (5 minutes)

**Get Authentication Token:**
```bash
curl -X POST http://localhost:8000/api-token-auth/ \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "admin123"}'
```

**Response:**
```json
{"token": "abc123def456..."}
```

**Test API Endpoint:**
```bash
curl -H "Authorization: Token YOUR_TOKEN" \
  http://localhost:8000/api/beekeeper/profiles/
```

### Step 5: Start IoT Simulator (Optional, 2 minutes)

**Continuous Mode:**
```bash
python scripts/start_iot_simulator.py
```

**Demo Mode (10 readings):**
```bash
python scripts/start_iot_simulator.py --demo
```

**What you'll see:**
```
📊 Reading #1 - 14:23:45
  HIVE-001: HEALTHY
    ✅ Temperature: 32.5 °C
    ✅ Humidity: 65.0 %
    ✅ Weight: 15.2 kg
    ✅ Sound: 78.5 dB
  ...
```

---

## 🎯 HOW TO USE EACH MODULE

### 1. **Admin Panel** - Visual Management

**Access:** http://localhost:8000/admin/

**What you can do:**
- View all data in database
- Create, edit, delete records
- Manage users and permissions
- View audit logs

**Step-by-step:**
1. Login with admin/admin123
2. Click on any app (Beekeeper, Hive, Sensor, etc.)
3. View list of records
4. Click on any record to edit
5. Make changes and save

### 2. **REST API** - Programmatic Access

**Get Token:**
```bash
curl -X POST http://localhost:8000/api-token-auth/ \
  -H "Content-Type: application/json" \
  -d '{"username":"admin","password":"admin123"}'
```

**Use Token in Requests:**
```bash
# Set token as environment variable
TOKEN="your_token_here"

# Example: Get all beekeeper profiles
curl -H "Authorization: Token $TOKEN" \
  http://localhost:8000/api/beekeeper/profiles/
```

**Common Operations:**

**1. List Records:**
```bash
curl -H "Authorization: Token $TOKEN" \
  http://localhost:8000/api/beekeeper/profiles/
```

**2. Create Record:**
```bash
curl -X POST http://localhost:8000/api/beekeeper/profiles/ \
  -H "Authorization: Token $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "user": 1,
    "years_of_experience": 5,
    "total_hives": 25,
    "avg_honey_yield": 12.5,
    "certification": "ISO 9001 Certified"
  }'
```

**3. Update Record:**
```bash
curl -X PATCH http://localhost:8000/api/beekeeper/profiles/1/ \
  -H "Authorization: Token $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"total_hives": 30}'
```

**4. Delete Record:**
```bash
curl -X DELETE http://localhost:8000/api/beekeeper/profiles/1/ \
  -H "Authorization: Token $TOKEN"
```

### 3. **Django Shell** - Interactive Python

**Access Shell:**
```bash
python manage.py shell
```

**Example: Query Beekeepers**
```python
>>> from apps.beekeeper.models import BeekeeperProfile
>>> BeekeeperProfile.objects.all()
<QuerySet [<BeekeeperProfile: Rajesh Kumar>]>

>>> profile = BeekeeperProfile.objects.first()
>>> profile.total_hives
50

>>> profile.avg_honey_yield
15.5
```

**Example: Create Apiary**
```python
>>> from apps.beekeeper.models import Apiary
>>> from django.contrib.auth.models import User

>>> user = User.objects.first()
>>> apiary = Apiary.objects.create(
...     beekeeper=BeekeeperProfile.objects.first(),
...     name="Test Apiary",
...     location="Test Location",
...     latitude=26.8467,
...     longitude=80.9462,
...     total_hives=20
... )
>>> print(apiary.name)
Test Apiary
```

**Exit Shell:**
```python
>>> exit()
```

### 4. **IoT Simulator** - Generate Sensor Data

**Continuous Mode:**
```bash
python scripts/start_iot_simulator.py
```

**Use in Python:**
```python
from iot.simulator import IoTSimulator

# Create simulator for 5 hives
simulator = IoTSimulator(hive_count=5)

# Get readings from all hives
for i in range(10):
    data = simulator.simulate_all()
    print(f"Timestamp: {data['timestamp']}")
    print(f"Total Alerts: {data['total_alerts']}")
```

**Export Data:**
```python
# Export to JSON
simulator.export_to_json("iot_data.json")
```

### 5. **AI Analysis** - Health & Predictions

**Health Analysis:**
```python
from ai.analyzer import HiveHealthAnalyzer
from apps.sensor.models import SensorData

analyzer = HiveHealthAnalyzer()

# Get sensor readings
readings = [
    {"sensor_type": "temperature", "value": 32.5, "unit": "°C"},
    {"sensor_type": "humidity", "value": 65.0, "unit": "%"},
    {"sensor_type": "weight", "value": 15.2, "unit": "kg"},
    {"sensor_type": "sound", "value": 78.5, "unit": "dB"},
]

# Analyze
health = analyzer.analyze_readings(readings)
print(f"Health Score: {health['health_score']}/100")
print(f"Status: {health['overall_health']}")
print(f"Alerts: {health['alerts']}")
print(f"Recommendations: {health['recommendations']}")
```

**Disease Prediction:**
```python
from ai.analyzer import DiseasePredictor

predictor = DiseasePredictor()

diseases = predictor.predict_diseases(readings)
print(f"Overall Risk: {diseases['overall_risk']}")
for disease in diseases['diseases']:
    print(f"- {disease['disease']}: {disease['confidence']}%")
```

**Yield Prediction:**
```python
from ai.analyzer import YieldPredictor

yield_pred = YieldPredictor()

# Weight progression over time
weight_progression = [13.5, 14.0, 14.5, 15.0, 15.2, 15.5]

# Predict yield
yield_est = yield_pred.predict_yield(weight_progression, days_until_harvest=30)
print(f"Estimated Honey Yield: {yield_est['estimated_honey_yield']}kg")
print(f"Confidence: {yield_est['confidence']}%")
print(f"Recommendation: {yield_est['recommendation']}")
```

### 6. **Database Seeding** - Create Test Data

**Seed All Data:**
```bash
python manage.py shell < scripts/seed_database.py
```

**Manual Seeding (Python Shell):**
```python
from django.contrib.auth.models import User
from apps.beekeeper.models import BeekeeperProfile, Apiary

# Create user
user = User.objects.create_user(
    username='beekeeper1',
    email='beekeeper@example.com',
    password='pass123'
)

# Create beekeeper profile
profile = BeekeeperProfile.objects.create(
    user=user,
    years_of_experience=10,
    total_hives=50,
    avg_honey_yield=15.5,
    certification="ISO 9001"
)

# Create apiary
apiary = Apiary.objects.create(
    beekeeper=profile,
    name="Main Apiary",
    location="Lucknow",
    latitude=26.8467,
    longitude=80.9462,
    total_hives=50
)

print(f"Created: {apiary.name}")
```

---

## 📊 COMMON WORKFLOWS

### Workflow 1: Track Honey from Hive to Consumer

**Step 1: Record Sensor Data (IoT)**
```bash
# Manually in admin or API
# POST /api/sensor/data/
{
  "hive": 1,
  "sensor_type": "weight",
  "value": 15.2,
  "unit": "kg"
}
```

**Step 2: Record Harvest**
```bash
# POST /api/harvest/records/
{
  "hive": 1,
  "harvest_date": "2024-12-01",
  "quantity": 12.5,
  "honey_type": "Multifloral",
  "color_grade": "Amber"
}
```

**Step 3: Create Batch**
```bash
# POST /api/batch/batches/
{
  "batch_id": "BATCH-2024-001",
  "total_quantity": 50.0,
  "honey_type": "Premium Multifloral",
  "status": "created"
}
```

**Step 4: Quality Testing**
```bash
# POST /api/processing/quality/
{
  "batch": 1,
  "acidity": 3.5,
  "moisture": 17.2,
  "color_intensity": 95,
  "aroma_grade": "excellent",
  "is_approved": true
}
```

**Step 5: Generate QR Code**
```bash
# POST /api/qr/codes/
{
  "batch": 1,
  "code_data": "https://honeychain.com/verify/BATCH-2024-001"
}
```

**Step 6: Track Shipment**
```bash
# POST /api/distributor/shipments/
{
  "distributor": 1,
  "batch_id": "BATCH-2024-001",
  "destination": "Mumbai",
  "quantity": 50.0,
  "status": "in_transit"
}
```

**Step 7: Record Sale**
```bash
# POST /api/retailer/sales/
{
  "product": 1,
  "customer_name": "John Doe",
  "quantity": 5.0,
  "total_amount": 2500.0
}
```

**Step 8: Consumer Purchase & Review**
```bash
# POST /api/consumer/purchases/
{
  "consumer": 1,
  "product_id": 1,
  "quantity": 1,
  "price": 500.0
}

# POST /api/consumer/reviews/
{
  "purchase": 1,
  "rating": 5,
  "comment": "Excellent honey!"
}
```

### Workflow 2: Monitor Hive Health

**Step 1: Get Real-time Sensor Data**
```python
from apps.sensor.models import SensorData

# Get latest readings for a hive
sensors = SensorData.objects.filter(
    hive_id=1
).order_by('-timestamp')[:4]

for sensor in sensors:
    print(f"{sensor.sensor_type}: {sensor.value} {sensor.unit}")
```

**Step 2: Analyze Health**
```python
from ai.analyzer import HiveHealthAnalyzer

analyzer = HiveHealthAnalyzer()

# Convert to readable format
readings = [
    {"sensor_type": s.sensor_type, "value": s.value, "unit": s.unit}
    for s in sensors
]

health = analyzer.analyze_readings(readings)
print(f"Health Score: {health['health_score']}/100")
print(f"Recommendations: {health['recommendations']}")
```

**Step 3: Predict Diseases**
```python
from ai.analyzer import DiseasePredictor

predictor = DiseasePredictor()
diseases = predictor.predict_diseases(readings)

if diseases['overall_risk'] == 'critical':
    print("⚠️ ALERT: Disease risk detected!")
    for disease in diseases['diseases']:
        print(f"  - {disease['disease']}: {disease['recommended_action']}")
```

**Step 4: Send Notification**
```python
from apps.notifications.models import Notification

if health['overall_health'] == 'critical':
    Notification.objects.create(
        user=hive.apiary.beekeeper.user,
        title="Hive Health Alert",
        message=f"Hive {hive.hive_id} health score: {health['health_score']}/100",
        notification_type="health_alert"
    )
```

### Workflow 3: Generate Yield Forecasts

**Step 1: Collect Weight Data**
```python
from apps.sensor.models import SensorData
from datetime import timedelta
from django.utils import timezone

# Get weight readings for last 30 days
thirty_days_ago = timezone.now() - timedelta(days=30)
weights = SensorData.objects.filter(
    hive_id=1,
    sensor_type='weight',
    timestamp__gte=thirty_days_ago
).order_by('timestamp').values_list('value', flat=True)
```

**Step 2: Predict Yield**
```python
from ai.analyzer import YieldPredictor

yield_pred = YieldPredictor()
prediction = yield_pred.predict_yield(list(weights), days_until_harvest=30)

print(f"Current Weight: {prediction['current_weight']}kg")
print(f"Estimated Harvest Weight: {prediction['estimated_harvest_weight']}kg")
print(f"Estimated Honey Yield: {prediction['estimated_honey_yield']}kg")
print(f"Confidence: {prediction['confidence']}%")
```

**Step 3: Take Action**
```python
if prediction['estimated_honey_yield'] < 10:
    # Send recommendation to beekeeper
    Notification.objects.create(
        user=hive.apiary.beekeeper.user,
        title="Yield Warning",
        message=prediction['recommendation'],
        notification_type="yield_warning"
    )
```

---

## 💻 API EXAMPLES

### Complete API Usage Examples

**1. Authentication**
```bash
# Get Token
curl -X POST http://localhost:8000/api-token-auth/ \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "admin123"}'

# Save token
export TOKEN="your_token_here"
```

**2. Create Beekeeper**
```bash
curl -X POST http://localhost:8000/api/beekeeper/profiles/ \
  -H "Authorization: Token $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "user": 2,
    "years_of_experience": 8,
    "total_hives": 50,
    "avg_honey_yield": 15.5,
    "certification": "ISO 9001 Certified"
  }'
```

**3. Create Apiary**
```bash
curl -X POST http://localhost:8000/api/beekeeper/apiaries/ \
  -H "Authorization: Token $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "beekeeper": 1,
    "name": "Main Apiary",
    "location": "Lucknow, UP",
    "latitude": 26.8467,
    "longitude": 80.9462,
    "total_hives": 50,
    "description": "Primary honey production facility"
  }'
```

**4. Record Sensor Data**
```bash
curl -X POST http://localhost:8000/api/sensor/data/ \
  -H "Authorization: Token $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "hive": 1,
    "sensor_type": "temperature",
    "sensor_id": "SENSOR-TEMP-001",
    "value": 32.5,
    "unit": "°C"
  }'
```

**5. Create Harvest**
```bash
curl -X POST http://localhost:8000/api/harvest/records/ \
  -H "Authorization: Token $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "hive": 1,
    "harvest_date": "2024-12-01",
    "quantity": 12.5,
    "honey_type": "Multifloral",
    "color_grade": "Amber",
    "notes": "Good quality harvest"
  }'
```

**6. Create Batch**
```bash
curl -X POST http://localhost:8000/api/batch/batches/ \
  -H "Authorization: Token $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "batch_id": "BATCH-2024-001",
    "total_quantity": 50.0,
    "honey_type": "Premium Multifloral",
    "status": "created"
  }'
```

**7. Quality Testing**
```bash
curl -X POST http://localhost:8000/api/processing/quality/ \
  -H "Authorization: Token $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "batch": 1,
    "acidity": 3.5,
    "moisture": 17.2,
    "color_intensity": 95,
    "aroma_grade": "excellent",
    "is_approved": true
  }'
```

**8. Get API Data (List)**
```bash
# Get all beekeeper profiles
curl -H "Authorization: Token $TOKEN" \
  http://localhost:8000/api/beekeeper/profiles/

# Get all hives for apiary 1
curl -H "Authorization: Token $TOKEN" \
  http://localhost:8000/api/hive/hives/?apiary=1

# Get sensor data for hive 1
curl -H "Authorization: Token $TOKEN" \
  http://localhost:8000/api/sensor/data/?hive=1
```

---

## 🐛 TROUBLESHOOTING

### Issue 1: "ModuleNotFoundError: No module named 'django'"

**Problem:** Django not installed

**Solution:**
```bash
pip install -r requirements.txt
```

**Verify:**
```bash
python -c "import django; print(django.__version__)"
```

### Issue 2: "SQLite3 database error"

**Problem:** Database not initialized or migrations not applied

**Solution:**
```bash
python manage.py migrate
```

**Verify:**
```bash
python manage.py showmigrations
```

### Issue 3: "sqlite3.OperationalError: no such table"

**Problem:** Migrations not applied

**Solution:**
```bash
python manage.py makemigrations
python manage.py migrate
```

### Issue 4: "Port 8000 already in use"

**Problem:** Another process using port 8000

**Solution:**
```bash
# Use different port
python manage.py runserver 8080

# Or kill process on port 8000 (Windows)
netstat -ano | findstr :8000
taskkill /PID <PID> /F

# Or kill process on port 8000 (Linux/Mac)
lsof -ti:8000 | xargs kill -9
```

### Issue 5: "FOREIGN KEY constraint failed"

**Problem:** Missing related data

**Solution:**
```bash
# Seed sample data first
python manage.py shell < scripts/seed_database.py
```

### Issue 6: "Permission denied" on migrations

**Problem:** File permissions issue

**Solution:**
```bash
# Regenerate migrations
python manage.py makemigrations
```

### Issue 7: API returns "401 Unauthorized"

**Problem:** Missing or invalid authentication token

**Solution:**
```bash
# Get new token
curl -X POST http://localhost:8000/api-token-auth/ \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "admin123"}'

# Use token in header
curl -H "Authorization: Token YOUR_TOKEN" \
  http://localhost:8000/api/beekeeper/profiles/
```

### Issue 8: Tests failing

**Problem:** Various causes

**Solution:**
```bash
# Check database
python manage.py migrate

# Seed data
python manage.py shell < scripts/seed_database.py

# Run tests again
python manage.py test_features
```

---

## 📚 USEFUL COMMANDS REFERENCE

### Database Commands
```bash
python manage.py makemigrations          # Create migrations
python manage.py migrate                 # Apply migrations
python manage.py migrate --fake-initial  # Skip initial migration
python manage.py showmigrations          # Show migration status
python manage.py sqlmigrate app 0001    # Show SQL for migration
```

### User & Admin Commands
```bash
python manage.py createsuperuser         # Create admin
python manage.py changepassword username # Change password
python manage.py shell                   # Interactive shell
```

### Server Commands
```bash
python manage.py runserver               # Start dev server
python manage.py runserver 0.0.0.0:8000  # Public access
python manage.py runserver 8080          # Different port
```

### Testing & Data Commands
```bash
python manage.py test_features           # Run all tests
python manage.py test                    # Run pytest
python manage.py shell < scripts/seed_database.py  # Seed data
```

### Backup & Restore
```bash
python manage.py dumpdata > backup.json  # Backup database
python manage.py loaddata backup.json    # Restore database
python manage.py dumpdata app_name > app_backup.json  # Backup app
```

---

## ✅ VERIFICATION CHECKLIST

After completing setup and next steps:

- [ ] Virtual environment created and activated
- [ ] All dependencies installed (`pip list` shows 80+ packages)
- [ ] Database migrations applied (no errors)
- [ ] Superuser created (admin/admin123)
- [ ] Development server starts without errors
- [ ] Admin panel accessible and working
- [ ] All 24 tests passing
- [ ] API endpoints responding
- [ ] Sample data seeded (optional)
- [ ] IoT simulator running (optional)
- [ ] AI analyzer working (optional)

**All checked?** ✅ **You're ready to go!**

---

## 🎯 COMMON TASKS QUICK REFERENCE

| Task | Command |
|------|---------|
| Start server | `python manage.py runserver` |
| Run tests | `python manage.py test_features` |
| Seed data | `python manage.py shell < scripts/seed_database.py` |
| Access admin | http://localhost:8000/admin/ |
| Interactive shell | `python manage.py shell` |
| Run IoT simulator | `python scripts/start_iot_simulator.py` |
| Create superuser | `python manage.py createsuperuser` |
| Apply migrations | `python manage.py migrate` |

---

## 📞 NEED MORE HELP?

| Topic | See This File |
|-------|---------------|
| Quick setup | README.md |
| API usage | API_REFERENCE.md |
| Features list | FEATURES_VERIFIED.md |
| All commands | QUICK_REFERENCE.md |
| Project status | IMPLEMENTATION_STATUS.md |
| Python workflows | Django shell section above |

---

**Status**: ✅ Complete  
**Version**: 1.0.0  
**Last Updated**: December 2024

**Now you're ready! Follow the steps above and enjoy building with Honey Chain! 🍯**
