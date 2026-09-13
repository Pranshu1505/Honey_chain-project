/**
 * QR Code Management Service
 * Handles all QR code generation, scanning, and verification
 */

import { apiCall, apiCallWithFile } from './base';

const QrService = {
    // QR Code management
    list: () => apiCall('/qr/'),

    get: (id) => apiCall(`/qr/${id}/`),

    getByBatch: (batchId) => apiCall(`/qr/?batch=${batchId}`),

    // Generation
    generate: (batchId) => apiCall('/qr/', {
        method: 'POST',
        body: JSON.stringify({ batch_id: batchId })
    }),

    generateBulk: (batchIds) => apiCall('/qr/bulk/', {
        method: 'POST',
        body: JSON.stringify({ batch_ids: batchIds })
    }),

    regenerate: (id) => apiCall(`/qr/${id}/regenerate/`, { method: 'POST' }),

    // Scanning & Verification
    scan: (qrCode) => apiCall('/qr/scan/', {
        method: 'POST',
        body: JSON.stringify({ qr_code: qrCode })
    }),

    verify: (qrData) => apiCall('/qr/verify/', {
        method: 'POST',
        body: JSON.stringify({ data: qrData })
    }),

    validateQRCode: (qrCode) => apiCall('/qr/validate/', {
        method: 'POST',
        body: JSON.stringify({ qr_code: qrCode })
    }),

    // Download
    downloadQRImage: (id) => apiCall(`/qr/${id}/download/`),

    downloadBulkQRCodes: (batchIds) => apiCall('/qr/download-bulk/', {
        method: 'POST',
        body: JSON.stringify({ batch_ids: batchIds })
    }),

    // Statistics
    getScanStats: (id) => apiCall(`/qr/${id}/stats/`),

    getTotalScans: (id) => apiCall(`/qr/${id}/total-scans/`),

    getScanHistory: (id, limit = 50) =>
        apiCall(`/qr/${id}/scan-history/?limit=${limit}`),

    // Batch operations
    batchGenerate: (batchIds) => apiCall('/qr/batch-generate/', {
        method: 'POST',
        body: JSON.stringify({ batch_ids: batchIds })
    }),

    batchPrint: (ids, format = 'pdf') => apiCall('/qr/batch-print/', {
        method: 'POST',
        body: JSON.stringify({ qr_ids: ids, format })
    }),

    // Format operations
    getQRAsJSON: (id) => apiCall(`/qr/${id}/json/`),

    getQRAsImage: (id, format = 'png') => apiCall(`/qr/${id}/image/?format=${format}`),

    getQRMetadata: (id) => apiCall(`/qr/${id}/metadata/`),
};

export default QrService;
