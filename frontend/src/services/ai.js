/**
 * AI Analysis & Recommendations Service
 * Handles all AI-powered analysis and recommendation API calls
 */

import { apiCall } from './base';

const AiService = {
    // Health Analysis
    analyzeHiveHealth: (hiveId, hours = 24) =>
        apiCall(`/ai/health/${hiveId}/?hours=${hours}`),

    getHealthTrend: (hiveId, days = 7) =>
        apiCall(`/ai/health/${hiveId}/trend/?days=${days}`),

    getHealthScore: (hiveId) =>
        apiCall(`/ai/health/${hiveId}/score/`),

    // Disease Detection
    detectDiseases: (hiveId, hours = 48) =>
        apiCall(`/ai/disease/${hiveId}/?hours=${hours}`),

    getDiseaseRiskTimeline: (hiveId, days = 7) =>
        apiCall(`/ai/disease/${hiveId}/timeline/?days=${days}`),

    predictDisease: (hiveId, diseaseType) =>
        apiCall(`/ai/disease/${hiveId}/predict/?disease=${diseaseType}`),

    // Yield Prediction
    predictYield: (hiveId) =>
        apiCall(`/ai/yield/${hiveId}/predict/`),

    predictHarvestTime: (hiveId) =>
        apiCall(`/ai/yield/${hiveId}/harvest-time/`),

    predictWeeklyYield: (hiveId) =>
        apiCall(`/ai/yield/${hiveId}/weekly/`),

    getNectarFlowPrediction: (hiveId) =>
        apiCall(`/ai/yield/${hiveId}/nectar-flow/`),

    // Recommendations
    getRecommendations: (hiveId) =>
        apiCall(`/ai/recommendations/${hiveId}/`),

    getQuickRecommendations: (hiveId) =>
        apiCall(`/ai/recommendations/${hiveId}/quick/`),

    getSeasonalRecommendations: (season) =>
        apiCall(`/ai/recommendations/seasonal/${season}/`),

    getHealthRecommendations: (hiveId) =>
        apiCall(`/ai/recommendations/${hiveId}/health/`),

    getDiseaseRecommendations: (hiveId, diseaseType) =>
        apiCall(`/ai/recommendations/${hiveId}/disease/${diseaseType}/`),

    // Comprehensive Analysis
    analyzeHive: (hiveId) =>
        apiCall(`/ai/analyze/${hiveId}/`),

    getComprehensiveReport: (hiveId) =>
        apiCall(`/ai/report/${hiveId}/`),

    // Data Preprocessing
    validateSensorData: (sensorData) =>
        apiCall('/ai/validate/', {
            method: 'POST',
            body: JSON.stringify(sensorData)
        }),

    preprocessData: (sensorData) =>
        apiCall('/ai/preprocess/', {
            method: 'POST',
            body: JSON.stringify(sensorData)
        }),
};

export default AiService;
