/**
 * Alerts Component
 * Reusable alert/notification component
 */

import React from 'react';
import './Alerts.css';

const Alerts = ({ type = 'info', message = '', title = '', dismissible = true }) => {
    const [visible, setVisible] = React.useState(true);

    if (!visible) return null;

    const getAlertClass = (type) => {
        switch (type?.toLowerCase()) {
            case 'success':
                return 'alert--success';
            case 'error':
            case 'danger':
                return 'alert--error';
            case 'warning':
                return 'alert--warning';
            case 'info':
            default:
                return 'alert--info';
        }
    };

    return (
        <div className={`alert ${getAlertClass(type)}`}>
            <div className="alert-content">
                {title && <h5>{title}</h5>}
                <p>{message}</p>
            </div>
            {dismissible && (
                <button
                    className="alert-close"
                    onClick={() => setVisible(false)}
                    aria-label="Close alert"
                >
                    ×
                </button>
            )}
        </div>
    );
};

export default Alerts;
export { Alerts };
