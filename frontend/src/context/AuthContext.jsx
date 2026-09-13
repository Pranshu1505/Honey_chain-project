import React, { createContext, useState, useCallback, useEffect } from 'react';
import { AuthService } from '../services/api';

export const AuthContext = createContext();

/**
 * AuthProvider Component
 * Manages global authentication state
 */
export const AuthProvider = ({ children }) => {
    const [user, setUser] = useState(null);
    const [loading, setLoading] = useState(true);
    const [token, setToken] = useState(localStorage.getItem('authToken'));

    useEffect(() => {
        if (token) {
            checkAuthStatus();
        } else {
            setLoading(false);
        }
    }, []);

    const checkAuthStatus = useCallback(async () => {
        try {
            const currentUser = await AuthService.getCurrentUser();
            setUser(currentUser);
        } catch (error) {
            setToken(null);
            localStorage.removeItem('authToken');
            setUser(null);
        } finally {
            setLoading(false);
        }
    }, []);

    const login = useCallback(async (username, password) => {
        try {
            const response = await AuthService.login({ username, password });
            localStorage.setItem('authToken', response.token);
            setToken(response.token);
            setUser(response.user);
            return response;
        } catch (error) {
            throw error;
        }
    }, []);

    const logout = useCallback(async () => {
        try {
            await AuthService.logout();
        } catch (error) {
            console.error('Logout error:', error);
        } finally {
            setUser(null);
            setToken(null);
            localStorage.removeItem('authToken');
        }
    }, []);

    const value = {
        user,
        token,
        loading,
        isAuthenticated: !!user,
        login,
        logout,
    };

    return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
};
