# 🍯 HONEY CHAIN - Blockchain-Based Honey Traceability System

## 📋 Overview

Honey Chain is a comprehensive blockchain-enabled supply chain management system for honey production, processing, and distribution. Built for the **Smart India Hackathon 2026 (Problem Statement 26021)**, it provides end-to-end traceability from beekeepers to consumers using Django REST API backend with blockchain verification.

### 🎯 Key Features

- **Beekeeper Management**: Track apiaries, hives, and bee health
- **IoT Integration**: Real-time sensor data (temperature, humidity, weight, sound)
- **Quality Assurance**: Comprehensive quality testing and grading
- **Blockchain Verification**: Immutable records of honey batches
- **QR Code Traceability**: Scan-to-verify authentication
- **Supply Chain Tracking**: From production to retail sales
- **AI Health Analysis**: Predict diseases and forecast honey yield
- **Consumer Reviews**: End-to-end transparency and feedback

---

## 🏗️ Project Structure

```
honey_chain/
├── apps/                          # 13 Django Apps
│   ├── accounts/                 # User authentication
│   ├── admin_portal/             # Admin dashboard
│   ├── batch/                    # Honey batch management
│   ├── beekeeper/                # Beekeeper profiles & apiaries
│   ├── blockchain/               # Blockchain integration
│   ├── consumer/                 # Consumer profiles
│   ├── core/                     # Core utilities
│   ├── distributor/              # Distribution & logistics
│   ├── harvest/                  # Harvest records
│   ├── hive/                     # Hive management
│   ├── notifications/            # User notifications
│   ├── processing/               # Quality testing
│   ├── qr/                       # QR code generation
│   ├── retailer/                 # Retail stores
│   └── sensor/                   # IoT sensor data
├── ai/                            # AI Analysis Module
│   ├── __init__.py
│   └── analyzer.py               # Health, disease, yield analysis
├── iot/                           # IoT Simulator
│   ├── __init__.py
│   └── simulator.py              # Sensor simulation
├── scripts/                       # Utility Scripts
│   ├── __init__.py
│   ├── seed_database.py          # Database seeding
│   └── start_iot_simulator.py    # IoT launcher
├── config/                        # Django Configuration
│   ├── settings/
│   │   ├── base.py              # Base settings
│   │   ├── dev.py               # Development
│   │   └── prod.py              # Production
│   ├── urls.py                  # Main URL routing
│   ├── wsgi.py
│   └── celery.py
├── db.sqlite3                    # Database
├── manage.py                     # Django management
├── requirements.txt              # Dependencies
└── README.md                     # This file
```

---

## ⚡ Quick Start (5 Minutes)

### Prerequisites
- Python 3.8+
- pip
- Virtual environment (recommended)

### Step 1: Clone/Extract Project
```bash
cd honey_chain
```

### Step 2: Create Virtual Environment
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

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Setup Database
```bash
# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser
# Username: admin
# Password: admin123
```

### Step 5: Seed Sample Data (Optional)
```bash
python manage.py shell < scripts/seed_database.py
```

### Step 6: Run Development Server
```bash
python manage.py runserver
```

Access at: `http://localhost:8000/admin/`

---

## 📚 Complete Setup Guide

### Installation Steps

#### 1. Environment Setup

**Create Virtual Environment**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

#### 2. Install All Dependencies
```bash
# Upgrade pip first
pip install --upgrade pip

# Install requirements
pip install -r requirements.txt
```

#### 3. Database Setup (IMPORTANT!)

**Step 1: Create Migration Files**
```bash
python manage.py makemigrations

# This command scans all models and creates migration files:
# - beekeeper/migrations/0001_initial.py
# - hive/migrations/0001_initial.py
# - harvest/migrations/0001_initial.py
# - batch/migrations/0001_initial.py
# ... (for all 13 apps)
```

**Step 2: Apply Migrations**
```bash
python manage.py migrate

# This applies migrations to database:
# - Creates db.sqlite3
# - Creates 22+ database tables
# - Sets up Django system tables
```

**Step 3: Create Superuser (Admin Account)**
```bash
python manage.py createsuperuser

# Enter when prompted:
# Username: admin
# Email: admin@example.com
# Password: admin123
# Confirm Password: admin123
```

#### 4. Seed Sample Data (Recommended)
```bash
python manage.py shell < scripts/seed_database.py

# Creates:
# - 6 sample users
# - 2 beekeeper profiles
# - 3 apiaries with hives
# - Sensor data for 7 days
# - Harvests and batches
# - Blockchain records
# - Distributors, retailers, consumers
```

#### 5. Run Tests
```bash
python manage.py test_features

# Should show 24/24 tests passing:
# ✅ Test 1: User Creation
# ✅ Test 2: Beekeeper Profile
# ... (24 total)
```

#### 6. Start Development Server
```bash
python manage.py runserver

# Server starts at: http://127.0.0.1:8000/
# Admin Panel: http://127.0.0.1:8000/admin/
# API Root: http://127.0.0.1:8000/api/
```

---

## 🚀 Running the Application

### Start Django Server
```bash
python manage.py runserver 0.0.0.0:8000
```

**Access Points:**
- Admin Panel: `http://localhost:8000/admin/`
- API Root: `http://localhost:8000/api/`
- Beekeeper: `http://localhost:8000/api/beekeeper/profiles/`
- Hives: `http://localhost:8000/api/hive/hives/`
- Sensors: `http://localhost:8000/api/sensor/data/`

### Run IoT Simulator

**Continuous Mode:**
```bash
python scripts/start_iot_simulator.py
```

**Demo Mode (10 readings):**
```bash
python scripts/start_iot_simulator.py --demo
```

### Use AI Analysis

```python
from ai.analyzer import HiveHealthAnalyzer, DiseasePredictor

# Analyze hive health
analyzer = HiveHealthAnalyzer()
health = analyzer.analyze_readings(sensor_readings)
print(f"Health Score: {health['health_score']}/100")

# Predict diseases
predictor = DiseasePredictor()
diseases = predictor.predict_diseases(readings)
print(f"Disease Risk: {diseases['overall_risk']}")
```

---

## 🔌 API Endpoints

### Authentication
```bash
# Get token
curl -X POST http://localhost:8000/api-token-auth/ \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "admin123"}'

# Use token in requests
curl -H "Authorization: Token YOUR_TOKEN" \
  http://localhost:8000/api/beekeeper/profiles/
```

### Main API Routes

```
# Beekeeper
GET/POST  /api/beekeeper/profiles/
GET       /api/beekeeper/profiles/{id}/
GET/POST  /api/beekeeper/apiaries/
GET       /api/beekeeper/apiaries/{id}/

# Hive Management
GET/POST  /api/hive/hives/
GET       /api/hive/hives/{id}/
GET       /api/hive/health/
POST      /api/hive/health/

# Sensor Data
GET/POST  /api/sensor/data/
GET       /api/sensor/data/?hive_id=HIVE001

# Harvest & Batch
GET/POST  /api/harvest/records/
GET/POST  /api/batch/batches/

# Quality Testing
GET/POST  /api/processing/quality/

# Blockchain
GET       /api/blockchain/transactions/
GET       /api/blockchain/records/

# Supply Chain
GET       /api/distributor/shipments/
GET       /api/retailer/products/
GET       /api/consumer/purchases/

# QR Code
GET/POST  /api/qr/codes/
GET       /api/qr/codes/{batch_id}/verify/

# Notifications
GET       /api/notifications/
```

---

## 📊 Testing Features

### Run Comprehensive Tests
```bash
python manage.py test_features

# Expected Output:
# Test 1: User Creation ✅
# Test 2: Beekeeper Profile ✅
# Test 3: Apiary Creation ✅
# ... (24 total tests)
# ✅ ALL TESTS PASSED: 24/24
```

### Test Individual Components
```bash
# Test shell access
python manage.py shell

# Count users
>>> from django.contrib.auth.models import User
>>> User.objects.all().count()

# Get hives
>>> from apps.hive.models import Hive
>>> Hive.objects.all()

# Check sensor data
>>> from apps.sensor.models import SensorData
>>> SensorData.objects.count()
```

---

## 🗄️ Database Schema

### 13 Apps, 30+ Models, 22+ Tables

**Beekeeper App**
- BeekeeperProfile
- Apiary

**Hive App**
- Hive
- HiveHealth

**Harvest App**
- Harvest

**Batch App**
- HoneyBatch
- BatchHarvest (M2M)

**Sensor App**
- SensorData

**Processing App**
- QualityTest
- Processing

**Blockchain App**
- BlockchainTransaction
- BlockchainRecord

**QR App**
- QRCode

**Distributor App**
- Distributor
- Shipment
- Inventory

**Retailer App**
- Retailer
- Product
- Sale

**Consumer App**
- Consumer
- Purchase
- Review

**Notifications App**
- Notification
- NotificationPreference

**Core & Admin**
- Custom permissions, utilities

See `FEATURES_VERIFIED.md` for complete documentation.

---

## 🔐 Authentication

### Token-Based Authentication

**Get Token:**
```bash
curl -X POST http://localhost:8000/api-token-auth/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "admin",
    "password": "admin123"
  }'

# Response: {"token": "abc123def456..."}
```

**Use Token in API Calls:**
```bash
curl -H "Authorization: Token abc123def456..." \
  http://localhost:8000/api/beekeeper/profiles/
```

**Python Example:**
```python
import requests

url = "http://localhost:8000/api/beekeeper/profiles/"
headers = {"Authorization": "Token abc123def456..."}
response = requests.get(url, headers=headers)
print(response.json())
```

---

## 📝 Example API Calls

### Create Beekeeper Profile
```bash
curl -X POST http://localhost:8000/api/beekeeper/profiles/ \
  -H "Authorization: Token YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "user": 1,
    "years_of_experience": 5,
    "total_hives": 25,
    "avg_honey_yield": 12.5,
    "certification": "ISO 9001 Certified"
  }'
```

### Record Sensor Data
```bash
curl -X POST http://localhost:8000/api/sensor/data/ \
  -H "Authorization: Token YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "hive": 1,
    "sensor_type": "temperature",
    "sensor_id": "SENSOR-TEMP-001",
    "value": 32.5,
    "unit": "°C"
  }'
```

### Create Harvest
```bash
curl -X POST http://localhost:8000/api/harvest/records/ \
  -H "Authorization: Token YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "hive": 1,
    "harvest_date": "2024-12-01",
    "quantity": 12.5,
    "honey_type": "Multifloral",
    "color_grade": "Amber"
  }'
```

---

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| "No module named django" | Run `pip install -r requirements.txt` |
| "SQLite3 database error" | Run `python manage.py migrate` |
| "ModuleNotFoundError: apps" | Ensure working directory is `honey_chain/` |
| "Port 8000 in use" | Use `python manage.py runserver 8080` |
| "FOREIGN KEY constraint" | Run `python manage.py shell < scripts/seed_database.py` |
| "Permission denied on migrations" | Run `python manage.py makemigrations` |

---

## 📦 Tech Stack

| Component | Technology | Version |
|-----------|-----------|---------|
| Framework | Django | 4.2.0 |
| API | Django REST Framework | 3.14.0 |
| Database | SQLite3/PostgreSQL | Latest |
| Blockchain | Web3.py | 6.11.0 |
| Task Queue | Celery | 5.3.4 |
| Cache | Redis | 5.0.0 |
| QR Codes | qrcode | 7.4.2 |
| Auth | DRF Token Auth | Built-in |

---

## 🛠️ Development Commands

### Database
```bash
python manage.py makemigrations          # Create migrations
python manage.py migrate                 # Apply migrations
python manage.py migrate --fake-initial  # Skip initial
python manage.py sqlmigrate              # Show SQL
```

### Server
```bash
python manage.py runserver               # Start dev server
python manage.py runserver 0.0.0.0:8000  # Public access
python manage.py runserver 8080          # Different port
```

### Management
```bash
python manage.py shell                   # Interactive shell
python manage.py shell < script.py       # Run script
python manage.py createsuperuser         # Create admin
python manage.py changepassword username # Change password
```

### Testing
```bash
python manage.py test_features           # Run all tests
python manage.py test                    # Run pytest
```

### Utilities
```bash
python manage.py collectstatic           # Collect static files
python manage.py dumpdata > backup.json  # Backup DB
python manage.py loaddata backup.json    # Restore DB
```

### IoT & AI
```bash
python scripts/start_iot_simulator.py                # IoT simulator
python scripts/start_iot_simulator.py --demo        # Demo mode
python manage.py shell < scripts/seed_database.py   # Seed DB
```

---

## 📚 Project Statistics

| Metric | Count |
|--------|-------|
| Django Apps | 13 |
| Database Models | 30+ |
| API Endpoints | 50+ |
| Verified Features | 24 |
| Database Tables | 22+ |
| Test Pass Rate | 100% ✅ |
| Lines of Code | 5000+ |

---

## 🌐 Environment Variables

Create `.env` file:

```bash
# Django
DEBUG=True
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=localhost,127.0.0.1

# Database
DB_ENGINE=django.db.backends.sqlite3
DB_NAME=db.sqlite3

# Blockchain
WEB3_PROVIDER=http://localhost:8545
CONTRACT_ADDRESS=0x...

# Email
EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend

# Celery
CELERY_BROKER_URL=redis://localhost:6379
CELERY_RESULT_BACKEND=redis://localhost:6379
```

---

## ✅ Post-Setup Verification

After complete setup, verify:

- [ ] Virtual environment activated
- [ ] All dependencies installed
- [ ] `python manage.py migrate` - no errors
- [ ] `python manage.py createsuperuser` - admin created
- [ ] `python manage.py runserver` - server starts
- [ ] Admin accessible at `http://localhost:8000/admin/`
- [ ] Sample data seeded (optional)
- [ ] Tests pass: `python manage.py test_features` (24/24 ✅)

---

## 📖 Documentation

- [Django Docs](https://docs.djangoproject.com/)
- [DRF Docs](https://www.django-rest-framework.org/)
- [Web3.py Docs](https://web3py.readthedocs.io/)
- [Celery Docs](https://docs.celeryproject.org/)
- [FEATURES_VERIFIED.md](FEATURES_VERIFIED.md) - All 24 features with models & endpoints

---

## 🤝 Support

For issues:
1. Check troubleshooting section above
2. Review FEATURES_VERIFIED.md
3. Check Django/DRF docs
4. Ensure all dependencies installed

---

## 📄 License

Smart India Hackathon 2026 - Problem Statement 26021

**Status**: Production Ready ✅  
**Version**: 1.0.0  
**Last Updated**: December 2024
