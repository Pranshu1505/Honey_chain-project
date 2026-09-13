/**
 * Distributor Management Service
 * Handles all distributor-related API calls
 */

import { apiCall } from './base';

const DistributorService = {
    // Distributor management
    list: () => apiCall('/distributor/'),

    get: (id) => apiCall(`/distributor/${id}/`),

    create: (data) => apiCall('/distributor/', {
        method: 'POST',
        body: JSON.stringify(data)
    }),

    update: (id, data) => apiCall(`/distributor/${id}/`, {
        method: 'PUT',
        body: JSON.stringify(data)
    }),

    // Inventory
    getInventory: (distributorId) =>
        apiCall(`/distributor/${distributorId}/inventory/`),

    getInventoryItem: (distributorId, batchId) =>
        apiCall(`/distributor/${distributorId}/inventory/${batchId}/`),

    updateInventory: (distributorId, batchId, quantity) =>
        apiCall(`/distributor/${distributorId}/inventory/${batchId}/`, {
            method: 'PUT',
            body: JSON.stringify({ quantity })
        }),

    getInventoryStatus: (distributorId) =>
        apiCall(`/distributor/${distributorId}/inventory-status/`),

    getLowStockItems: (distributorId) =>
        apiCall(`/distributor/${distributorId}/low-stock/`),

    // Shipments
    listShipments: (distributorId) =>
        apiCall(`/distributor/${distributorId}/shipments/`),

    getShipment: (distributorId, shipmentId) =>
        apiCall(`/distributor/${distributorId}/shipments/${shipmentId}/`),

    createShipment: (distributorId, data) =>
        apiCall(`/distributor/${distributorId}/shipments/`, {
            method: 'POST',
            body: JSON.stringify(data)
        }),

    updateShipment: (distributorId, shipmentId, data) =>
        apiCall(`/distributor/${distributorId}/shipments/${shipmentId}/`, {
            method: 'PUT',
            body: JSON.stringify(data)
        }),

    completeShipment: (distributorId, shipmentId) =>
        apiCall(`/distributor/${distributorId}/shipments/${shipmentId}/complete/`, {
            method: 'POST'
        }),

    cancelShipment: (distributorId, shipmentId, reason) =>
        apiCall(`/distributor/${distributorId}/shipments/${shipmentId}/cancel/`, {
            method: 'POST',
            body: JSON.stringify({ reason })
        }),

    // Tracking
    trackShipment: (shipmentId) =>
        apiCall(`/distributor/shipments/${shipmentId}/track/`),

    getShipmentStatus: (shipmentId) =>
        apiCall(`/distributor/shipments/${shipmentId}/status/`),

    getTrackingHistory: (shipmentId) =>
        apiCall(`/distributor/shipments/${shipmentId}/history/`),

    // Reports
    getShipmentReport: (distributorId, startDate, endDate) =>
        apiCall(`/distributor/${distributorId}/reports/?start=${startDate}&end=${endDate}`),

    getInventoryReport: (distributorId) =>
        apiCall(`/distributor/${distributorId}/inventory-report/`),
};

export default DistributorService;
