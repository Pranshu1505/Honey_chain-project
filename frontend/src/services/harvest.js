/**
 * Harvest Management Service
 * Handles all harvest-related API calls
 */

import { apiCall } from './base';

const HarvestService = {
    list: () => apiCall('/harvest/'),

    get: (id) => apiCall(`/harvest/${id}/`),

    create: (data) => apiCall('/harvest/', {
        method: 'POST',
        body: JSON.stringify(data)
    }),

    update: (id, data) => apiCall(`/harvest/${id}/`, {
        method: 'PUT',
        body: JSON.stringify(data)
    }),

    delete: (id) => apiCall(`/harvest/${id}/`, { method: 'DELETE' }),

    getByHive: (hiveId) => apiCall(`/harvest/?hive=${hiveId}`),

    getByBeekeeper: (beekeeperId) => apiCall(`/harvest/?beekeeper=${beekeeperId}`),

    getByDate: (startDate, endDate) =>
        apiCall(`/harvest/?harvest_date__gte=${startDate}&harvest_date__lte=${endDate}`),

    getByHoneyType: (honeyType) => apiCall(`/harvest/?honey_type=${honeyType}`),

    getRecentHarvests: (limit = 10) => apiCall(`/harvest/?limit=${limit}&ordering=-harvest_date`),

    getYearlyTotal: (hiveId, year) =>
        apiCall(`/harvest/yearly-total/?hive=${hiveId}&year=${year}`),

    getSeasonalStats: (hiveId, season) =>
        apiCall(`/harvest/seasonal-stats/?hive=${hiveId}&season=${season}`),
};

export default HarvestService;
