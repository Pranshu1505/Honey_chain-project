# 🍯 Honey Chain - Quick API Reference

## 🚀 Getting Started

### Start Development Server
```bash
cd c:\Users\rohit.b.kumar\Downloads\HoneyProject\honey_chain
python manage.py runserver
```

### Access Points
- **Admin Panel:** http://localhost:8000/admin
- **API Base:** http://localhost:8000/api/

### Credentials
- **Username:** admin
- **Password:** admin123

---

## 📡 API Endpoints Reference

### 1️⃣ **Beekeeper Management**
```
GET/POST   /api/beekeeper/profiles/
GET/POST   /api/beekeeper/apiaries/
```

**Example Request (Create Profile):**
```bash
curl -X POST http://localhost:8000/api/beekeeper/profiles/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Token YOUR_TOKEN" \
  -d '{
    "user": 1,
    "years_of_experience": 10,
    "total_hives": 50,
    "avg_honey_yield": 15.5,
    "certification": "ISO 9001"
  }'
```

---

### 2️⃣ **Hive Management**
```
GET/POST   /api/hive/hives/
GET/POST   /api/hive/health/
```

**Example Request (Create Hive):**
```bash
curl -X POST http://localhost:8000/api/hive/hives/ \
  -H "Content-Type: application/json" \
  -d '{
    "apiary": 1,
    "hive_id": "HIVE-001",
    "name": "Premium Hive #1",
    "hive_type": "langstroth",
    "installation_date": "2026-01-15",
    "health_status": "healthy",
    "population": 40000,
    "honey_frames": 8
  }'
```

---

### 3️⃣ **IoT Sensor Data**
```
GET/POST   /api/sensor/data/
```

**Sensor Types:**
- `temperature` (°C)
- `humidity` (%)
- `weight` (kg)
- `sound` (dB)

**Example Request:**
```bash
curl -X POST http://localhost:8000/api/sensor/data/ \
  -H "Content-Type: application/json" \
  -d '{
    "hive": 1,
    "sensor_type": "temperature",
    "sensor_id": "SENSOR-TEMP-001",
    "value": 32.5,
    "unit": "°C"
  }'
```

---

### 4️⃣ **Honey Production**
```
GET/POST   /api/harvest/harvests/
GET/POST   /api/batch/batches/
GET/POST   /api/processing/quality/
GET/POST   /api/processing/processing/
```

---

### 5️⃣ **Blockchain Integration**
```
GET/POST   /api/blockchain/transactions/
GET/POST   /api/blockchain/records/
GET/POST   /api/qr/codes/
```

---

### 6️⃣ **Distribution Network**
```
GET/POST   /api/distributor/distributors/
GET/POST   /api/distributor/shipments/
PATCH      /api/distributor/shipments/{id}/mark_delivered/
GET/POST   /api/distributor/inventory/
```

**Mark Shipment as Delivered:**
```bash
curl -X PATCH http://localhost:8000/api/distributor/shipments/1/mark_delivered/ \
  -H "Authorization: Token YOUR_TOKEN"
```

---

### 7️⃣ **Retail Management**
```
GET/POST   /api/retailer/retailers/
GET/POST   /api/retailer/products/
GET/POST   /api/retailer/sales/
```

---

### 8️⃣ **Consumer Platform**
```
GET/POST   /api/consumer/consumers/
GET        /api/consumer/consumers/{id}/purchase_history/
GET/POST   /api/consumer/purchases/
POST       /api/consumer/purchases/{id}/add_review/
GET/POST   /api/consumer/reviews/
```

**Get Purchase History:**
```bash
curl -X GET http://localhost:8000/api/consumer/consumers/1/purchase_history/ \
  -H "Authorization: Token YOUR_TOKEN"
```

---

### 9️⃣ **Notifications**
```
GET/POST   /api/notifications/notifications/
PATCH      /api/notifications/notifications/{id}/mark_as_read/
GET        /api/notifications/notifications/unread_count/
GET/POST   /api/notifications/alerts/
GET        /api/notifications/alerts/active_alerts/
GET/POST   /api/notifications/preferences/my_preferences/
```

**Get Unread Count:**
```bash
curl -X GET http://localhost:8000/api/notifications/notifications/unread_count/ \
  -H "Authorization: Token YOUR_TOKEN"
```

---

## 🧪 Testing

### Run Feature Tests
```bash
python manage.py test_features
```

### Expected Output
```
✓ TEST 1: User Creation & Authentication ✅
✓ TEST 2: Beekeeper Profile Management ✅
... (24 tests total)
✅ ALL 24 FEATURES TESTED SUCCESSFULLY! ✅
```

---

## 🗄️ Database Models

### Beekeeper App
- `User` - Django built-in user model
- `BeekeeperProfile` - Beekeeper profile data
- `Apiary` - Apiary/Beehive collection

### Hive App
- `Hive` - Individual hive records
- `HiveHealth` - Real-time health metrics

### Sensor App
- `SensorData` - IoT sensor readings

### Harvest & Batch
- `Harvest` - Individual harvest records
- `HoneyBatch` - Aggregated batch of honey

### Processing
- `QualityTest` - Quality testing results
- `Processing` - Processing workflow records

### Blockchain
- `BlockchainTransaction` - Blockchain transaction records
- `BlockchainRecord` - Immutable honey records
- `QRCode` - QR code data for batches

### Distribution
- `Distributor` - Distributor company info
- `Shipment` - Shipment tracking
- `Inventory` - Distributor inventory

### Retail
- `Retailer` - Retail store info
- `Product` - Product catalog
- `Sale` - Sales transactions

### Consumer
- `Consumer` - Consumer profiles
- `Purchase` - Purchase records
- `Review` - Product reviews

### Notifications
- `Notification` - User notifications
- `Alert` - System alerts
- `NotificationPreference` - User notification settings

---

## 📊 Common Query Examples

### Get Beekeeper Profile
```bash
curl -X GET http://localhost:8000/api/beekeeper/profiles/1/
```

### Get Hive Health
```bash
curl -X GET http://localhost:8000/api/hive/health/?hive=1
```

### Get Batch Blockchain Record
```bash
curl -X GET http://localhost:8000/api/blockchain/records/?batch_id=BATCH-001
```

### Get Distributor Inventory
```bash
curl -X GET http://localhost:8000/api/distributor/inventory/?distributor=1
```

### Get Consumer Purchase History
```bash
curl -X GET http://localhost:8000/api/consumer/consumers/1/purchase_history/
```

### Get Product Reviews
```bash
curl -X GET http://localhost:8000/api/consumer/reviews/?purchase__consumer=1
```

---

## 🔐 Authentication

### Get Token
```bash
curl -X POST http://localhost:8000/api/auth/token/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "your_username",
    "password": "your_password"
  }'
```

### Use Token
```bash
curl -X GET http://localhost:8000/api/beekeeper/profiles/ \
  -H "Authorization: Token YOUR_TOKEN_HERE"
```

---

## 🛠️ Management Commands

### Create Migrations
```bash
python manage.py makemigrations
```

### Apply Migrations
```bash
python manage.py migrate
```

### Create Superuser
```bash
python manage.py createsuperuser
```

### Collect Static Files
```bash
python manage.py collectstatic
```

### Flush Database
```bash
python manage.py flush
```

---

## 📂 Project Structure

```
honey_chain/
├── manage.py
├── db.sqlite3
├── requirements.txt
├── config/
│   ├── settings/
│   │   ├── base.py          # Main settings
│   │   ├── dev.py           # Dev settings
│   │   └── prod.py          # Prod settings
│   ├── urls.py              # Main URLs
│   ├── wsgi.py
│   └── asgi.py
└── apps/
    ├── core/                # Core utilities
    ├── beekeeper/           # Beekeeper management
    ├── hive/                # Hive management
    ├── sensor/              # Sensor data
    ├── harvest/             # Harvest records
    ├── batch/               # Batch management
    ├── processing/          # Quality & processing
    ├── blockchain/          # Blockchain integration
    ├── qr/                  # QR codes
    ├── distributor/         # Distribution
    ├── retailer/            # Retail
    ├── consumer/            # Consumer
    ├── notifications/       # Notifications
    └── admin_portal/        # Admin features
```

---

## 🎯 API Status Codes

- `200 OK` - Successful GET/POST
- `201 Created` - Successful POST (creation)
- `204 No Content` - Successful DELETE
- `400 Bad Request` - Invalid data
- `401 Unauthorized` - Missing/invalid token
- `403 Forbidden` - Access denied
- `404 Not Found` - Resource not found
- `500 Server Error` - Server error

---

## 🔄 Common Workflows

### Complete Honey Production Workflow

1. **Create Hive**
   ```bash
   POST /api/hive/hives/
   ```

2. **Collect Sensor Data**
   ```bash
   POST /api/sensor/data/ (repeatedly)
   ```

3. **Update Hive Health**
   ```bash
   POST /api/hive/health/
   ```

4. **Record Harvest**
   ```bash
   POST /api/harvest/harvests/
   ```

5. **Create Batch**
   ```bash
   POST /api/batch/batches/
   ```

6. **Test Quality**
   ```bash
   POST /api/processing/quality/
   ```

7. **Process Honey**
   ```bash
   POST /api/processing/processing/
   ```

8. **Record Blockchain**
   ```bash
   POST /api/blockchain/transactions/
   POST /api/blockchain/records/
   ```

9. **Generate QR Code**
   ```bash
   POST /api/qr/codes/
   ```

10. **Create Shipment**
    ```bash
    POST /api/distributor/shipments/
    ```

11. **Add to Inventory**
    ```bash
    POST /api/distributor/inventory/
    ```

12. **Create Product**
    ```bash
    POST /api/retailer/products/
    ```

13. **Record Sale**
    ```bash
    POST /api/retailer/sales/
    ```

14. **Record Consumer Purchase**
    ```bash
    POST /api/consumer/purchases/
    ```

15. **Add Review**
    ```bash
    POST /api/consumer/reviews/
    ```

---

## 💡 Tips

- All endpoints support filtering via query parameters
- Use `?page=1&page_size=20` for pagination
- Use `?ordering=-created_at` for sorting
- Admin panel is at `/admin/` for visual database management
- Check `FEATURES_VERIFIED.md` for detailed feature documentation
- Check `COMPLETION_REPORT.md` for system status

---

## 📞 Quick Troubleshooting

**Q: Command not found - python**
A: Use `py` instead of `python` on Windows
```bash
py manage.py runserver
```

**Q: Port 8000 already in use**
A: Use a different port
```bash
py manage.py runserver 8001
```

**Q: Database locked error**
A: Close any other connections to database and retry

**Q: Import errors**
A: Reinstall requirements
```bash
pip install -r requirements.txt
```

---

## 📚 Documentation Files

- `README.md` - Project overview
- `QUICK_START.md` - Quick setup guide
- `FEATURES_VERIFIED.md` - Complete feature documentation
- `COMPLETION_REPORT.md` - System status report
- `API_REFERENCE.md` - This file

---

**Last Updated:** January 12, 2026
**Version:** 1.0.0
