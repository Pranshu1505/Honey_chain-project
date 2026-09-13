/**
 * Sidebar Component
 * Navigation sidebar for main application layout
 */

import React, { useContext } from 'react';
import { AuthContext } from '../../context/AuthContext';
import './Sidebar.css';

const Sidebar = () => {
    const { user } = useContext(AuthContext);

    const getMenuItems = () => {
        if (!user) return [];

        const baseMenus = {
            admin: [
                { name: 'Dashboard', path: '/admin' },
                { name: 'Users', path: '/admin/users' },
                { name: 'Approvals', path: '/admin/approvals' },
                { name: 'Reports', path: '/admin/reports' },
                { name: 'Audit Logs', path: '/admin/audit-logs' },
            ],
            beekeeper: [
                { name: 'Dashboard', path: '/beekeeper' },
                { name: 'Apiaries', path: '/beekeeper/apiaries' },
                { name: 'Hives', path: '/beekeeper/hives' },
                { name: 'Harvest', path: '/beekeeper/harvest' },
                { name: 'Batches', path: '/beekeeper/batches' },
                { name: 'Alerts', path: '/beekeeper/alerts' },
            ],
            processor: [
                { name: 'Dashboard', path: '/processing' },
                { name: 'Incoming Batches', path: '/processing/incoming' },
                { name: 'Quality Tests', path: '/processing/quality' },
                { name: 'Processing', path: '/processing/process' },
            ],
            distributor: [
                { name: 'Dashboard', path: '/distributor' },
                { name: 'Inventory', path: '/distributor/inventory' },
                { name: 'Shipments', path: '/distributor/shipments' },
                { name: 'Tracking', path: '/distributor/tracking' },
            ],
            retailer: [
                { name: 'Dashboard', path: '/retailer' },
                { name: 'Inventory', path: '/retailer/inventory' },
                { name: 'Products', path: '/retailer/products' },
                { name: 'Sales', path: '/retailer/sales' },
            ],
        };

        return baseMenus[user.role] || [];
    };

    return (
        <aside className="sidebar">
            <ul className="menu">
                {getMenuItems().map((item) => (
                    <li key={item.path}>
                        <a href={item.path}>{item.name}</a>
                    </li>
                ))}
            </ul>
        </aside>
    );
};

export default Sidebar;
export { Sidebar };
