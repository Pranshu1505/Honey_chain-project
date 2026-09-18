import React, { useState, useEffect } from 'react';
import './Dashboard.css';

const Dashboard = ({ token, onNavigate }) => {
    const [stats, setStats] = useState({
        beekeepers: 0,
        hives: 0,
        sensors: 0,
        batches: 0
    });
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        fetchDashboardStats();
    }, [token]);

    const fetchDashboardStats = async () => {
        try {
            const headers = { 'Authorization': `Token ${token}` };

            const [beekeepersRes, hivesRes, sensorsRes, batchesRes] = await Promise.all([
                fetch('https://honey-chain-project-backend.onrender.com/api/beekeeper/apiaries/', { headers }),
                fetch('https://honey-chain-project-backend.onrender.com/api/hive/', { headers }),
                fetch('https://honey-chain-project-backend.onrender.com/api/sensor/', { headers }),
                fetch('https://honey-chain-project-backend.onrender.com/api/batch/', { headers })
            ]);

            const beekeepersData = await beekeepersRes.json();
            const hivesData = await hivesRes.json();
            const sensorsData = await sensorsRes.json();
            const batchesData = await batchesRes.json();

            setStats({
                beekeepers: beekeepersData.results?.length ?? beekeepersData.length ?? 0,
                hives: hivesData.results?.length ?? hivesData.length ?? 0,
                sensors: sensorsData.results?.length ?? sensorsData.length ?? 0,
                batches: batchesData.results?.length ?? batchesData.length ?? 0
            });
        } catch (error) {
            console.error('Error fetching stats:', error);
        } finally {
            setLoading(false);
        }
    };

    const handleCardClick = (page) => {
        if (onNavigate) {
            onNavigate(page);
        }
    };

    if (loading) {
        return <div className="dashboard-loading">Loading dashboard...</div>;
    }

    return (
        <div className="dashboard">
            <h1>Dashboard</h1>

            <div className="stats-grid">
                <div className="stat-card" onClick={() => handleCardClick('beekeepers')}>
                    <div className="stat-icon">🧑‍🌾</div>
                    <div className="stat-content">
                        <h3>Beekeepers</h3>
                        <p className="stat-number">{stats.beekeepers}</p>
                    </div>
                </div>

                <div className="stat-card" onClick={() => handleCardClick('hives')}>
                    <div className="stat-icon">🐝</div>
                    <div className="stat-content">
                        <h3>Hives</h3>
                        <p className="stat-number">{stats.hives}</p>
                    </div>
                </div>

                <div className="stat-card" onClick={() => handleCardClick('hives')}>
                    <div className="stat-icon">📡</div>
                    <div className="stat-content">
                        <h3>Sensor Readings</h3>
                        <p className="stat-number">{stats.sensors}</p>
                    </div>
                </div>

                <div className="stat-card" onClick={() => handleCardClick('batches')}>
                    <div className="stat-icon">📦</div>
                    <div className="stat-content">
                        <h3>Batches</h3>
                        <p className="stat-number">{stats.batches}</p>
                    </div>
                </div>
            </div>

            <div className="welcome-banner">
                <h2>Welcome to Honey Chain!</h2>
                <p>Monitor your honey production, track batches through the supply chain, and verify quality all in one place.</p>
            </div>
        </div>
    );
};

export default Dashboard;