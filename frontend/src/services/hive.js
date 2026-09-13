/**
 * Hive Management Service
 * Handles all hive-related API calls
 */

import { apiCall } from './base';

const HiveService = {
    list: () => apiCall('/hive/'),

    get: (id) => apiCall(`/hive/${id}/`),

    create: (data) => apiCall('/hive/', {
        method: 'POST',
        body: JSON.stringify(data)
    }),

    update: (id, data) => apiCall(`/hive/${id}/`, {
        method: 'PUT',
        body: JSON.stringify(data)
    }),

    delete: (id) => apiCall(`/hive/${id}/`, { method: 'DELETE' }),

    getHealth: (id) => apiCall(`/hive/${id}/health/`),

    getAnalytics: (id) => apiCall(`/hive/${id}/analytics/`),

    getDetails: (id) => apiCall(`/hive/${id}/details/`),

    updateLocation: (id, location) => apiCall(`/hive/${id}/location/`, {
        method: 'PUT',
        body: JSON.stringify(location)
    }),

    getHivesByApiary: (apiaryId) => apiCall(`/hive/?apiary=${apiaryId}`),

    getHivesByBeekeeper: (beekeeperId) => apiCall(`/hive/?beekeeper=${beekeeperId}`),

    getRecentHives: (limit = 10) => apiCall(`/hive/?limit=${limit}&ordering=-updated_at`),
};

export default HiveService;
