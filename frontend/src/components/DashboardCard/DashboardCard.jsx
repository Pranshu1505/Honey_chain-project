/**
 * DashboardCard Component
 * Reusable card component for dashboard metrics
 */

import React from 'react';
import './DashboardCard.css';

const DashboardCard = ({ title, value, icon, trend, color = 'blue' }) => {
    return (
        <div className={`dashboard-card dashboard-card--${color}`}>
            <div className="card-header">
                <h3>{title}</h3>
                {icon && <span className="card-icon">{icon}</span>}
            </div>
            <div className="card-body">
                <p className="card-value">{value}</p>
                {trend && <p className="card-trend">{trend}</p>}
            </div>
        </div>
    );
};

export default DashboardCard;
export { DashboardCard };
