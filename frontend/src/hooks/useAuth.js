import { useState, useCallback, useEffect } from 'react';
import { AuthService } from '../services/api';

/**
 * useAuth Hook
 * Manages authentication state and operations
 */
const useAuth = () => {
    const [user, setUser] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        // Load user from token on mount
        checkAuth();
    }, []);

    const checkAuth = useCallback(async () => {
        try {
            const currentUser = await AuthService.getCurrentUser();
            setUser(currentUser);
        } catch (err) {
            setUser(null);
        } finally {
            setLoading(false);
        }
    }, []);

    const login = useCallback(async (credentials) => {
        setLoading(true);
        try {
            const response = await AuthService.login(credentials);
            setUser(response.user);
            return response;
        } catch (err) {
            setError(err.message);
            throw err;
        } finally {
            setLoading(false);
        }
    }, []);

    const logout = useCallback(async () => {
        try {
            await AuthService.logout();
            setUser(null);
        } catch (err) {
            setError(err.message);
        }
    }, []);

    return { user, loading, error, login, logout, checkAuth };
};

export default useAuth;
