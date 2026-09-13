# 🍯 Honey Chain - Blockchain-Based Honey Traceability System

A complete supply chain management system for honey production, processing, and distribution using React frontend and Django REST API backend, with blockchain integration for immutable record-keeping.

## 📋 Project Structure

```
HoneyProject/
├── honey_chain/          # Main application (Frontend + Backend combined)
│   ├── frontend/         # React + Vite application
│   ├── apps/             # Django applications (16 apps)
│   ├── config/           # Django configuration
│   ├── ai/               # AI models and analytics
│   ├── iot/              # IoT sensor management
│   ├── qr_codes/         # QR code storage
│   ├── media/            # User uploaded files
│   ├── static/           # Static files
│   ├── manage.py         # Django CLI
│   ├── requirements.txt   # Python dependencies
│   └── setup.py          # Setup script
├── README.md             # This file
└── requirement.txt       # Root level dependencies (legacy)
```

## 🎯 Key Features

- **🐝 Hive Management** - Track multiple apiaries and hives with real-time sensor data
- **🔬 IoT Integration** - Temperature, humidity, weight, and activity sensors
- **🤖 AI Analytics** - Hive health analysis, disease prediction, yield forecasting
- **⛓️ Blockchain** - Immutable batch traceability and verification
- **📱 Multi-Role System** - 8 user roles with specific dashboards (Admin, Beekeeper, Processor, Distributor, Retailer, Consumer, Government)
- **🔐 JWT Authentication** - Secure token-based authentication
- **📊 Analytics & Reports** - Comprehensive dashboards and reporting

## 🚀 Quick Start (5 minutes)

### Prerequisites

- **Node.js** v16+ (for frontend)
- **Python** 3.9+ (for backend)
- **Git** (for version control)
- **npm** or **yarn** (comes with Node.js)

### Step 1: Install Backend Dependencies

```bash
# Navigate to honey_chain directory
cd honey_chain

# Create Python virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install Python dependencies
pip install -r requirements.txt
```

### Step 2: Setup Backend Database

```bash
# Run migrations
python manage.py migrate

# Create admin/superuser account
python manage.py createsuperuser
# Follow prompts to create admin user (e.g., admin/admin123)
```

### Step 3: Install Frontend Dependencies

```bash
# Navigate to frontend folder
cd frontend

# Install npm packages
npm install
```

### Step 4: Start the Application

**Terminal 1 - Start Backend:**
```bash
# From honey_chain directory (with venv activated)
python manage.py runserver
# Backend runs at http://localhost:8000
```

**Terminal 2 - Start Frontend:**
```bash
# From honey_chain/frontend directory
npm run dev
# Frontend runs at http://localhost:5173
```

### Step 5: Access the Application

- **Frontend:** `http://localhost:5173`
- **Backend API:** `http://localhost:8000/api/`
- **Admin Panel:** `http://localhost:8000/admin/`

**Default Login:**
- Username: `admin`
- Password: (your created password)

## 🧪 Testing the Application

### Backend Testing

```bash
# From honey_chain directory (with venv activated)

# Run all Django tests
python manage.py test

# Run specific app tests
python manage.py test apps.accounts
python manage.py test apps.hive
python manage.py test apps.ai

# Run with verbose output
python manage.py test --verbosity=2

# Run tests with coverage
pip install pytest pytest-cov
pytest --cov=apps
```

### Frontend Testing

```bash
# From honey_chain/frontend directory

# Run all tests
npm test

# Run tests in watch mode
npm run test:watch

# Run tests with coverage
npm run test:coverage
```

### Manual Testing Workflow

1. **Start both servers** (as shown above)
2. **Create test data:**
   - Login with admin credentials
   - Create apiaries and hives
   - Generate sensor data
3. **Test features:**
   - Check hive health dashboard
   - View AI recommendations
   - Scan QR codes
   - Verify blockchain records
4. **Check API directly:**
   - Visit `http://localhost:8000/api/`
   - Browse API endpoints

## 📚 Detailed Installation Guide

### Prerequisites Check

```bash
# Check Python version (should be 3.9+)
python --version

# Check Node.js version (should be 16+)
node --version

# Check npm version (should be 8+)
npm --version
```

### Backend Installation (Django)

#### 1. Virtual Environment Setup

```bash
cd honey_chain

# Create virtual environment
python -m venv venv

# Activate it
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Verify activation (should show (venv) prefix)
python --version
```

#### 2. Install Dependencies

```bash
# Upgrade pip
pip install --upgrade pip

# Install all Python packages
pip install -r requirements.txt

# Verify installation
pip list
```

#### 3. Database Setup

```bash
# Initialize database with migrations
python manage.py migrate

# Create admin user
python manage.py createsuperuser
# Enter: username (e.g., admin)
# Enter: email (e.g., admin@example.com)
# Enter: password (e.g., admin123)

# Load sample data (optional)
python manage.py loaddata initial_data
```

#### 4. Run Backend Server

```bash
# Start development server
python manage.py runserver

# Or run on custom port
python manage.py runserver 8001

# Server output should show:
# Starting development server at http://127.0.0.1:8000/
# Quit the server with CTRL-BREAK.
```

### Frontend Installation (React)

#### 1. Install Dependencies

```bash
# Navigate to frontend
cd honey_chain/frontend

# Install npm packages
npm install

# Verify installation
npm list react react-dom
```

#### 2. Environment Configuration

```bash
# Check if .env.local exists, if not copy from template
copy .env.example .env.local
# (or: cp .env.example .env.local on macOS/Linux)

# File should contain:
# VITE_API_BASE_URL=http://localhost:8000
```

#### 3. Run Frontend Server

```bash
# Start development server with hot reload
npm run dev

# Frontend output should show:
#   ➜  Local:   http://localhost:5173/
#   ➜  Press q to quit
```

## 📖 Full Project Directory Structure

```
honey_chain/
│
├── frontend/                    # React + Vite frontend
│   ├── src/
│   │   ├── services/           # API service layer (11 services)
│   │   │   ├── base.js         # Core HTTP client
│   │   │   ├── auth.js         # Authentication
│   │   │   ├── hive.js         # Hive management
│   │   │   ├── iot.js          # Sensor data
│   │   │   ├── ai.js           # AI analytics
│   │   │   ├── harvest.js      # Harvest tracking
│   │   │   ├── batch.js        # Batch management
│   │   │   ├── blockchain.js   # Blockchain
│   │   │   ├── processing.js   # Quality processing
│   │   │   ├── distributor.js  # Distribution
│   │   │   ├── retailer.js     # Retail
│   │   │   └── qr.js           # QR codes
│   │   │
│   │   ├── pages/              # Page components (35+ pages)
│   │   │   ├── auth/           # Login, Register
│   │   │   ├── admin/          # Admin dashboards
│   │   │   ├── beekeeper/      # Beekeeper pages
│   │   │   ├── hive/           # Hive details
│   │   │   ├── processing/     # Processing
│   │   │   ├── distributor/    # Distribution
│   │   │   ├── retailer/       # Retail
│   │   │   ├── consumer/       # Consumer
│   │   │   └── verification/   # Verification
│   │   │
│   │   ├── components/         # Reusable UI components (9 components)
│   │   │   ├── Navbar/
│   │   │   ├── Sidebar/
│   │   │   ├── DashboardCard/
│   │   │   ├── Charts/
│   │   │   ├── Tables/
│   │   │   ├── Alerts/
│   │   │   ├── StatusBadge/
│   │   │   ├── QRScanner/
│   │   │   └── Loading/
│   │   │
│   │   ├── hooks/              # Custom React hooks (4 hooks)
│   │   │   ├── useAuth.js
│   │   │   ├── useFetch.js
│   │   │   ├── useForm.js
│   │   │   └── useNotification.js
│   │   │
│   │   ├── context/            # Context providers (3 contexts)
│   │   │   ├── AuthContext.jsx
│   │   │   ├── NotificationContext.jsx
│   │   │   └── ThemeContext.jsx
│   │   │
│   │   ├── types/              # TypeScript interfaces
│   │   │   └── index.ts
│   │   │
│   │   ├── utils/              # Utility functions
│   │   │   ├── formatters.js
│   │   │   ├── validators.js
│   │   │   ├── constants.js
│   │   │   └── helpers.js
│   │   │
│   │   ├── routes/             # Route configuration
│   │   │   ├── PrivateRoutes.jsx
│   │   │   ├── PublicRoutes.jsx
│   │   │   ├── RoleBasedRoute.jsx
│   │   │   └── routeConfig.js
│   │   │
│   │   ├── App.jsx
│   │   ├── main.jsx
│   │   └── index.css
│   │
│   ├── .env.example            # Environment template
│   ├── package.json            # npm dependencies
│   ├── vite.config.js          # Vite configuration
│   └── jest.config.js          # Jest testing config
│
├── apps/                       # Django applications (16 apps)
│   ├── accounts/               # User management
│   ├── core/                   # Core utilities
│   ├── courses/                # Course content
│   ├── quizzes/                # Quiz system
│   ├── hive/                   # Hive management
│   ├── harvest/                # Harvest tracking
│   ├── batch/                  # Batch management
│   ├── processing/             # Quality processing
│   ├── blockchain/             # Blockchain integration
│   ├── qr/                     # QR code management
│   ├── distributor/            # Distribution
│   ├── retailer/               # Retail management
│   ├── consumer/               # Consumer features
│   ├── admin_portal/           # Admin functions
│   ├── audit/                  # Audit logging
│   └── notifications/          # Notifications
│
├── config/                     # Django configuration
│   ├── settings/
│   │   ├── base.py            # Common settings
│   │   ├── dev.py             # Development
│   │   └── prod.py            # Production
│   ├── urls.py                # URL routing
│   ├── wsgi.py                # WSGI config
│   ├── asgi.py                # ASGI config
│   └── celery.py              # Celery setup
│
├── ai/                        # AI/ML modules
│   ├── models/                # AI models
│   ├── services/              # Analysis services
│   └── inference.py           # Main AI coordinator
│
├── iot/                       # IoT sensor modules
│   ├── sensor_generator.py    # Test data generator
│   ├── alerts.py              # Alert system
│   └── simulator.py           # IoT simulator
│
├── manage.py                  # Django CLI
├── requirements.txt           # Python dependencies
├── setup.py                   # Setup script
└── .env.example              # Environment template
```

## 🔧 Configuration

### Backend Environment Setup

Edit `honey_chain/.env`:

```env
# Django
DEBUG=True
SECRET_KEY=your-secret-key
ENVIRONMENT=development

# Database (uses SQLite by default for development)
DATABASE_URL=sqlite:///db.sqlite3

# CORS
CORS_ALLOWED_ORIGINS=http://localhost:5173,http://localhost:3000

# JWT
JWT_EXPIRATION_HOURS=24
```

### Frontend Environment Setup

Edit `honey_chain/frontend/.env.local`:

```env
VITE_API_BASE_URL=http://localhost:8000
```

## ⚙️ Running Commands

### Backend Commands

```bash
# From honey_chain directory (with venv activated)

# Run development server
python manage.py runserver

# Create new migration
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Load sample data
python manage.py loaddata initial_data

# Access Django shell
python manage.py shell

# Run tests
python manage.py test

# Generate test coverage
pip install coverage
coverage run --source='.' manage.py test
coverage report

# Collect static files (production)
python manage.py collectstatic --noinput
```

### Frontend Commands

```bash
# From honey_chain/frontend directory

# Run development server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview

# Run tests
npm test

# Run tests in watch mode
npm run test:watch

# Run tests with coverage
npm run test:coverage

# Lint code
npm run lint

# Fix linting issues
npm run lint:fix
```

## 🔐 API Endpoints (Sample)

### Authentication
```
POST   /api/auth/login/
POST   /api/auth/register/
POST   /api/auth/logout/
GET    /api/auth/me/
```

### Hive Management
```
GET    /api/hive/
POST   /api/hive/
GET    /api/hive/{id}/
PUT    /api/hive/{id}/
DELETE /api/hive/{id}/
GET    /api/hive/{id}/health/
```

### IoT & Sensors
```
GET    /api/iot/sensors/
POST   /api/iot/sensors/
GET    /api/iot/health/{hive_id}/
GET    /api/iot/alerts/
```

### AI Analytics
```
GET    /api/ai/health/{hive_id}/
GET    /api/ai/diseases/{hive_id}/
GET    /api/ai/yield/{hive_id}/
GET    /api/ai/recommendations/{hive_id}/
```

See all endpoints at `http://localhost:8000/api/`

## ⚠️ Troubleshooting

### Common Backend Issues

**"ModuleNotFoundError" when running Django:**
```bash
# Solution: Activate virtual environment
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux

# Then reinstall packages
pip install -r requirements.txt
```

**"Port 8000 already in use":**
```bash
# Solution: Use different port
python manage.py runserver 8001

# Or kill process on Windows:
netstat -ano | findstr :8000
taskkill /PID {PID} /F
```

**Database migration errors:**
```bash
# Solution: Fresh migrations
python manage.py makemigrations
python manage.py migrate --run-syncdb
```

### Common Frontend Issues

**"npm ERR! Cannot find module":**
```bash
# Solution: Reinstall packages
rm -rf node_modules package-lock.json
npm install
```

**"Port 5173 already in use":**
```bash
# Vite will auto-use next available port
# Or specify custom port:
npm run dev -- --port 3000
```

**API connection errors:**
```
Check:
1. Backend is running on http://localhost:8000
2. CORS settings are correct
3. API URL in .env.local is correct
4. Both servers have hot reload working
```

## 📊 Development Workflow

### Typical Development Session

```bash
# Terminal 1: Backend
cd honey_chain
source venv/bin/activate  # or venv\Scripts\activate on Windows
python manage.py runserver

# Terminal 2: Frontend
cd honey_chain/frontend
npm run dev

# Terminal 3: Tests (optional)
cd honey_chain
python manage.py test --watch
```

### Adding New Features

1. **Backend:**
   - Create model in relevant app
   - Create serializer for API responses
   - Create views/viewsets for endpoints
   - Add URL routing
   - Write tests

2. **Frontend:**
   - Create service in `src/services/`
   - Create page/component in `src/pages/` or `src/components/`
   - Add route to `src/routes/routeConfig.js`
   - Write tests

### Code Quality

```bash
# Frontend linting
cd honey_chain/frontend
npm run lint
npm run lint:fix

# Backend code style
cd honey_chain
pip install flake8 black
black .
flake8 .
```

## 🚀 Production Build

### Frontend Production Build

```bash
cd honey_chain/frontend

# Build optimized production bundle
npm run build

# Output in dist/ directory
# Ready to deploy to static hosting (AWS S3, Netlify, Vercel, etc.)
```

### Backend Production Deployment

```bash
cd honey_chain

# Set production settings
export DJANGO_SETTINGS_MODULE=config.settings.prod

# Collect static files
python manage.py collectstatic --noinput

# Apply migrations
python manage.py migrate

# Run with production server (Gunicorn)
pip install gunicorn
gunicorn config.wsgi:application --bind 0.0.0.0:8000
```

## 📱 Supported User Roles

1. **Admin** - System administration and approvals
2. **Beekeeper** - Hive management and data entry
3. **Hive Manager** - Hive monitoring and health tracking
4. **Processor** - Quality testing and batch processing
5. **Distributor** - Inventory and shipment management
6. **Retailer** - Product sales and consumer management
7. **Consumer** - Product verification and tracing
8. **Government** - Regulatory oversight

## 📞 Support & Resources

- **Issue Tracker:** Check GitHub Issues
- **API Documentation:** `http://localhost:8000/api/`
- **Admin Panel:** `http://localhost:8000/admin/`
- **Frontend Live:** `http://localhost:5173`

## 🆘 Quick Help

```bash
# Everything not working? Fresh start:

# Backend
cd honey_chain
rm -rf venv db.sqlite3
python -m venv venv
venv\Scripts\activate  # or source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

# Frontend (new terminal)
cd honey_chain/frontend
rm -rf node_modules package-lock.json
npm install
npm run dev
```

---

**Last Updated:** 2026-09-12  
**Status:** Production Ready ✅  
**Support:** For issues, see troubleshooting section or create an issue
