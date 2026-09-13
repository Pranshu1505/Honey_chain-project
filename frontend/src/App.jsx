import React, { useState } from 'react';
import './App.css';
import Login from './components/Login';
import Dashboard from './components/Dashboard';
import BeekeeperManager from './components/BeekeeperManager';
import HiveMonitor from './components/HiveMonitor';
import BatchTracker from './components/BatchTracker';
import QualityTester from './components/QualityTester';
import BlockchainVerifier from './components/BlockchainVerifier';
import QRCodeScanner from './components/QRCodeScanner';

const NAV_ITEMS = [
    { key: 'dashboard', label: 'Dashboard', roles: ['admin', 'beekeeper', 'processor', 'distributor', 'retailer', 'consumer'] },
    { key: 'beekeepers', label: 'Beekeepers', roles: ['admin', 'beekeeper'] },
    { key: 'hives', label: 'Hives', roles: ['admin', 'beekeeper'] },
    { key: 'batches', label: 'Batches', roles: ['admin', 'beekeeper', 'processor', 'distributor', 'retailer'] },
    { key: 'quality', label: 'Quality', roles: ['admin', 'beekeeper', 'processor'] },
    { key: 'blockchain', label: 'Blockchain', roles: ['admin', 'beekeeper', 'processor', 'distributor', 'retailer', 'consumer'] },
    { key: 'scan', label: 'Scan QR', roles: ['admin', 'beekeeper', 'processor', 'distributor', 'retailer', 'consumer'] },
];

function App() {
    const [token, setToken] = useState(localStorage.getItem('token') || null);
    const [role, setRole] = useState(localStorage.getItem('role') || 'consumer');
    const [currentPage, setCurrentPage] = useState('dashboard');

    const handleLogin = (newToken) => {
        setToken(newToken);
        setRole(localStorage.getItem('role') || 'consumer');
        setCurrentPage('dashboard');
    };

    const handleLogout = () => {
        setToken(null);
        localStorage.removeItem('token');
        localStorage.removeItem('username');
        localStorage.removeItem('role');
        setCurrentPage('dashboard');
    };

    if (!token) {
        return <Login onLoginSuccess={handleLogin} />;
    }

    const visibleNavItems = NAV_ITEMS.filter(item => item.roles.includes(role));

    const renderPage = () => {
        switch (currentPage) {
            case 'dashboard':
                return <Dashboard token={token} />;
            case 'beekeepers':
                return <BeekeeperManager token={token} />;
            case 'hives':
                return <HiveMonitor token={token} />;
            case 'batches':
                return <BatchTracker token={token} />;
            case 'quality':
                return <QualityTester token={token} />;
            case 'blockchain':
                return <BlockchainVerifier token={token} />;
            case 'scan':
                return <QRCodeScanner token={token} />;
            default:
                return <Dashboard token={token} />;
        }
    };

    return (
        <div className="app">
            <nav className="navbar">
                <div className="nav-brand">ðŸ¯ Honey Chain</div>

                <div className="nav-menu">
                    {visibleNavItems.map(item => (
                        <button
                            key={item.key}
                            className={`nav-item ${currentPage === item.key ? 'active' : ''}`}
                            onClick={() => setCurrentPage(item.key)}
                        >
                            {item.label}
                        </button>
                    ))}
                </div>

                <div className="nav-user">
                    <span className="username">{localStorage.getItem('username')} ({role})</span>
                    <button className="btn-logout" onClick={handleLogout}>
                        Logout
                    </button>
                </div>
            </nav>

            <main className="main-content">
                {renderPage()}
            </main>

            <footer className="footer">
                <p>ðŸ¯ Honey Chain - Blockchain-Based Honey Traceability System</p>
                <p>Smart India Hackathon 2026 | Problem Statement 26021</p>
            </footer>
        </div>
    );
}

export default App;
