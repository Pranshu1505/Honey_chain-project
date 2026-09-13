import React, { useEffect, useState } from 'react';
import { AdminService } from '../../services/api';
import './Dashboard.css';

/**
 * Admin Dashboard Page
 * Overview of system metrics and key statistics
 */
const AdminDashboard = () => {
    const [stats, setStats] = useState({});
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        loadStats();
    }, []);

    const loadStats = async () => {
        try {
            // TODO: Fetch admin statistics and metrics
            setLoading(false);
        } catch (error) {
            console.error('Error loading admin stats:', error);
            setLoading(false);
        }
    };

    if (loading) return <div>Loading...</div>;

    return (
        <div className="admin-dashboard">
            <h1>Admin Dashboard</h1>
            <div className="dashboard-grid">
                <div className="stat-card">
                    <h3>Total Users</h3>
                    <p className="stat-value">{stats.totalUsers || 0}</p>
                </div>
                <div className="stat-card">
                    <h3>Active Hives</h3>
                    <p className="stat-value">{stats.activeHives || 0}</p>
                </div>
                <div className="stat-card">
                    <h3>Pending Approvals</h3>
                    <p className="stat-value">{stats.pendingApprovals || 0}</p>
                </div>
                <div className="stat-card">
                    <h3>System Health</h3>
                    <p className="stat-value">{stats.systemHealth || 'Good'}</p>
                </div>
            </div>
            {/* Add more dashboard content */}
        </div>
    );
};

export default AdminDashboard;
