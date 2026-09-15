import React, { useState } from 'react';
import './Login.css';

const API_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000';

const Login = ({ onLoginSuccess }) => {
    const [username, setUsername] = useState('admin');
    const [password, setPassword] = useState('admin123');
    const [error, setError] = useState('');
    const [loading, setLoading] = useState(false);

    const handleLogin = async (e) => {
        e.preventDefault();
        setLoading(true);
        setError('');

        try {
            const response = await fetch(`${API_URL}/api/auth/users/login/`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ username, password })
            });

            if (!response.ok) {
                throw new Error('Invalid credentials');
            }

            const data = await response.json();
            localStorage.setItem('token', data.token);
            localStorage.setItem('username', username);
            localStorage.setItem('role', data.user?.profile?.role || 'consumer');
            onLoginSuccess(data.token);
        } catch (err) {
            setError(err.message || 'Login failed');
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="login-container">
            <div className="login-box">
                <h1>🍯 Honey Chain</h1>
                <p className="subtitle">Blockchain-Based Honey Traceability</p>

                <form onSubmit={handleLogin}>
                    <div className="form-group">
                        <label>Username</label>
                        <input
                            type="text"
                            value={username}
                            onChange={(e) => setUsername(e.target.value)}
                            placeholder="admin"
                        />
                    </div>

                    <div className="form-group">
                        <label>Password</label>
                        <input
                            type="password"
                            value={password}
                            onChange={(e) => setPassword(e.target.value)}
                            placeholder="admin123"
                        />
                    </div>

                    {error && <div className="error-message">{error}</div>}

                    <button type="submit" disabled={loading}>
                        {loading ? 'Logging in...' : 'Login'}
                    </button>
                </form>

                <div className="demo-credentials">
                    <p><strong>Demo Credentials:</strong></p>
                    <p>Username: admin</p>
                    <p>Password: admin123</p>
                </div>
            </div>
        </div>
    );
};

export default Login;
