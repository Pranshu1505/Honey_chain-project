/**
 * Blockchain Service
 * Handles all blockchain-related API calls
 */

import { apiCall } from './base';

const BlockchainService = {
    list: () => apiCall('/blockchain/'),

    get: (id) => apiCall(`/blockchain/${id}/`),

    create: (data) => apiCall('/blockchain/', {
        method: 'POST',
        body: JSON.stringify(data)
    }),

    // Verification
    verify: (hash) => apiCall(`/blockchain/verify/${hash}/`),

    verifyBatch: (batchId) => apiCall(`/blockchain/verify-batch/${batchId}/`),

    verifyTransaction: (transactionHash) =>
        apiCall(`/blockchain/verify-transaction/${transactionHash}/`),

    // Batch transactions
    getTransactionHistory: (batchId) =>
        apiCall(`/blockchain/batch/${batchId}/history/`),

    getBatchTransactions: (batchId) =>
        apiCall(`/blockchain/batch/${batchId}/transactions/`),

    getFullBatchTraceability: (batchId) =>
        apiCall(`/blockchain/batch/${batchId}/traceability/`),

    // Records
    recordHarvest: (data) => apiCall('/blockchain/harvest/', {
        method: 'POST',
        body: JSON.stringify(data)
    }),

    recordProcessing: (data) => apiCall('/blockchain/processing/', {
        method: 'POST',
        body: JSON.stringify(data)
    }),

    recordQualityTest: (data) => apiCall('/blockchain/quality/', {
        method: 'POST',
        body: JSON.stringify(data)
    }),

    recordDistribution: (data) => apiCall('/blockchain/distribution/', {
        method: 'POST',
        body: JSON.stringify(data)
    }),

    // Explorer
    getLatestTransactions: (limit = 20) =>
        apiCall(`/blockchain/latest/?limit=${limit}`),

    searchByHash: (hash) => apiCall(`/blockchain/search/?hash=${hash}`),

    searchByBatch: (batchId) => apiCall(`/blockchain/search/?batch=${batchId}`),

    getBlockInfo: (blockNumber) => apiCall(`/blockchain/block/${blockNumber}/`),

    getMiningStatus: () => apiCall('/blockchain/mining-status/'),
};

export default BlockchainService;
