/**
 * IoT & Sensor Management Service
 * Handles all sensor data and IoT-related API calls
 */

import { apiCall } from './base';

const IotService = {
    // Sensor Data
    listSensorData: () => apiCall('/sensor/'),

    getSensorReading: (id) => apiCall(`/sensor/${id}/`),

    createSensorReading: (data) => apiCall('/sensor/', {
        method: 'POST',
        body: JSON.stringify(data)
    }),

    getHiveSensorData: (hiveId) => apiCall(`/iot/sensors/hive/${hiveId}/`),

    getSensorDataByType: (hiveId, sensorType) =>
        apiCall(`/iot/sensors/hive/${hiveId}/?sensor_type=${sensorType}`),

    getRecentSensorData: (hiveId, limit = 50) =>
        apiCall(`/iot/sensors/hive/${hiveId}/?limit=${limit}`),

    // Simulator
    startSimulator: () => apiCall('/iot/simulator/start/', { method: 'POST' }),

    stopSimulator: () => apiCall('/iot/simulator/stop/', { method: 'POST' }),

    getSimulatorStatus: () => apiCall('/iot/simulator/status/'),

    generateSensorData: (hiveId, sensorType = null) => apiCall('/iot/simulator/generate/', {
        method: 'POST',
        body: JSON.stringify({
            hive_id: hiveId,
            ...(sensorType && { sensor_type: sensorType })
        })
    }),

    // Health & Alerts
    getHiveHealth: (hiveId) => apiCall(`/iot/health/${hiveId}/`),

    getHiveAlerts: (hiveId) => apiCall(`/iot/alerts/?hive_id=${hiveId}`),

    getAlertsByType: (hiveId, alertType) =>
        apiCall(`/iot/alerts/?hive_id=${hiveId}&type=${alertType}`),

    // Streaming (WebSocket support can be added here)
    subscribeToSensorData: (hiveId) => {
        // TODO: Implement WebSocket subscription
        return `wss://localhost:8000/ws/sensors/${hiveId}/`;
    },

    subscribeTohiveHealth: (hiveId) => {
        // TODO: Implement WebSocket subscription
        return `wss://localhost:8000/ws/health/${hiveId}/`;
    },
};

export default IotService;
