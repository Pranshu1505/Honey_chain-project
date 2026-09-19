import React, { useState, useRef } from 'react';
import { Html5Qrcode } from 'html5-qrcode';

const API_BASE = 'https://honey-chain-project-backend.onrender.com';

const QRCodeScanner = ({ token }) => {
    const [scanning, setScanning] = useState(false);
    const [scannedData, setScannedData] = useState(null);
    const [verifyResult, setVerifyResult] = useState(null);
    const [error, setError] = useState(null);
    const scannerRef = useRef(null);
    const html5QrCodeRef = useRef(null);

    const [batchIdInput, setBatchIdInput] = useState('');
    const [qrImage, setQrImage] = useState(null);
    const [qrLoading, setQrLoading] = useState(false);
    const [qrError, setQrError] = useState(null);

    const handleShowQR = async () => {
        setQrError(null);
        setQrImage(null);
        if (!batchIdInput.trim()) {
            setQrError('Please enter a Batch ID');
            return;
        }
        setQrLoading(true);
        try {
            const headers = { 'Authorization': `Token ${token}` };

            const batchesRes = await fetch(`${API_BASE}/api/batch/`, { headers });
            const batchesData = await batchesRes.json();
            const batchList = Array.isArray(batchesData) ? batchesData : (batchesData.results ?? []);
            const batch = batchList.find(b => b.batch_id === batchIdInput.trim());

            if (!batch) {
                setQrError('Batch not found: ' + batchIdInput);
                setQrLoading(false);
                return;
            }

            const qrListRes = await fetch(`${API_BASE}/api/qr/`, { headers });
            const qrListData = await qrListRes.json();
            const qrList = Array.isArray(qrListData) ? qrListData : (qrListData.results ?? []);
            let qrEntry = qrList.find(q => q.batch === batch.id);

            if (!qrEntry) {
                const createRes = await fetch(`${API_BASE}/api/qr/`, {
                    method: 'POST',
                    headers: { ...headers, 'Content-Type': 'application/json' },
                    body: JSON.stringify({ batch: batch.id, code_data: batch.batch_id })
                });
                qrEntry = await createRes.json();
            }

            if (!qrEntry.qr_image_base64)  {
                const genRes = await fetch(`${API_BASE}/api/qr/${qrEntry.id}/generate/`, {
                    method: 'POST',
                    headers
                });
                qrEntry = await genRes.json();
            }

            setQrImage(qrEntry.qr_image_base64);
        } catch (err) {
            setQrError('Error: ' + err.message);
        } finally {
            setQrLoading(false);
        }
    };

    const startScanning = async () => {
        setError(null);
        setScannedData(null);
        setVerifyResult(null);
        setScanning(true);

        try {
            const html5QrCode = new Html5Qrcode('qr-reader');
            html5QrCodeRef.current = html5QrCode;

            await html5QrCode.start(
                { facingMode: 'environment' },
                { fps: 10, qrbox: { width: 250, height: 250 } },
                (decodedText) => {
                    handleScanSuccess(decodedText);
                },
                () => {}
            );
        } catch (err) {
            setError('Could not access camera: ' + err.message);
            setScanning(false);
        }
    };

    const stopScanning = async () => {
        if (html5QrCodeRef.current) {
            try {
                await html5QrCodeRef.current.stop();
                html5QrCodeRef.current.clear();
            } catch (err) {
                console.error('Error stopping scanner:', err);
            }
        }
        setScanning(false);
    };

    const handleScanSuccess = async (decodedText) => {
        await stopScanning();

        let parsed;
        try {
            parsed = JSON.parse(decodedText);
        } catch {
            parsed = { batch_id: decodedText };
        }
        setScannedData(parsed);

        if (parsed.batch_id) {
            try {
                const response = await fetch(
                    `${API_BASE}/api/blockchain/records/verify/?batch_id=${parsed.batch_id}`,
                    { headers: { 'Authorization': `Token ${token}` } }
                );
                const data = await response.json();
                setVerifyResult(data);
            } catch (err) {
                setError('Verification failed: ' + err.message);
            }
        }
    };

    return (
        <div style={{ padding: '20px' }}>
            <h1>�" QR Code Verification</h1>

            <div style={{ background: '#f0f4f8', padding: '20px', borderRadius: '12px', marginBottom: '24px' }}>
                <h3>Show QR Code (scan with any phone)</h3>
                <p style={{ color: '#666', fontSize: '14px' }}>
                    Enter a Batch ID to display its QR code. Scan it with any phone's camera or QR app.
                </p>
                <div style={{ display: 'flex', gap: '8px', marginTop: '12px' }}>
                    <input
                        type="text"
                        placeholder="e.g., BATCH-2026-001"
                        value={batchIdInput}
                        onChange={(e) => setBatchIdInput(e.target.value)}
                        style={{ flex: 1, padding: '10px', borderRadius: '6px', border: '1px solid #ccc' }}
                    />
                    <button
                        onClick={handleShowQR}
                        disabled={qrLoading}
                        style={{
                            padding: '10px 20px',
                            background: '#667eea',
                            color: 'white',
                            border: 'none',
                            borderRadius: '6px',
                            cursor: 'pointer'
                        }}
                    >
                        {qrLoading ? 'Loading...' : 'Show QR Code'}
                    </button>
                </div>

                {qrError && (
                    <div style={{ marginTop: '12px', padding: '10px', background: '#fed7d7', color: '#c53030', borderRadius: '6px' }}>
                        {qrError}
                    </div>
                )}

                {qrImage && (
                    <div style={{ marginTop: '16px', textAlign: 'center' }}>
                        <img
                            src={qrImage}
                            alt="QR Code"
                            style={{ width: '280px', height: '280px', border: '2px solid #667eea', borderRadius: '12px', background: 'white', padding: '10px' }}
                        />
                    </div>
                )}
            </div>

            <hr style={{ margin: '24px 0' }} />

            <h3>Or Scan Using This Device's Camera</h3>

            {!scanning ? (
                <button
                    onClick={startScanning}
                    style={{
                        padding: '12px 24px',
                        background: '#667eea',
                        color: 'white',
                        border: 'none',
                        borderRadius: '8px',
                        cursor: 'pointer',
                        fontSize: '16px'
                    }}
                >
                    Start Camera Scan
                </button>
            ) : (
                <button
                    onClick={stopScanning}
                    style={{
                        padding: '12px 24px',
                        background: '#e53e3e',
                        color: 'white',
                        border: 'none',
                        borderRadius: '8px',
                        cursor: 'pointer',
                        fontSize: '16px'
                    }}
                >
                    Stop Scanning
                </button>
            )}

            <div id="qr-reader" ref={scannerRef} style={{ width: '100%', maxWidth: '400px', marginTop: '20px', margin: '20px auto 0' }}></div>

            {error && (
                <div style={{ marginTop: '16px', padding: '12px', background: '#fed7d7', color: '#c53030', borderRadius: '8px' }}>
                    {error}
                </div>
            )}

            {scannedData && (
                <div style={{ marginTop: '16px', padding: '16px', background: '#f0f4f8', borderRadius: '8px' }}>
                    <h3>Scanned Data:</h3>
                    <pre>{JSON.stringify(scannedData, null, 2)}</pre>
                </div>
            )}

            {verifyResult && (
                <div style={{
                    marginTop: '16px',
                    padding: '16px',
                    background: verifyResult.verified ? '#c6f6d5' : '#fed7d7',
                    borderRadius: '8px'
                }}>
                    <h3>{verifyResult.verified ? '✅ Verified!' : '� Not Verified'}</h3>
                    {verifyResult.verified && (
                        <div>
                            <p><strong>Batch:</strong> {verifyResult.record.batch_id}</p>
                            <p><strong>Origin:</strong> {verifyResult.record.origin}</p>
                            <p><strong>Type:</strong> {verifyResult.record.honey_type}</p>
                            <p><strong>Quality Score:</strong> {verifyResult.record.quality_score}/100</p>
                        </div>
                    )}
                </div>
            )}
        </div>
    );
};

export default QRCodeScanner;
