/**
 * TypeScript Type Definitions
 * Centralized interfaces and types for the application
 */

// User Types
export interface User {
    id: string;
    username: string;
    email: string;
    role: UserRole;
    firstName?: string;
    lastName?: string;
    profilePicture?: string;
    isActive: boolean;
    dateJoined: string;
    lastLogin?: string;
    permissions: string[];
}

export type UserRole =
    | 'admin'
    | 'beekeeper'
    | 'hive_manager'
    | 'processor'
    | 'distributor'
    | 'retailer'
    | 'consumer'
    | 'government';

// Hive Types
export interface Hive {
    id: string;
    name: string;
    beekeeper: string;
    apiary: string;
    location: {
        latitude: number;
        longitude: number;
        address: string;
    };
    beeSpecies: string;
    status: 'active' | 'inactive' | 'monitoring' | 'quarantined';
    healthScore: number;
    lastInspection: string;
    createdAt: string;
    updatedAt: string;
}

// Harvest Types
export interface Harvest {
    id: string;
    hive: string;
    harvestDate: string;
    honeyQuantity: number;
    honeyType: string;
    qualityGrade: 'A' | 'B' | 'C';
    notes?: string;
    createdAt: string;
}

// Batch Types
export interface HoneyBatch {
    id: string;
    batchNumber: string;
    harvest: string;
    quantity: number;
    qualityScore: number;
    status: 'pending' | 'approved' | 'rejected' | 'processing';
    blockchainHash?: string;
    createdAt: string;
    updatedAt: string;
}

// Sensor Types
export interface SensorData {
    id: string;
    hive: string;
    temperature: number;
    humidity: number;
    weight: number;
    soundLevel: number;
    timestamp: string;
}

// AI Analysis Types
export interface AiAnalysis {
    id: string;
    hive: string;
    healthScore: number;
    diseaseRisks: DiseaseRisk[];
    recommendations: string[];
    trendAnalysis: string;
    generatedAt: string;
}

export interface DiseaseRisk {
    disease: string;
    riskScore: number;
    symptoms: string[];
    recommendations: string[];
}

// Processing Types
export interface ProcessingRecord {
    id: string;
    batch: string;
    startDate: string;
    endDate?: string;
    processType: string;
    status: 'in_progress' | 'completed' | 'on_hold';
    qualityTests: QualityTest[];
}

export interface QualityTest {
    id: string;
    testType: string;
    result: string;
    passed: boolean;
    testDate: string;
}

// Distributor Types
export interface Shipment {
    id: string;
    batchIds: string[];
    destination: string;
    status: 'pending' | 'shipped' | 'in_transit' | 'delivered';
    trackingNumber: string;
    shippedDate?: string;
    deliveryDate?: string;
}

// Notification Types
export interface Notification {
    id: string;
    userId: string;
    type: 'alert' | 'info' | 'warning' | 'success';
    message: string;
    read: boolean;
    createdAt: string;
}

// API Response Types
export interface ApiResponse<T> {
    success: boolean;
    data?: T;
    error?: string;
    message?: string;
}

export interface PaginatedResponse<T> {
    results: T[];
    count: number;
    next?: string;
    previous?: string;
}
