/**
 * Loading Component
 * Reusable loading indicator/spinner
 */

import React from 'react';
import './Loading.css';

const Loading = ({ size = 'medium', fullscreen = false }) => {
    const loadingContent = (
        <div className={`loading loading--${size}`}>
            <div className="spinner"></div>
            <p>Loading...</p>
        </div>
    );

    if (fullscreen) {
        return (
            <div className="loading-fullscreen">
                {loadingContent}
            </div>
        );
    }

    return loadingContent;
};

export default Loading;
export { Loading };
