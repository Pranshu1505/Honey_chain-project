import React from 'react';
import { Navigate } from 'react-router-dom';
import { useAuth } from '../hooks';

/**
 * PublicRoutes Component
 * Routes accessible without authentication
 * Redirects to dashboard if user is already logged in
 */
const PublicRoutes = ({ children }) => {
    const { user, loading } = useAuth();

    if (loading) {
        return <div>Loading...</div>;
    }

    if (user) {
        return <Navigate to="/dashboard" replace />;
    }

    return children;
};

export default PublicRoutes;
