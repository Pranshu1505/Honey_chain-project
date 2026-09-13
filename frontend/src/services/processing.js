/**
 * Honey Processing Management Service
 * Handles all processing and quality testing API calls
 */

import { apiCall } from './base';

const ProcessingService = {
    // Processing records
    list: () => apiCall('/processing/'),

    get: (id) => apiCall(`/processing/${id}/`),

    create: (data) => apiCall('/processing/', {
        method: 'POST',
        body: JSON.stringify(data)
    }),

    update: (id, data) => apiCall(`/processing/${id}/`, {
        method: 'PUT',
        body: JSON.stringify(data)
    }),

    delete: (id) => apiCall(`/processing/${id}/`, { method: 'DELETE' }),

    // Status management
    markComplete: (id) => apiCall(`/processing/${id}/complete/`, { method: 'POST' }),

    updateStatus: (id, status) => apiCall(`/processing/${id}/`, {
        method: 'PUT',
        body: JSON.stringify({ status })
    }),

    // Quality testing
    listQualityTests: () => apiCall('/processing/quality-tests/'),

    getQualityTest: (id) => apiCall(`/processing/quality-tests/${id}/`),

    createQualityTest: (data) => apiCall('/processing/quality-tests/', {
        method: 'POST',
        body: JSON.stringify(data)
    }),

    updateQualityTest: (id, data) => apiCall(`/processing/quality-tests/${id}/`, {
        method: 'PUT',
        body: JSON.stringify(data)
    }),

    approveQuality: (testId) =>
        apiCall(`/processing/quality-tests/${testId}/approve/`, { method: 'POST' }),

    rejectQuality: (testId, reason) =>
        apiCall(`/processing/quality-tests/${testId}/reject/`, {
            method: 'POST',
            body: JSON.stringify({ reason })
        }),

    // Batch processing
    getProcessingByBatch: (batchId) => apiCall(`/processing/?batch=${batchId}`),

    getQualityTestsByBatch: (batchId) =>
        apiCall(`/processing/quality-tests/?batch=${batchId}`),

    // Filters
    getPendingProcessing: () => apiCall('/processing/?status=pending'),

    getPendingQualityTests: () => apiCall('/processing/quality-tests/?is_approved=false'),

    getInProgress: () => apiCall('/processing/?status=in_progress'),

    // Detailed analysis
    getProcessingDetails: (id) => apiCall(`/processing/${id}/details/`),

    getQualityReport: (batchId) => apiCall(`/processing/quality-report/${batchId}/`),

    getProcessingTimeline: (batchId) => apiCall(`/processing/timeline/${batchId}/`),
};

export default ProcessingService;
