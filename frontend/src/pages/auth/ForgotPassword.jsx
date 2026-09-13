import React, { useState } from 'react';
import './ForgotPassword.css';

/**
 * Forgot Password Page Component
 */
const ForgotPassword = () => {
    const [email, setEmail] = useState('');
    const [submitted, setSubmitted] = useState(false);

    const handleChange = (e) => {
        setEmail(e.target.value);
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        // TODO: Implement password reset logic using AuthService
        setSubmitted(true);
    };

    return (
        <div className="forgot-password-container">
            <div className="forgot-password-form">
                <h1>Reset Password</h1>
                {!submitted ? (
                    <form onSubmit={handleSubmit}>
                        <p>Enter your email address and we'll send you a link to reset your password.</p>
                        <input
                            type="email"
                            placeholder="Email Address"
                            value={email}
                            onChange={handleChange}
                            required
                        />
                        <button type="submit">Send Reset Link</button>
                    </form>
                ) : (
                    <div className="success-message">
                        <p>✓ Check your email for the password reset link!</p>
                        <a href="/login">Back to Login</a>
                    </div>
                )}
            </div>
        </div>
    );
};

export default ForgotPassword;
