/**
 * Honey Batch Management Service
 * Handles all batch-related API calls
 */

import { apiCall } from './base';

const BatchService = {
    list: () => apiCall('/batch/'),

    get: (id) => apiCall(`/batch/${id}/`),

    create: (data) => apiCall('/batch/', {
        method: 'POST',
        body: JSON.stringify(data)
    }),

    update: (id, data) => apiCall(`/batch/${id}/`, {
        method: 'PUT',
        body: JSON.stringify(data)
    }),

    delete: (id) => apiCall(`/batch/${id}/`, { method: 'DELETE' }),

    // Status management
    approve: (id) => apiCall(`/batch/${id}/approve/`, { method: 'POST' }),

    reject: (id, reason) => apiCall(`/batch/${id}/reject/`, {
        method: 'POST',
        body: JSON.stringify({ reason })
    }),

    updateStatus: (id, status) => apiCall(`/batch/${id}/`, {
        method: 'PUT',
        body: JSON.stringify({ status })
    }),

    // Filtering
    getByStatus: (status) => apiCall(`/batch/?status=${status}`),

    getByHoneyType: (honeyType) => apiCall(`/batch/?honey_type=${honeyType}`),

    getPendingApprovals: () => apiCall('/batch/?status=created'),

    getByDate: (startDate, endDate) =>
        apiCall(`/batch/?created_at__gte=${startDate}&created_at__lte=${endDate}`),

    // Quality
    getQualityScore: (id) => apiCall(`/batch/${id}/quality-score/`),

    updateQualityScore: (id, score) => apiCall(`/batch/${id}/`, {
        method: 'PUT',
        body: JSON.stringify({ quality_score: score })
    }),

    // Blockchain
    getBlockchainHash: (id) => apiCall(`/batch/${id}/blockchain-hash/`),

    // Related data
    getHarvests: (batchId) => apiCall(`/batch/${batchId}/harvests/`),

    getProcessing: (batchId) => apiCall(`/batch/${batchId}/processing/`),
};

export default BatchService;
