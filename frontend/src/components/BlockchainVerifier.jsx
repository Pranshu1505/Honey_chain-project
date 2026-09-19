import React, { useState, useEffect } from 'react';
import './BlockchainVerifier.css';

const BlockchainVerifier = ({ token }) => {
    const [records, setRecords] = useState([]);
    const [searchBatchId, setSearchBatchId] = useState('');
    const [verifyResult, setVerifyResult] = useState(null);
    const [loading, setLoading] = useState(true);

    const [createBatchId, setCreateBatchId] = useState('');
    const [createOrigin, setCreateOrigin] = useState('');
    const [creating, setCreating] = useState(false);
    const [createError, setCreateError] = useState(null);

    useEffect(() => {
        fetchRecords();
    }, [token]);

    const fetchRecords = async () => {
        try {
            const response = await fetch('https://honey-chain-project-backend.onrender.com/api/blockchain/records/', {
                headers: { 'Authorization': `Token ${token}` }
            });
            const data = await response.json();
            setRecords(Array.isArray(data) ? data : (data.results ?? []));
        } catch (error) {
            console.error('Error fetching blockchain records:', error);
        } finally {
            setLoading(false);
        }
    };

    const handleVerify = async (e) => {
        e.preventDefault();

        if (!searchBatchId) {
            alert('Please enter a batch ID');
            return;
        }

        try {
            const response = await fetch(
                `https://honey-chain-project-backend.onrender.com/api/blockchain/records/verify/?batch_id=${searchBatchId}`,
                {
                    headers: { 'Authorization': `Token ${token}` }
                }
            );
            const data = await response.json();
            setVerifyResult(data);
        } catch (error) {
            console.error('Error verifying batch:', error);
            setVerifyResult({ verified: false, error: 'Verification failed' });
        }
    };

    const handleCreateRecord = async (e) => {
        e.preventDefault();
        setCreateError(null);

        if (!createBatchId) {
            setCreateError('Please enter a batch ID');
            return;
        }

        setCreating(true);
        try {
            const response = await fetch(
                'https://honey-chain-project-backend.onrender.com/api/blockchain/records/create_record/',
                {
                    method: 'POST',
                    headers: {
                        'Authorization': `Token ${token}`,
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        batch_id: createBatchId,
                        origin: createOrigin || 'Unknown'
                    })
                }
            );
            const data = await response.json();

            if (response.ok) {
                alert('Batch recorded on blockchain!');
                setCreateBatchId('');
                setCreateOrigin('');
                fetchRecords();
            } else {
                setCreateError(data.error || 'Failed to create record');
            }
        } catch (error) {
            console.error('Error creating blockchain record:', error);
            setCreateError('Failed to create record');
        } finally {
            setCreating(false);
        }
    };

    if (loading) {
        return <div className="loading">Loading blockchain records...</div>;
    }

    return (
        <div className="blockchain-verifier">
            <h1>⛓️ Blockchain Verification</h1>

            <form className="verify-form" onSubmit={handleCreateRecord}>
                <div className="form-group">
                    <label>Batch ID</label>
                    <input
                        type="text"
                        value={createBatchId}
                        onChange={(e) => setCreateBatchId(e.target.value)}
                        placeholder="e.g., HB2026-002"
                    />
                </div>
                <div className="form-group">
                    <label>Origin / Apiary</label>
                    <input
                        type="text"
                        value={createOrigin}
                        onChange={(e) => setCreateOrigin(e.target.value)}
                        placeholder="e.g., Abhishek's Apiary"
                    />
                </div>
                <button type="submit" className="btn-primary" disabled={creating}>
                    {creating ? 'Recording...' : 'Record on Blockchain'}
                </button>
            </form>

            {createError && (
                <div className="verify-result not-verified">
                    <p>{createError}</p>
                </div>
            )}

            <hr style={{ margin: '24px 0' }} />

            <form className="verify-form" onSubmit={handleVerify}>
                <div className="form-group">
                    <label>Batch ID</label>
                    <input
                        type="text"
                        value={searchBatchId}
                        onChange={(e) => setSearchBatchId(e.target.value)}
                        placeholder="e.g., HB2026-002"
                    />
                </div>
                <button type="submit" className="btn-primary">Verify Batch</button>
            </form>

            {verifyResult && (
                <div className={`verify-result ${verifyResult.verified ? 'verified' : 'not-verified'}`}>
                    {verifyResult.verified ? (
                        <>
                            <div className="result-icon">✅</div>
                            <h2>Batch Verified!</h2>
                            <div className="result-details">
                                <div className="detail-row">
                                    <span className="label">Batch ID:</span>
                                    <span className="value">{verifyResult.record.batch_id}</span>
                                </div>
                                <div className="detail-row">
                                    <span className="label">Origin:</span>
                                    <span className="value">{verifyResult.record.origin}</span>
                                </div>
                                <div className="detail-row">
                                    <span className="label">Honey Type:</span>
                                    <span className="value">{verifyResult.record.honey_type}</span>
                                </div>
                                <div className="detail-row">
                                    <span className="label">Quantity:</span>
                                    <span className="value">{verifyResult.record.quantity} kg</span>
                                </div>
                                <div className="detail-row">
                                    <span className="label">Quality Score:</span>
                                    <span className="value">{verifyResult.record.quality_score}/100</span>
                                </div>
                                <div className="detail-row">
                                    <span className="label">Transaction Hash:</span>
                                    <span className="value hash">{verifyResult.record.transaction_hash}</span>
                                </div>
                                <div className="detail-row">
                                    <span className="label">Block Number:</span>
                                    <span className="value">{verifyResult.record.block_number}</span>
                                </div>
                            </div>
                        </>
                    ) : (
                        <>
                            <div className="result-icon">❌</div>
                            <h2>Batch Not Verified</h2>
                            <p>{verifyResult.error || 'Batch not found on blockchain'}</p>
                        </>
                    )}
                </div>
            )}

            <hr style={{ margin: '24px 0' }} />

            <h2>All Blockchain Records</h2>
            {records.length === 0 ? (
                <p className="no-data">No blockchain records found</p>
            ) : (
                <div className="records-list">
                    {records.map(r => (
                        <div key={r.id} className="record-card">
                            <strong>{r.batch_id}</strong> - {r.honey_type}
                            <div className="record-meta">
                                Origin: {r.origin} | Qty: {r.quantity}kg | Block #{r.block_number}
                            </div>
                        </div>
                    ))}
                </div>
            )}
        </div>
    );
};

export default BlockchainVerifier;