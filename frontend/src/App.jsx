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
    { key: 'dashboard', label: 'Dashboard', icon: '� ', roles: ['admin', 'beekeeper', 'processor', 'distributor', 'retailer', 'consumer'] },
    { key: 'beekeepers', label: 'Beekeepers', icon: '🧑�🌾', roles: ['admin', 'beekeeper'] },
    { key: 'hives', label: 'Hives', icon: '�', roles: ['admin', 'beekeeper'] },
    { key: 'batches', label: 'Batches', icon: '📦', roles: ['admin', 'beekeeper', 'processor'] },
    { key: 'quality', label: 'Quality', icon: '✅', roles: ['admin', 'beekeeper', 'processor'] },
    { key: 'distributorpanel', label: 'Shipments & Inventory', icon: '🚚', roles: ['admin', 'distributor'] },
    { key: 'retailerpanel', label: 'Products & Sales', icon: '🛒', roles: ['admin', 'retailer'] },
    { key: 'blockchain', label: 'Blockchain', icon: '⛓�', roles: ['admin', 'beekeeper', 'processor', 'distributor', 'retailer', 'consumer'] },
    { key: 'scan', label: 'Scan QR', icon: '📷', roles: ['admin', 'beekeeper', 'processor', 'distributor', 'retailer', 'consumer'] },
];

function App() {
    const [token, setToken] = useState(localStorage.getItem('token') || null);
    const [role, setRole] = useState(localStorage.getItem('role') || 'consumer');
    const [currentPage, setCurrentPage] = useState('dashboard');
    const [sidebarOpen, setSidebarOpen] = useState(false);

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
                return <Dashboard token={token} onNavigate={setCurrentPage} />;
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
            {sidebarOpen && <div className="sidebar-overlay" onClick={() => setSidebarOpen(false)}></div>}
            <aside className={`sidebar ${sidebarOpen ? 'open' : ''}`}>
                <div className="sidebar-brand">
                    <span className="brand-icon">�</span>
                    <span className="brand-text">Honey Chain</span>
                </div>
                <nav className="sidebar-menu">
                    {visibleNavItems.map(item => (
                        <button
                            key={item.key}
                            className={`sidebar-item ${currentPage === item.key ? 'active' : ''}`}
                            onClick={() => { setCurrentPage(item.key); setSidebarOpen(false); }}
                        >
                            <span className="sidebar-icon">{item.icon}</span>
                            <span>{item.label}</span>
                        </button>
                    ))}
                </nav>
            </aside>

            <div className="main-wrapper">
                <header className="topbar">
                    <div className="topbar-left">
                        <button className="hamburger-btn" onClick={() => setSidebarOpen(!sidebarOpen)}>☰</button>
                        <h2 className="topbar-title">{currentLabel}</h2>
                    </div>
                    <div className="topbar-user">
                        <span className="username">{localStorage.getItem('username')} <span className="role-badge">{role}</span></span>
                        <button className="btn-logout" onClick={handleLogout}>Logout</button>
                    </div>
                </header>

                <main className="main-content">
                    {renderPage()}
                </main>

                <footer className="footer">
                    <p>� Honey Chain - Blockchain-Based Honey Traceability System</p>
                    <p>Smart India Hackathon 2026 | Problem Statement 26021</p>
                </footer>
            </div>
        </div>
    );
}

export default App;
