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
import DistributorPanel from './components/DistributorPanel';
import RetailerPanel from './components/RetailerPanel';

const NAV_ITEMS = [
    { key: 'dashboard', label: 'Dashboard', icon: 'ðŸ ', roles: ['admin', 'beekeeper', 'processor', 'distributor', 'retailer', 'consumer'] },
    { key: 'beekeepers', label: 'Beekeepers', icon: 'ðŸ§‘â€ðŸŒ¾', roles: ['admin', 'beekeeper'] },
    { key: 'hives', label: 'Hives', icon: 'ðŸ', roles: ['admin', 'beekeeper'] },
    { key: 'batches', label: 'Batches', icon: 'ðŸ“¦', roles: ['admin', 'beekeeper', 'processor'] },
    { key: 'quality', label: 'Quality', icon: 'âœ…', roles: ['admin', 'beekeeper', 'processor'] },
    { key: 'distributorpanel', label: 'Shipments & Inventory', icon: 'ðŸšš', roles: ['admin', 'distributor'] },
    { key: 'retailerpanel', label: 'Products & Sales', icon: 'ðŸ›’', roles: ['admin', 'retailer'] },
    { key: 'blockchain', label: 'Blockchain', icon: 'â›“ï¸', roles: ['admin', 'beekeeper', 'processor', 'distributor', 'retailer', 'consumer'] },
    { key: 'scan', label: 'Scan QR', icon: 'ðŸ“·', roles: ['admin', 'beekeeper', 'processor', 'distributor', 'retailer', 'consumer'] },
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
    const currentLabel = NAV_ITEMS.find(item => item.key === currentPage)?.label || 'Dashboard';

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
            case 'distributorpanel':
                return <DistributorPanel token={token} />;
            case 'retailerpanel':
                return <RetailerPanel token={token} />;
            case 'blockchain':
                return <BlockchainVerifier token={token} />;
            case 'scan':
                return <QRCodeScanner token={token} />;
            default:
                return <Dashboard token={token} />;
        }
    };

    return (
        <div className="app-layout">
            <aside className="sidebar">
                <div className="sidebar-brand">
                    <span className="brand-icon">ðŸ¯</span>
                    <span className="brand-text">Honey Chain</span>
                </div>
                <nav className="sidebar-menu">
                    {visibleNavItems.map(item => (
                        <button
                            key={item.key}
                            className={`sidebar-item ${currentPage === item.key ? 'active' : ''}`}
                            onClick={() => setCurrentPage(item.key)}
                        >
                            <span className="sidebar-icon">{item.icon}</span>
                            <span>{item.label}</span>
                        </button>
                    ))}
                </nav>
            </aside>

            <div className="main-wrapper">
                <header className="topbar">
                    <h2 className="topbar-title">{currentLabel}</h2>
                    <div className="topbar-user">
                        <span className="username">{localStorage.getItem('username')} <span className="role-badge">{role}</span></span>
                        <button className="btn-logout" onClick={handleLogout}>Logout</button>
                    </div>
                </header>

                <main className="main-content">
                    {renderPage()}
                </main>

                <footer className="footer">
                    <p>ðŸ¯ Honey Chain - Blockchain-Based Honey Traceability System</p>
                    <p>Smart India Hackathon 2026 | Problem Statement 26021</p>
                </footer>
            </div>
        </div>
    );
}

export default App;
