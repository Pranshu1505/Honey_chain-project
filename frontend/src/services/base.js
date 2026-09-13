/**
 * API Base Configuration - Core HTTP client
 */

const BASE_URL = process.env.REACT_APP_API_BASE_URL || 'http://localhost:8000/api';

// Helper function for all API calls
export const apiCall = async (endpoint, options = {}) => {
    const token = localStorage.getItem('access_token');
    const headers = {
        'Content-Type': 'application/json',
        ...(token && { 'Authorization': `Bearer ${token}` }),
        ...options.headers,
    };

    const response = await fetch(`${BASE_URL}${endpoint}`, {
        ...options,
        headers,
    });

    if (response.status === 401) {
        localStorage.removeItem('access_token');
        window.location.href = '/login';
    }

    if (!response.ok) {
        const errorData = await response.json().catch(() => ({}));
        throw new Error(errorData.detail || `HTTP Error ${response.status}`);
    }

    return response.json();
};

// Handle file uploads
export const apiCallWithFile = async (endpoint, formData, options = {}) => {
    const token = localStorage.getItem('access_token');
    const headers = {
        ...(token && { 'Authorization': `Bearer ${token}` }),
        ...options.headers,
    };

    const response = await fetch(`${BASE_URL}${endpoint}`, {
        method: 'POST',
        ...options,
        body: formData,
        headers,
    });

    if (response.status === 401) {
        localStorage.removeItem('access_token');
        window.location.href = '/login';
    }

    return response.json();
};

// Set API base URL
export const setApiBaseUrl = (url) => {
    if (url) {
        window.BASE_URL = url;
    }
};

export default {
    apiCall,
    apiCallWithFile,
    setApiBaseUrl,
};
