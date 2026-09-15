import React, { useState, useEffect } from 'react';
import './BatchTracker.css';

const BatchTracker = ({ token }) => {
    const [batches, setBatches] = useState([]);
    const [selectedBatch, setSelectedBatch] = useState(null);
    const [loading, setLoading] = useState(true);
    const [qrImages, setQrImages] = useState({});
    const [qrLoading, setQrLoading] = useState(null);

    useEffect(() => {
        fetchBatches();
    }, [token]);

    const fetchBatches = async () => {
        try {
            const response = await fetch('http://localhost:8000/api/batch/', {
                headers: { 'Authorization': `Token ${token}` }
            });
            const data = await response.json();
            setBatches(Array.isArray(data) ? data : (data.results ?? []));
        } catch (error) {
            console.error('Error fetching batches:', error);
        } finally {
            setLoading(false);
        }
    };

    const getStatusColor = (status) => {
        const colors = {
            'created': '#FFA500',
            'processing': '#4169E1',
            'completed': '#32CD32',
            'shipped': '#FF6347'
        };
        return colors[status] || '#808080';
    };

    const handleGenerateQR = async (batch) => {
        setQrLoading(batch.id);
        try {
            const headers = { 'Authorization': `Token ${token}` };

            const listRes = await fetch('http://localhost:8000/api/qr/', { headers });
            const listData = await listRes.json();
            const qrList = Array.isArray(listData) ? listData : (listData.results ?? []);
            let qrEntry = qrList.find(q => q.batch === batch.id);

            if (!qrEntry) {
                const createRes = await fetch('http://localhost:8000/api/qr/', {
                    method: 'POST',
                    headers: { ...headers, 'Content-Type': 'application/json' },
                    body: JSON.stringify({ batch: batch.id, code_data: batch.batch_id })
                });
                qrEntry = await createRes.json();
            }

            if (!qrEntry.qr_image) {
                const genRes = await fetch(`http://localhost:8000/api/qr/${qrEntry.id}/generate/`, {
                    method: 'POST',
                    headers
                });
                qrEntry = await genRes.json();
            }

            setQrImages(prev => ({ ...prev, [batch.id]: qrEntry.qr_image }));
        } catch (error) {
            console.error('Error generating QR:', error);
            alert('Failed to generate QR code');
        } finally {
            setQrLoading(null);
        }
    };

    if (loading) {
        return <div className="loading">Loading batches...</div>;
    }

    return (
        <div className="batch-tracker">
            <h1>📦 Batch Tracker</h1>

            {batches.length === 0 ? (
                <p className="no-data">No batches found</p>
            ) : (
                <div className="batches-list">
                    {batches.map(batch => (
                        <div
                            key={batch.id}
                            className="batch-item"
                            onClick={() => setSelectedBatch(selectedBatch?.id === batch.id ? null : batch)}
                        >
                            <div className="batch-header">
                                <div className="batch-id">{batch.batch_id}</div>
                                <div
                                    className="batch-status"
                                    style={{ backgroundColor: getStatusColor(batch.status) }}
                                >
                                    {batch.status.toUpperCase()}
                                </div>
                            </div>

                            {selectedBatch?.id === batch.id && (
                                <div className="batch-details">
                                    <div className="detail-row">
                                        <span className="label">Honey Type:</span>
                                        <span className="value">{batch.honey_type}</span>
                                    </div>
                                    <div className="detail-row">
                                        <span className="label">Quantity:</span>
                                        <span className="value">{batch.total_quantity} kg</span>
                                    </div>
                                    <div className="detail-row">
                                        <span className="label">Created:</span>
                                        <span className="value">{new Date(batch.created_at).toLocaleDateString()}</span>
                                    </div>

                                    <div style={{ marginTop: '12px' }}>
                                        <button
                                            onClick={(e) => { e.stopPropagation(); handleGenerateQR(batch); }}
                                            disabled={qrLoading === batch.id}
                                            style={{
                                                padding: '8px 16px',
                                                background: '#667eea',
                                                color: 'white',
                                                border: 'none',
                                                borderRadius: '6px',
                                                cursor: 'pointer'
                                            }}
                                        >
                                            {qrLoading === batch.id ? 'Generating...' : 'Generate / View QR'}
                                        </button>

                                        {qrImages[batch.id] && (
                                            <div style={{ marginTop: '12px' }}>
                                                <img
                                                    src={qrImages[batch.id]}
                                                    alt="QR Code"
                                                    style={{ width: '160px', height: '160px', border: '1px solid #ddd', borderRadius: '8px' }}
                                                />
                                            </div>
                                        )}
                                    </div>
                                </div>
                            )}
                        </div>
                    ))}
                </div>
            )}
        </div>
    );
};

export default BatchTracker;
