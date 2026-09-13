# Honey Chain - Blockchain-Based Honey Traceability System

A comprehensive Django REST Framework-based backend for the Honey Chain platform, combining Blockchain, IoT, and AI to ensure honey authenticity, traceability, and smart beekeeping management.

## Project Features

✅ **Multi-role User Management** - Admin, Beekeeper, Processor, Distributor, Retailer, Consumer
✅ **Blockchain Integration** - Immutable honey batch traceability with Web3
✅ **IoT Sensor Management** - Temperature, humidity, weight, and activity monitoring
✅ **Honey Batch Lifecycle** - Creation → Quality Testing → Processing → Packaging → Shipment
✅ **QR Code Generation** - Consumer verification and supply chain tracking
✅ **Admin Portal** - Dashboard, reporting, and audit logging
✅ **Apiary Management** - Multiple apiaries per beekeeper with hive tracking
✅ **Quality Assurance** - Quality testing and certification workflow

## Tech Stack

- **Backend**: Django 4.2 + Django REST Framework
- **Database**: SQLite (Development) / PostgreSQL (Production)
- **Blockchain**: Web3.py (for Ethereum integration)
- **QR Codes**: qrcode library
- **Authentication**: Token-based authentication
- **Task Queue**: Celery (optional)

## Project Structure

```
honey_chain/
├── manage.py
├── requirements.txt
├── .env.example
├── config/
│   ├── settings/
│   │   ├── base.py          # Base settings
│   │   ├── dev.py           # Development settings
│   │   └── __init__.py
│   ├── urls.py              # Main URL routing
│   ├── wsgi.py
│   └── __init__.py
├── apps/
│   ├── auth/                # User authentication & profiles
│   ├── beekeeper/           # Beekeeper profiles & apiaries
│   ├── hive/                # Hive management & health metrics
│   ├── harvest/             # Harvest records
│   ├── batch/               # Honey batch management
│   ├── processing/          # Processing & quality testing
│   ├── blockchain/          # Blockchain transactions & records
│   ├── qr/                  # QR code generation & verification
│   ├── sensor/              # IoT sensor data
│   └── admin_portal/        # Admin dashboard & audit logs
├── templates/               # HTML templates
├── static/                  # CSS, JS, images
├── media/                   # User uploads (QR codes, etc)
└── db.sqlite3              # Database file
```

## Installation & Setup

### 1. Prerequisites
- Python 3.9+
- pip or poetry
- Virtual environment (optional but recommended)

### 2. Create Virtual Environment
```bash
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Linux/Mac)
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Environment Configuration
```bash
cp .env.example .env
# Edit .env with your settings
```

### 5. Database Migration
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser (Admin)
```bash
python manage.py createsuperuser
# Follow the prompts to create an admin account
```

### 7. Run Development Server
```bash
python manage.py runserver
# Server will run on http://127.0.0.1:8000
```

### 8. Access Admin Panel
Navigate to: `http://127.0.0.1:8000/admin/`
Login with the superuser credentials created above

## API Endpoints

### Authentication
- `POST /api/auth/users/register/` - Register new user
- `POST /api/auth/users/login/` - Login user
- `POST /api/auth/users/logout/` - Logout user
- `GET/PUT /api/auth/users/profile/` - User profile

### Beekeeper
- `GET/POST /api/beekeeper/apiaries/` - Manage apiaries
- `GET/PUT /api/beekeeper/profile/me/` - Beekeeper profile

### Hive
- `GET/POST /api/hive/` - Manage hives
- `GET/PUT /api/hive/{id}/health/` - Hive health metrics

### Harvest
- `GET/POST /api/harvest/` - Record harvests

### Batch
- `GET/POST /api/batch/` - Create & manage batches

### Blockchain
- `GET /api/blockchain/records/` - View blockchain records
- `GET /api/blockchain/records/verify/?batch_id=X` - Verify batch
- `POST /api/blockchain/records/record_transaction/` - Record transaction

### QR Code
- `GET/POST /api/qr/` - QR code management
- `POST /api/qr/{id}/generate/` - Generate QR code
- `POST /api/qr/{id}/scan/` - Record QR scan

### Sensor
- `GET/POST /api/sensor/` - Sensor data
- `GET /api/sensor/latest/` - Latest sensor readings

### Admin
- `GET /api/admin/dashboard/stats/` - Dashboard statistics
- `POST /api/admin/dashboard/verify_user/` - Verify user

## Example API Usage

### 1. Register as Beekeeper
```bash
curl -X POST http://127.0.0.1:8000/api/auth/users/register/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "farmer_john",
    "email": "john@example.com",
    "password": "SecurePass123!",
    "password2": "SecurePass123!",
    "first_name": "John",
    "last_name": "Doe",
    "role": "beekeeper"
  }'
```

### 2. Create Apiary
```bash
curl -X POST http://127.0.0.1:8000/api/beekeeper/apiaries/ \
  -H "Authorization: Token YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Hill Farm Apiary",
    "location": "Lucknow, UP",
    "latitude": 26.8467,
    "longitude": 80.9462,
    "total_hives": 50
  }'
```

### 3. Create Hive
```bash
curl -X POST http://127.0.0.1:8000/api/hive/ \
  -H "Authorization: Token YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "hive_id": "HIVE-001",
    "name": "Hive 1",
    "hive_type": "langstroth",
    "apiary": 1,
    "installation_date": "2026-01-15"
  }'
```

### 4. Record Sensor Data
```bash
curl -X POST http://127.0.0.1:8000/api/sensor/ \
  -H "Authorization: Token YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "hive": 1,
    "sensor_type": "temperature",
    "sensor_id": "TEMP-001",
    "value": 32.5,
    "unit": "°C"
  }'
```

## Database Models

### Core Entities
- **User** - Django's built-in user model
- **UserProfile** - Extended user info with role & wallet
- **Apiary** - Beekeeper's bee farm
- **Hive** - Individual hive in an apiary
- **HiveHealth** - Health metrics for hives
- **Harvest** - Honey harvest records
- **HoneyBatch** - Grouped honey for processing
- **Processing** - Processing details
- **QualityTest** - Quality testing results
- **BlockchainTransaction** - Transaction history
- **BlockchainRecord** - Immutable batch records
- **QRCode** - QR codes for verification
- **SensorData** - IoT sensor readings
- **AdminReport** - Admin-generated reports
- **AuditLog** - System audit trail

## Configuration

### settings/base.py
- Database configuration
- Installed apps
- Middleware
- REST framework settings
- CORS configuration
- Blockchain settings
- Logging configuration

### .env File
Key environment variables:
- `SECRET_KEY` - Django secret key
- `DEBUG` - Debug mode (False in production)
- `BLOCKCHAIN_NETWORK` - Web3 provider URL
- `CORS_ALLOWED_ORIGINS` - CORS allowed origins

## Security Notes

⚠️ **For Production:**
1. Set `DEBUG = False`
2. Use strong `SECRET_KEY`
3. Configure HTTPS/SSL
4. Use PostgreSQL instead of SQLite
5. Set up proper CORS origins
6. Implement rate limiting
7. Use environment variables for sensitive data
8. Regular security audits

## Testing

```bash
python manage.py test
# Run tests for all apps
```

## Deployment

### Using Gunicorn
```bash
gunicorn config.wsgi:application --bind 0.0.0.0:8000
```

### Using Docker (optional)
Create a Dockerfile for containerized deployment.

## Contributing

1. Create a feature branch
2. Make your changes
3. Write tests
4. Submit a pull request

## License

This project is developed for the Smart India Hackathon 2026 (Problem Statement 26021)

## Support

For issues and questions, please contact the development team.

---

**Made with ❤️ for Transparent, Sustainable Beekeeping Ecosystem**
