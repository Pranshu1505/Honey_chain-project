/**
 * Route Configuration
 * Defines all application routes and their properties
 */

// Auth Routes
export const authRoutes = [
    { path: '/login', name: 'Login', public: true },
    { path: '/register', name: 'Register', public: true },
    { path: '/forgot-password', name: 'Forgot Password', public: true },
];

// Admin Routes
export const adminRoutes = [
    { path: '/admin', name: 'Admin Dashboard', roles: ['admin'] },
    { path: '/admin/users', name: 'User Management', roles: ['admin'] },
    { path: '/admin/beekeeper-approvals', name: 'Beekeeper Approvals', roles: ['admin'] },
    { path: '/admin/hive-approvals', name: 'Hive Approvals', roles: ['admin'] },
    { path: '/admin/batch-approvals', name: 'Batch Approvals', roles: ['admin'] },
    { path: '/admin/processing-approvals', name: 'Processing Approvals', roles: ['admin'] },
    { path: '/admin/blockchain', name: 'Blockchain', roles: ['admin'] },
    { path: '/admin/audit-logs', name: 'Audit Logs', roles: ['admin'] },
    { path: '/admin/reports', name: 'Reports', roles: ['admin'] },
];

// Beekeeper Routes
export const beekeeperRoutes = [
    { path: '/beekeeper', name: 'Beekeeper Dashboard', roles: ['beekeeper'] },
    { path: '/beekeeper/profile', name: 'Profile', roles: ['beekeeper'] },
    { path: '/beekeeper/apiaries', name: 'Apiaries', roles: ['beekeeper'] },
    { path: '/beekeeper/hives', name: 'Hives', roles: ['beekeeper'] },
    { path: '/beekeeper/harvest', name: 'Harvest', roles: ['beekeeper'] },
    { path: '/beekeeper/batches', name: 'Honey Batches', roles: ['beekeeper'] },
    { path: '/beekeeper/alerts', name: 'AI Alerts', roles: ['beekeeper'] },
    { path: '/beekeeper/reports', name: 'Reports', roles: ['beekeeper'] },
];

// Hive Routes
export const hiveRoutes = [
    { path: '/hive/:id', name: 'Hive Details', roles: ['beekeeper', 'hive_manager'] },
    { path: '/hive/:id/health', name: 'Hive Health', roles: ['beekeeper', 'hive_manager'] },
    { path: '/hive/:id/sensors', name: 'Sensor Data', roles: ['beekeeper', 'hive_manager'] },
    { path: '/hive/:id/history', name: 'History', roles: ['beekeeper', 'hive_manager'] },
];

// Processing Routes
export const processingRoutes = [
    { path: '/processing', name: 'Processing Dashboard', roles: ['processor'] },
    { path: '/processing/incoming', name: 'Incoming Batches', roles: ['processor'] },
    { path: '/processing/quality', name: 'Quality Testing', roles: ['processor'] },
    { path: '/processing/process', name: 'Processing', roles: ['processor'] },
    { path: '/processing/packaging', name: 'Packaging', roles: ['processor'] },
];

// Distributor Routes
export const distributorRoutes = [
    { path: '/distributor', name: 'Distributor Dashboard', roles: ['distributor'] },
    { path: '/distributor/inventory', name: 'Inventory', roles: ['distributor'] },
    { path: '/distributor/shipments', name: 'Shipments', roles: ['distributor'] },
    { path: '/distributor/tracking', name: 'Tracking', roles: ['distributor'] },
];

// Retailer Routes
export const retailerRoutes = [
    { path: '/retailer', name: 'Retailer Dashboard', roles: ['retailer'] },
    { path: '/retailer/inventory', name: 'Inventory', roles: ['retailer'] },
    { path: '/retailer/products', name: 'Products', roles: ['retailer'] },
    { path: '/retailer/sales', name: 'Sales', roles: ['retailer'] },
];

// Consumer Routes
export const consumerRoutes = [
    { path: '/consumer', name: 'Home', roles: ['consumer'] },
    { path: '/consumer/scan', name: 'QR Scan', roles: ['consumer'] },
    { path: '/consumer/journey/:batchId', name: 'Product Journey', roles: ['consumer'] },
    { path: '/consumer/verify', name: 'Verification', roles: ['consumer'] },
];

// Verification Routes
export const verificationRoutes = [
    { path: '/verify/:batchId', name: 'Verify Batch', public: true },
    { path: '/verify/:batchId/proof', name: 'Blockchain Proof', public: true },
];

// Combine all routes
const routeConfig = [
    ...authRoutes,
    ...adminRoutes,
    ...beekeeperRoutes,
    ...hiveRoutes,
    ...processingRoutes,
    ...distributorRoutes,
    ...retailerRoutes,
    ...consumerRoutes,
    ...verificationRoutes,
];

export default routeConfig;
