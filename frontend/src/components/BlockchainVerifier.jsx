import React, { useState, useEffect } from 'react';
import './BlockchainVerifier.css';

const BlockchainVerifier = ({ token }) => {
    const [records, setRecords] = useState([]);
    const [searchBatchId, setSearchBatchId] = useState('');
    const [verifyResult, setVerifyResult] = useState(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        fetchRecords();
    }, [token]);

    const fetchRecords = async () => {
        try {
            const response = await fetch('http://localhost:8000/api/blockchain/records/', {
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
                `http://localhost:8000/api/blockchain/records/verify/?batch_id=${searchBatchId}`,
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

    if (loading) {
        return <div className="loading">Loading blockchain records...</div>;
    }

    return (
        <div className="blockchain-verifier">
            <h1>⛓️ Blockchain Verification</h1>

            <form className="verify-form" onSubmit={handleVerify}>
                <div className="form-group">
                    <label>Batch ID</label>
                    <input
                        type="text"
                        value={searchBatchId}
                        onChange={(e) => setSearchBatchId(e.target.value)}
                        placeholder="e.g., BATCH-2024-001"
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
                            <p>{verifyResult.error}</p>
                        </>
                    )}
                </div>
            )}

            <div className="records-section">
                <h2>All Blockchain Records</h2>
                {records.length === 0 ? (
                    <p className="no-data">No blockchain records found</p>
                ) : (
                    <div className="records-list">
                        {records.map(record => (
                            <div key={record.id} className="record-card">
                                <div className="card-header">
                                    <h3>{record.batch_id}</h3>
                                    <span className="quality-badge">{record.quality_score}/100</span>
                                </div>
                                <div className="card-body">
                                    <p><strong>Origin:</strong> {record.origin}</p>
                                    <p><strong>Type:</strong> {record.honey_type}</p>
                                    <p><strong>Quantity:</strong> {record.quantity} kg</p>
                                    <p><strong>Block:</strong> {record.block_number}</p>
                                </div>
                            </div>
                        ))}
                    </div>
                )}
            </div>
        </div>
    );
};

export default BlockchainVerifier;
