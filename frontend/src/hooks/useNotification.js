import { useState, useCallback, useContext } from 'react';
import { NotificationContext } from '../context/NotificationContext';

/**
 * useNotification Hook
 * Simplifies notification/toast management
 */
const useNotification = () => {
    const context = useContext(NotificationContext);

    if (!context) {
        throw new Error('useNotification must be used within NotificationProvider');
    }

    const { addNotification } = context;

    const showSuccess = useCallback(
        (message, duration = 3000) => {
            addNotification({
                type: 'success',
                message,
                duration,
            });
        },
        [addNotification]
    );

    const showError = useCallback(
        (message, duration = 5000) => {
            addNotification({
                type: 'error',
                message,
                duration,
            });
        },
        [addNotification]
    );

    const showInfo = useCallback(
        (message, duration = 3000) => {
            addNotification({
                type: 'info',
                message,
                duration,
            });
        },
        [addNotification]
    );

    const showWarning = useCallback(
        (message, duration = 4000) => {
            addNotification({
                type: 'warning',
                message,
                duration,
            });
        },
        [addNotification]
    );

    return { showSuccess, showError, showInfo, showWarning };
};

export default useNotification;
