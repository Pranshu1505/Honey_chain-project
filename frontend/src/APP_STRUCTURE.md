"""Frontend Structure - Complete routing and main API service"""

// App.jsx - Main application component
import React, { useState } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import Sidebar from './components/Sidebar';
import { AuthContext } from './context/AuthContext';
import './App.css';

// Auth pages
import Login from './pages/auth/Login';
import Register from './pages/auth/Register';
import ForgotPassword from './pages/auth/ForgotPassword';

// Admin pages
import AdminDashboard from './pages/admin/Dashboard';
import UserManagement from './pages/admin/Users';
import BeekeeperApprovals from './pages/admin/BeekeeperApprovals';
import HiveApprovals from './pages/admin/HiveApprovals';
import BatchApprovals from './pages/admin/BatchApprovals';
import ProcessingApprovals from './pages/admin/ProcessingApprovals';
import BlockchainExplorer from './pages/admin/Blockchain';
import AuditLogs from './pages/admin/AuditLogs';
import AdminReports from './pages/admin/Reports';

// Beekeeper pages
import BeekeeperDashboard from './pages/beekeeper/Dashboard';
import BeekeeperProfile from './pages/beekeeper/Profile';
import ApiariesManagement from './pages/beekeeper/Apiaries';
import HivesManagement from './pages/beekeeper/Hives';
import HarvestManagement from './pages/beekeeper/Harvest';
import HoneyBatchesManagement from './pages/beekeeper/HoneyBatches';
import AIAlerts from './pages/beekeeper/AIAlerts';
import BeekeeperReports from './pages/beekeeper/Reports';

// Hive pages
import HiveDetails from './pages/hive/HiveDetails';
import HiveHealth from './pages/hive/HiveHealth';
import SensorData from './pages/hive/SensorData';
import HiveHistory from './pages/hive/History';

// Processing pages
import ProcessingDashboard from './pages/processing/Dashboard';
import IncomingBatches from './pages/processing/IncomingBatches';
import QualityTesting from './pages/processing/QualityTesting';
import ProcessingSteps from './pages/processing/Processing';
import PackagingManagement from './pages/processing/Packaging';

// Distributor pages
import DistributorDashboard from './pages/distributor/Dashboard';
import InventoryManagement from './pages/distributor/Inventory';
import ShipmentsManagement from './pages/distributor/Shipments';
import TrackingInfo from './pages/distributor/Tracking';

// Retailer pages
import RetailerDashboard from './pages/retailer/Dashboard';
import RetailerInventory from './pages/retailer/Inventory';
import RetailerProducts from './pages/retailer/Products';
import SalesManagement from './pages/retailer/Sales';

// Consumer pages
import ConsumerHome from './pages/consumer/Home';
import QRScanner from './pages/consumer/QRScan';
import ProductJourney from './pages/consumer/ProductJourney';
import VerificationResult from './pages/consumer/Verification';

// Verification pages
import VerifyBatch from './pages/verification/VerifyBatch';
import BlockchainProof from './pages/verification/BlockchainProof';

function App() {
  const [user, setUser] = useState(null);
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  
  return (
    <Router>
      <AuthContext.Provider value={{ user, setUser, isAuthenticated, setIsAuthenticated }}>
        <div className="app">
          {isAuthenticated && <Navbar />}
          <div className="app-container">
            {isAuthenticated && <Sidebar userRole={user?.role} />}
            <Routes>
              {/* Public Routes */}
              <Route path="/login" element={<Login />} />
              <Route path="/register" element={<Register />} />
              <Route path="/forgot-password" element={<ForgotPassword />} />
              
              {/* Admin Routes */}
              <Route path="/admin/dashboard" element={<AdminDashboard />} />
              <Route path="/admin/users" element={<UserManagement />} />
              <Route path="/admin/approvals/beekeeper" element={<BeekeeperApprovals />} />
              <Route path="/admin/approvals/hive" element={<HiveApprovals />} />
              <Route path="/admin/approvals/batch" element={<BatchApprovals />} />
              <Route path="/admin/approvals/processing" element={<ProcessingApprovals />} />
              <Route path="/admin/blockchain" element={<BlockchainExplorer />} />
              <Route path="/admin/audit-logs" element={<AuditLogs />} />
              <Route path="/admin/reports" element={<AdminReports />} />
              
              {/* Beekeeper Routes */}
              <Route path="/beekeeper/dashboard" element={<BeekeeperDashboard />} />
              <Route path="/beekeeper/profile" element={<BeekeeperProfile />} />
              <Route path="/beekeeper/apiaries" element={<ApiariesManagement />} />
              <Route path="/beekeeper/hives" element={<HivesManagement />} />
              <Route path="/beekeeper/harvest" element={<HarvestManagement />} />
              <Route path="/beekeeper/batches" element={<HoneyBatchesManagement />} />
              <Route path="/beekeeper/ai-alerts" element={<AIAlerts />} />
              <Route path="/beekeeper/reports" element={<BeekeeperReports />} />
              
              {/* Hive Routes */}
              <Route path="/hive/:id" element={<HiveDetails />} />
              <Route path="/hive/:id/health" element={<HiveHealth />} />
              <Route path="/hive/:id/sensors" element={<SensorData />} />
              <Route path="/hive/:id/history" element={<HiveHistory />} />
              
              {/* Processing Routes */}
              <Route path="/processing/dashboard" element={<ProcessingDashboard />} />
              <Route path="/processing/incoming" element={<IncomingBatches />} />
              <Route path="/processing/quality" element={<QualityTesting />} />
              <Route path="/processing/process" element={<ProcessingSteps />} />
              <Route path="/processing/packaging" element={<PackagingManagement />} />
              
              {/* Distributor Routes */}
              <Route path="/distributor/dashboard" element={<DistributorDashboard />} />
              <Route path="/distributor/inventory" element={<InventoryManagement />} />
              <Route path="/distributor/shipments" element={<ShipmentsManagement />} />
              <Route path="/distributor/tracking" element={<TrackingInfo />} />
              
              {/* Retailer Routes */}
              <Route path="/retailer/dashboard" element={<RetailerDashboard />} />
              <Route path="/retailer/inventory" element={<RetailerInventory />} />
              <Route path="/retailer/products" element={<RetailerProducts />} />
              <Route path="/retailer/sales" element={<SalesManagement />} />
              
              {/* Consumer Routes */}
              <Route path="/consumer" element={<ConsumerHome />} />
              <Route path="/consumer/qr-scan" element={<QRScanner />} />
              <Route path="/consumer/journey" element={<ProductJourney />} />
              <Route path="/consumer/verify" element={<VerificationResult />} />
              
              {/* Verification Routes */}
              <Route path="/verify/batch/:batchId" element={<VerifyBatch />} />
              <Route path="/verify/blockchain/:hash" element={<BlockchainProof />} />
              
              {/* Default */}
              <Route path="/" element={isAuthenticated ? <BeekeeperDashboard /> : <Login />} />
            </Routes>
          </div>
        </div>
      </AuthContext.Provider>
    </Router>
  );
}

export default App;
