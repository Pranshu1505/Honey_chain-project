/**
 * Authentication Service
 * Handles all authentication-related API calls
 */

import { apiCall } from './base';

const AuthService = {
    login: (credentials) => apiCall('/auth/users/login/', {
        method: 'POST',
        body: JSON.stringify(credentials)
    }),

    register: (data) => apiCall('/auth/users/register/', {
        method: 'POST',
        body: JSON.stringify(data)
    }),

    logout: () => apiCall('/auth/users/logout/', { method: 'POST' }),

    getProfile: () => apiCall('/auth/users/me/'),

    updateProfile: (data) => apiCall('/auth/users/me/', {
        method: 'PUT',
        body: JSON.stringify(data)
    }),

    changePassword: (data) => apiCall('/auth/users/set_password/', {
        method: 'POST',
        body: JSON.stringify(data)
    }),

    resetPassword: (email) => apiCall('/auth/users/reset_password/', {
        method: 'POST',
        body: JSON.stringify({ email })
    }),

    verifyToken: (token) => apiCall('/auth/users/verify/', {
        method: 'POST',
        body: JSON.stringify({ token })
    }),

    refreshToken: () => apiCall('/auth/users/refresh/', { method: 'POST' }),

    getCurrentUser: () => apiCall('/auth/users/me/'),

    listUsers: () => apiCall('/auth/users/'),

    getUserPermissions: (userId) => apiCall(`/auth/users/${userId}/permissions/`),
};

export default AuthService;
