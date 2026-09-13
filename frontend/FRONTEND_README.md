# Honey Chain Frontend

**React + Vite + Fetch API** - Full-featured honey traceability system UI.

## Quick Start

### 1. Prerequisites
- Node.js 18+ installed
- Django backend running on `http://localhost:8000`

### 2. Setup

```bash
cd frontend
npm install
```

### 3. Environment Setup

Copy `.env.example` to `.env.local` (already configured for local development):

```bash
VITE_API_BASE_URL=http://localhost:8000
```

### 4. Run Development Server

```bash
npm run dev
```

Frontend will open at `http://localhost:3000`

### 5. Default Credentials

**Username:** `admin`  
**Password:** `admin123`

## Available Commands

| Command | Purpose |
|---------|---------|
| `npm run dev` | Start development server with hot reload |
| `npm run build` | Build optimized production bundle |
| `npm run preview` | Preview production build locally |
| `npm test` | Run all tests (Jest + React Testing Library) |
| `npm run test:watch` | Run tests in watch mode |
| `npm run test:coverage` | Generate test coverage report |
| `npm run lint` | Check code style with ESLint |
| `npm run lint:fix` | Auto-fix linting issues |

## Project Structure

```
frontend/
├── src/
│   ├── components/
│   │   ├── Login.jsx              # Authentication component
│   │   ├── Login.test.jsx         # Login tests
│   │   ├── Dashboard.jsx          # Statistics & overview
│   │   ├── Dashboard.test.jsx     # Dashboard tests
│   │   ├── BeekeeperManager.jsx   # Beekeeper CRUD
│   │   ├── BeekeeperManager.test.jsx
│   │   ├── HiveMonitor.jsx        # Hive & sensor monitoring
│   │   ├── HiveMonitor.test.jsx
│   │   ├── BatchTracker.jsx       # Batch supply chain tracking
│   │   ├── BatchTracker.test.jsx
│   │   ├── QualityTester.jsx      # Quality testing interface
│   │   ├── QualityTester.test.jsx
│   │   ├── BlockchainVerifier.jsx # Blockchain verification
│   │   ├── BlockchainVerifier.test.jsx
│   │   ├── *.css                  # Component-specific styles
│   ├── App.jsx                    # Main app with routing
│   ├── App.css                    # App-wide styles
│   ├── index.jsx                  # React entry point
│   └── index.css                  # Global styles
├── index.html                     # HTML entry point
├── package.json                   # Dependencies & scripts
├── vite.config.js                 # Vite configuration
├── jest.config.js                 # Jest test configuration
├── .babelrc                       # Babel transpilation
├── jest.setup.js                  # Jest setup file
├── .env.example                   # Environment variables template
└── .env.local                     # Local environment variables (add to .gitignore)
```

## Component Overview

### 1. **Login.jsx**
- User authentication with Django backend
- Token storage in localStorage
- Default admin credentials: `admin` / `admin123`
- Error handling and loading states

### 2. **Dashboard.jsx**
- Statistics overview (Beekeepers, Hives, Sensors, Batches)
- Real-time data from 4 API endpoints
- Responsive grid layout

### 3. **BeekeeperManager.jsx**
- List all beekeeper profiles
- Create new beekeeper records
- Display experience, hives, yield, certification

### 4. **HiveMonitor.jsx**
- View all hives with health status
- Click hive to view real-time sensor data
- Temperature, humidity, weight, sound sensors
- Color-coded health indicators

### 5. **BatchTracker.jsx**
- Track honey batches through supply chain
- Status indicators: created, processing, completed, shipped
- Expandable details for each batch

### 6. **QualityTester.jsx**
- Record quality test results
- Test fields: acidity, moisture, color, aroma
- Approval workflow

### 7. **BlockchainVerifier.jsx**
- Search and verify batches on blockchain
- View blockchain records with transaction hashes
- Quality scores and transaction details

### 8. **App.jsx**
- Main app component with navigation
- Token-based authentication
- Route between all features
- Logout functionality

## Testing

### Run All Tests
```bash
npm test
```

### Run Tests in Watch Mode
```bash
npm run test:watch
```

### Generate Coverage Report
```bash
npm run test:coverage
```

### Test Files Created

- `Login.test.jsx` - Authentication, form handling, token storage
- `Dashboard.test.jsx` - API calls, stat display
- `BeekeeperManager.test.jsx` - CRUD operations, form validation
- `HiveMonitor.test.jsx` - Hive selection, sensor data filtering
- `BatchTracker.test.jsx` - Batch listing, status display
- `QualityTester.test.jsx` - Form submission, data validation
- `BlockchainVerifier.test.jsx` - Verification search, blockchain records

## Authentication Flow

1. User enters username/password on Login page
2. Frontend sends POST to `/api-token-auth/`
3. Backend returns auth token
4. Token stored in `localStorage` as `authToken`
5. All subsequent API requests include `Authorization: Token {token}` header
6. Logout clears token from localStorage

## API Integration

All components communicate with Django REST Framework endpoints:

### Authentication
- `POST /api-token-auth/` - Login and get token

### Beekeepers
- `GET /api/beekeeper/profiles/` - List beekeepers
- `POST /api/beekeeper/profiles/` - Create beekeeper

### Hives
- `GET /api/hive/hives/` - List all hives
- `GET /api/sensor/data/?hive={id}` - Get sensor readings

### Batches
- `GET /api/batch/batches/` - List batches

### Quality Testing
- `GET /api/processing/quality/` - List quality tests
- `POST /api/processing/quality/` - Record new test

### Blockchain
- `GET /api/blockchain/records/` - List records
- `GET /api/blockchain/records/verify/?batch_id={id}` - Verify batch
- `POST /api/blockchain/record_transaction/` - Create transaction

## Building for Production

```bash
npm run build
```

Output will be in `dist/` directory.

To preview production build locally:

```bash
npm run preview
```

## Troubleshooting

### Port 3000 already in use
```bash
# Change port in vite.config.js
# Or kill process on port 3000
```

### API requests failing with CORS errors
- Ensure Django backend has CORS enabled
- Check `CORS_ALLOWED_ORIGINS` in Django settings

### Authentication not working
- Verify Django `rest_framework.authtoken` is installed
- Check token endpoint is at `/api-token-auth/`
- Ensure token is in `Authorization: Token` format

### Tests failing
```bash
npm run test -- --verbose
```

## Code Style

Check and fix code style:
```bash
npm run lint
npm run lint:fix
```

## Performance Tips

- Lazy load components with React.lazy() as app grows
- Implement pagination for large lists
- Add React.memo() to prevent unnecessary re-renders
- Use useCallback() for event handlers

## Browser Support

- Chrome/Edge: Latest 2 versions
- Firefox: Latest 2 versions
- Safari: Latest 2 versions
- IE: Not supported

## Contributing

1. Create a feature branch
2. Make changes in components
3. Add tests for new features
4. Run `npm test` and `npm run lint`
5. Submit pull request

## License

MIT

## Support

For issues and questions:
1. Check Django backend is running
2. Review browser console for errors
3. Check API endpoint responses in Network tab
4. Verify authentication token is valid
