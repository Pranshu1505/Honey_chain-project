/**
 * QRScanner Component
 * QR code scanning functionality for consumer verification
 */

import React, { useState } from 'react';
import { QrService } from '../../services/api';
import './QRScanner.css';

const QRScanner = ({ onScanComplete }) => {
    const [scanning, setScanning] = useState(false);
    const [result, setResult] = useState(null);
    const [error, setError] = useState(null);

    const handleScan = async (data) => {
        setScanning(false);
        try {
            const verified = await QrService.scan(data);
            setResult(verified);
            if (onScanComplete) {
                onScanComplete(verified);
            }
        } catch (err) {
            setError(err.message);
        }
    };

    const startScanning = () => {
        setScanning(true);
        setError(null);
    };

    const handleFileInput = (e) => {
        const file = e.target.files?.[0];
        if (file) {
            // TODO: Implement QR code reading from image file
            // This would require a QR code library like jsQR or jsbarcode
        }
    };

    return (
        <div className="qr-scanner">
            <h3>Scan QR Code</h3>

            {scanning ? (
                <div className="scanner-active">
                    <div className="scan-area">
                        <p>Point your camera at the QR code</p>
                        {/* TODO: Add video element for camera feed */}
                    </div>
                </div>
            ) : (
                <div className="scanner-inactive">
                    <button onClick={startScanning} className="scan-button">
                        📷 Start Scanning
                    </button>
                    <p>or</p>
                    <input
                        type="file"
                        accept="image/*"
                        onChange={handleFileInput}
                        className="file-input"
                    />
                </div>
            )}

            {error && <p className="error">{error}</p>}

            {result && (
                <div className="scan-result">
                    <h4>✓ Scan Successful</h4>
                    <pre>{JSON.stringify(result, null, 2)}</pre>
                </div>
            )}
        </div>
    );
};

export default QRScanner;
export { QRScanner };
