/**
 * Navbar Component
 * Main navigation bar component
 */

import React, { useContext } from 'react';
import { AuthContext } from '../../context/AuthContext';
import './Navbar.css';

const Navbar = () => {
    const { user, logout } = useContext(AuthContext);

    return (
        <nav className="navbar">
            <div className="navbar-brand">
                <h1>🍯 Honey Chain</h1>
            </div>
            <div className="navbar-menu">
                <ul className="navbar-items">
                    <li><a href="/dashboard">Dashboard</a></li>
                    <li><a href="/profile">Profile</a></li>
                    <li>
                        <button onClick={logout}>Logout</button>
                    </li>
                </ul>
            </div>
            {user && <span className="navbar-user">{user.username}</span>}
        </nav>
    );
};

export default Navbar;
export { Navbar };
