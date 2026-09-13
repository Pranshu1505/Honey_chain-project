/**
 * Main API Service Module
 * Re-exports all individual service modules for centralized access
 * 
 * Usage:
 * import { AuthService, HiveService, IotService } from './services/api';
 * 
 * Or import individual services:
 * import AuthService from './services/auth';
 * import HiveService from './services/hive';
 */

// Import all service modules
import AuthService from './auth';
import HiveService from './hive';
import IotService from './iot';
import AiService from './ai';
import HarvestService from './harvest';
import BatchService from './batch';
import BlockchainService from './blockchain';
import ProcessingService from './processing';
import DistributorService from './distributor';
import RetailerService from './retailer';
import QrService from './qr';
import { apiCall, apiCallWithFile, setApiBaseUrl } from './base';

// Export individual services
export {
    AuthService,
    HiveService,
    IotService,
    AiService,
    HarvestService,
    BatchService,
    BlockchainService,
    ProcessingService,
    DistributorService,
    RetailerService,
    QrService,
    apiCall,
    apiCallWithFile,
    setApiBaseUrl,
};

// Default export for convenience
export default {
    AuthService,
    HiveService,
    IotService,
    AiService,
    HarvestService,
    BatchService,
    BlockchainService,
    ProcessingService,
    DistributorService,
    RetailerService,
    QrService,
    apiCall,
    apiCallWithFile,
    setApiBaseUrl,
};
