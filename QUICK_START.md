# 🍯 Honey Chain Django Project - Quick Start Guide

## ✅ Project Status: READY TO RUN

Congratulations! Your Django-based Honey Chain blockchain project has been successfully created and is now running!

## 🚀 Server is LIVE!

**Django Development Server:**
- **URL:** http://localhost:8000
- **Admin Panel:** http://localhost:8000/admin
- **Username:** admin
- **Password:** admin123

## 📁 Project Location

`C:\Users\rohit.b.kumar\Downloads\HoneyProject\honey_chain\`

## 🏗️ Project Architecture

### Backend Apps Created:
1. **beekeeper** - Beekeeper profiles, apiaries, and bee farm management
2. **hive** - Individual hive tracking with health metrics
3. **harvest** - Honey harvest records from hives
4. **batch** - Honey batch grouping for processing
5. **processing** - Quality testing and processing workflow
6. **blockchain** - Blockchain transactions and immutable records ⛓️
7. **qr** - QR code generation for product verification
8. **sensor** - IoT sensor data collection (temperature, humidity, weight)
9. **admin_portal** - Admin dashboard, reporting, and audit logging

## 🔑 Key Features Implemented

✅ **Multi-Role User System** - Admin, Beekeeper, Processor, Distributor, Retailer, Consumer
✅ **Blockchain Integration** - Web3-ready for transaction recording
✅ **IoT Sensor Management** - Real-time hive monitoring
✅ **QR Code Generation** - Consumer verification & supply chain tracking
✅ **Honey Batch Lifecycle** - Complete workflow from harvest to delivery
✅ **Admin Dashboard** - Statistics, reporting, and audit logs
✅ **RESTful API** - Full REST API with Django REST Framework
✅ **Role-Based Permissions** - Token-based authentication

## 📡 API Endpoints

### Admin Dashboard
- `GET /api/admin/dashboard/stats/` - Dashboard statistics
- `POST /api/admin/dashboard/verify_user/` - Verify user account
- `GET /api/admin/reports/` - View admin reports

### Beekeeper Management
- `GET/POST /api/beekeeper/apiaries/` - Manage apiaries
- `GET/PUT /api/beekeeper/profile/me/` - Beekeeper profile

### Hive Management
- `GET/POST /api/hive/` - Create and manage hives
- `GET/PUT /api/hive/{id}/health/` - Hive health metrics

### Harvest Tracking
- `GET/POST /api/harvest/` - Record honey harvests

### Batch Management
- `GET/POST /api/batch/` - Create and manage batches
- `GET /api/batch/{id}/` - View batch details

### Blockchain (⛓️ Key Feature)
- `GET /api/blockchain/transactions/` - View blockchain transactions
- `GET /api/blockchain/records/` - View blockchain records
- `GET /api/blockchain/records/verify/?batch_id=XXX` - Verify honey batch
- `POST /api/blockchain/records/record_transaction/` - Record new transaction

### QR Code
- `GET/POST /api/qr/` - QR code management
- `POST /api/qr/{id}/generate/` - Generate QR code
- `POST /api/qr/{id}/scan/` - Record QR scan

### Sensor Data (IoT)
- `GET/POST /api/sensor/` - Record sensor data
- `GET /api/sensor/latest/` - Get latest sensor readings

### Processing & Quality
- `GET/POST /api/processing/` - Processing records
- `GET/POST /api/processing/quality-test/` - Quality test results

## 🎯 Next Steps

### 1. Access Admin Panel
Open browser → http://localhost:8000/admin
- Login with: **admin** / **admin123**
- Create users for different roles (Beekeeper, Processor, etc.)

### 2. Create Test Data
```bash
# From the project root, run Django shell:
py manage.py shell
```

Then create sample data:
```python
from django.contrib.auth.models import User
from apps.beekeeper.models import Apiary, BeekeeperProfile
from apps.hive.models import Hive, HiveHealth

# Create a beekeeper user
beekeeper = User.objects.create_user('farmer_ramesh', 'ramesh@example.com', 'pass123')

# Create beekeeper profile
BeekeeperProfile.objects.create(
    user=beekeeper,
    years_of_experience=10,
    total_hives=50,
    avg_honey_yield=15.5
)

# Create an apiary
apiary = Apiary.objects.create(
    beekeeper=beekeeper,
    name='Hill Farm Apiary',
    location='Lucknow, UP',
    total_hives=50,
    latitude=26.8467,
    longitude=80.9462
)

# Create a hive
hive = Hive.objects.create(
    apiary=apiary,
    hive_id='HIVE-001',
    name='Hive 1',
    hive_type='langstroth',
    installation_date='2026-01-15'
)

# Create hive health metrics
HiveHealth.objects.create(
    hive=hive,
    temperature=32.5,
    humidity=65.0,
    weight=15.2,
    bee_activity=85,
    disease_risk='low'
)
```

### 3. Test API Endpoints
Use a tool like Postman or curl to test:

```bash
# List hives
curl -H "Authorization: Token YOUR_TOKEN" \
  http://localhost:8000/api/hive/

# Record sensor data
curl -X POST http://localhost:8000/api/sensor/ \
  -H "Authorization: Token YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"hive": 1, "sensor_type": "temperature", "sensor_id": "TEMP-001", "value": 32.5, "unit": "°C"}'
```

### 4. Blockchain Integration (Future)
The project is ready for Ethereum integration:
1. Update `.env` with blockchain network settings
2. Install `web3.py`: `pip install web3`
3. Configure Ganache or Infura RPC endpoint
4. Deploy smart contract for honey traceability

## 📊 Database

- **Engine:** SQLite (development) - `db.sqlite3`
- **Models Created:** 30+ models across all apps
- **Ready for:** PostgreSQL (production)

## 🔒 Security Notes

⚠️ **Development Setup:**
- `DEBUG = True` (change to `False` in production)
- SQLite database (use PostgreSQL in production)
- Default secret key (create new one)

**For Production:**
1. Update `SECRET_KEY` in `.env`
2. Set `DEBUG = False`
3. Configure PostgreSQL database
4. Set up HTTPS/SSL
5. Update `ALLOWED_HOSTS` and CORS settings
6. Implement rate limiting
7. Use environment variables for secrets

## 📝 Configuration Files

- **Settings:** `config/settings/base.py`, `config/settings/dev.py`
- **URLs:** `config/urls.py`
- **Requirements:** `requirements.txt`
- **Environment:** `.env.example` → copy to `.env`

## 🗂️ Project Structure

```
honey_chain/
├── manage.py
├── requirements.txt
├── .env.example
├── db.sqlite3              # SQLite database
├── config/
│   ├── settings/          # Django settings
│   ├── urls.py            # URL routing
│   └── wsgi.py
├── apps/                  # Django apps
│   ├── beekeeper/
│   ├── hive/
│   ├── harvest/
│   ├── batch/
│   ├── processing/
│   ├── blockchain/
│   ├── qr/
│   ├── sensor/
│   └── admin_portal/
├── static/                # CSS, JS, images
├── media/                 # User uploads
└── templates/            # HTML templates
```

## ⚙️ Common Commands

```bash
# Run development server
py manage.py runserver

# Access Django shell
py manage.py shell

# Create migrations
py manage.py makemigrations

# Apply migrations
py manage.py migrate

# Create superuser
py manage.py createsuperuser

# Run tests
py manage.py test

# Collect static files (production)
py manage.py collectstatic
```

## 🧪 Running Tests

```bash
py manage.py test
```

## 🐛 Troubleshooting

**Port 8000 already in use:**
```bash
py manage.py runserver 8001
```

**Database issues:**
```bash
py manage.py migrate --run-syncdb
```

**Clear cache:**
```bash
py manage.py clear_cache
```

## 📚 API Documentation

More detailed API documentation coming soon. For now:
1. Check `README.md` for detailed API examples
2. Visit http://localhost:8000/admin for data models
3. Use Django shell for complex queries

## 🎯 Hackathon Development Roadmap

Phase 1 ✅ (COMPLETED):
- Project structure and apps
- Database models
- Basic CRUD APIs
- Blockchain integration framework

Phase 2 (TODO):
- Blockchain smart contract deployment
- QR code generation optimization
- Sensor data simulation
- Admin dashboard UI

Phase 3 (TODO):
- Mobile app integration
- IoT hardware integration
- AI-based predictions
- Consumer verification interface

## 🤝 Support

For issues or questions:
1. Check Django documentation: https://docs.djangoproject.com/
2. Check DRF documentation: https://www.django-rest-framework.org/
3. Review model definitions in each app's `models.py`

## 📄 License

Smart India Hackathon 2026 - Problem Statement 26021
"Honey Chain - Blockchain-Based Honey Traceability and Smart Beekeeping Management System"

---

**Happy Hacking! 🍯** 

*From Hive to Home - Transparent, Sustainable Beekeeping Ecosystem*
