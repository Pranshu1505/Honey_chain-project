/**
 * StatusBadge Component
 * Displays status indicators with appropriate styling
 */

import React from 'react';
import './StatusBadge.css';

const StatusBadge = ({ status, label }) => {
    const getStatusClass = (status) => {
        switch (status?.toLowerCase()) {
            case 'active':
            case 'healthy':
            case 'success':
                return 'status-success';
            case 'pending':
            case 'warning':
                return 'status-warning';
            case 'inactive':
            case 'error':
            case 'failed':
                return 'status-error';
            case 'processing':
                return 'status-processing';
            default:
                return 'status-neutral';
        }
    };

    return (
        <span className={`status-badge ${getStatusClass(status)}`}>
            {label || status}
        </span>
    );
};

export default StatusBadge;
export { StatusBadge };
