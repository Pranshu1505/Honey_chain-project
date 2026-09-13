/**
 * Application Constants
 * Centralized constants for the application
 */

// User Roles
export const USER_ROLES = {
    ADMIN: 'admin',
    BEEKEEPER: 'beekeeper',
    HIVE_MANAGER: 'hive_manager',
    PROCESSOR: 'processor',
    DISTRIBUTOR: 'distributor',
    RETAILER: 'retailer',
    CONSUMER: 'consumer',
    GOVERNMENT: 'government',
};

// Hive Status
export const HIVE_STATUS = {
    ACTIVE: 'active',
    INACTIVE: 'inactive',
    MONITORING: 'monitoring',
    QUARANTINED: 'quarantined',
};

// Batch Status
export const BATCH_STATUS = {
    PENDING: 'pending',
    APPROVED: 'approved',
    REJECTED: 'rejected',
    PROCESSING: 'processing',
    COMPLETED: 'completed',
};

// Quality Grades
export const QUALITY_GRADES = {
    A: 'A',
    B: 'B',
    C: 'C',
};

// Alert Types
export const ALERT_TYPES = {
    TEMPERATURE: 'temperature',
    HUMIDITY: 'humidity',
    WEIGHT: 'weight',
    ACTIVITY: 'activity',
    DISEASE: 'disease',
    SYSTEM: 'system',
};

// Notification Types
export const NOTIFICATION_TYPES = {
    ALERT: 'alert',
    INFO: 'info',
    WARNING: 'warning',
    SUCCESS: 'success',
};

// Honey Types
export const HONEY_TYPES = [
    'Acacia',
    'Clover',
    'Wildflower',
    'Manuka',
    'Eucalyptus',
    'Orange Blossom',
];

// Temperature Range for Optimal Hive Health (Celsius)
export const TEMPERATURE_RANGE = {
    MIN: 15,
    MAX: 35,
    OPTIMAL_MIN: 20,
    OPTIMAL_MAX: 30,
};

// Humidity Range for Optimal Hive Health (%)
export const HUMIDITY_RANGE = {
    MIN: 40,
    MAX: 80,
};

// Health Score Ranges
export const HEALTH_SCORE_RANGES = {
    CRITICAL: { min: 0, max: 25, label: 'Critical' },
    POOR: { min: 26, max: 50, label: 'Poor' },
    FAIR: { min: 51, max: 75, label: 'Fair' },
    GOOD: { min: 76, max: 100, label: 'Good' },
};

// Disease Risk Levels
export const DISEASE_RISK_LEVELS = {
    LOW: { min: 0, max: 25, label: 'Low' },
    MODERATE: { min: 26, max: 50, label: 'Moderate' },
    HIGH: { min: 51, max: 75, label: 'High' },
    CRITICAL: { min: 76, max: 100, label: 'Critical' },
};

// API Endpoints
export const API_ENDPOINTS = {
    AUTH: '/auth',
    HIVE: '/hive',
    HARVEST: '/harvest',
    BATCH: '/batch',
    SENSOR: '/sensor',
    AI: '/ai',
    PROCESSING: '/processing',
    DISTRIBUTOR: '/distributor',
    RETAILER: '/retailer',
    CONSUMER: '/consumer',
    QR: '/qr',
    BLOCKCHAIN: '/blockchain',
    ADMIN: '/admin',
};

// Storage Keys
export const STORAGE_KEYS = {
    AUTH_TOKEN: 'authToken',
    USER_DATA: 'userData',
    THEME: 'theme',
    LOCALE: 'locale',
};

// Pagination
export const PAGINATION = {
    DEFAULT_PAGE_SIZE: 20,
    PAGE_SIZE_OPTIONS: [10, 20, 50, 100],
};
