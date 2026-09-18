import React, { useState, useEffect } from 'react';
import './BatchTracker.css';

const BatchTracker = ({ token }) => {
    const [batches, setBatches] = useState([]);
    const [selectedBatch, setSelectedBatch] = useState(null);
    const [loading, setLoading] = useState(true);
    const [qrImages, setQrImages] = useState({});
    const [qrLoading, setQrLoading] = useState(null);
    const [showForm, setShowForm] = useState(false);
    const [formData, setFormData] = useState({
        batch_id: '',
        harvests: '',
        total_quantity: '',
        honey_type: '',
        status: 'created',
        quality_score: ''
    });

    useEffect(() => {
        fetchBatches();
    }, [token]);

    const fetchBatches = async () => {
        try {
            const response = await fetch('https://honey-chain-project-backend.onrender.com/api/batch/', {
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

    const handleSubmit = async (e) => {
        e.preventDefault();

        try {
            const harvestIds = formData.harvests
                .split(',')
                .map(id => id.trim())
                .filter(id => id.length > 0)
                .map(Number);

            const response = await fetch('https://honey-chain-project-backend.onrender.com/api/batch/', {
                method: 'POST',
                headers: {
                    'Authorization': `Token ${token}`,
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    batch_id: formData.batch_id,
                    harvests: harvestIds,
                    total_quantity: Number(formData.total_quantity),
                    honey_type: formData.honey_type,
                    status: formData.status,
                    quality_score: formData.quality_score ? Number(formData.quality_score) : 0
                })
            });

            if (response.ok) {
                setFormData({
                    batch_id: '',
                    harvests: '',
                    total_quantity: '',
                    honey_type: '',
                    status: 'created',
                    quality_score: ''
                });
                setShowForm(false);
                fetchBatches();
                alert('Batch created successfully!');
            } else {
                const errorData = await response.json().catch(() => ({}));
                alert('Error creating batch: ' + JSON.stringify(errorData));
            }
        } catch (error) {
            console.error('Error creating batch:', error);
            alert('Error creating batch');
        }
    };

    const getStatusColor = (status) => {
        const colors = {
            'created': '#FFA500',
            'quality_tested': '#9370DB',
            'approved': '#20B2AA',
            'processing': '#4169E1',
            'packaged': '#32CD32',
            'shipped': '#FF6347'
        };
        return colors[status] || '#808080';
    };

    const handleGenerateQR = async (batch) => {
        setQrLoading(batch.id);
        try {
            const headers = { 'Authorization': `Token ${token}` };

            const listRes = await fetch('https://honey-chain-project-backend.onrender.com/api/qr/', { headers });
            const listData = await listRes.json();
            const qrList = Array.isArray(listData) ? listData : (listData.results ?? []);
            let qrEntry = qrList.find(q => q.batch === batch.id);

            if (!qrEntry) {
                const createRes = await fetch('https://honey-chain-project-backend.onrender.com/api/qr/', {
                    method: 'POST',
                    headers: { ...headers, 'Content-Type': 'application/json' },
                    body: JSON.stringify({ batch: batch.id, code_data: batch.batch_id })
                });
                qrEntry = await createRes.json();
            }

            if (!qrEntry.qr_image) {
                const genRes = await fetch(`https://honey-chain-project-backend.onrender.com/api/qr/${qrEntry.id}/generate/`, {
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
            <div className="batch-tracker-header">
                <h1>📦 Batch Tracker</h1>
                <button
                    className="btn-primary"
                    onClick={() => setShowForm(!showForm)}
                >
                    {showForm ? 'Cancel' : 'Add Batch'}
                </button>
            </div>

            {showForm && (
                <form className="batch-form" onSubmit={handleSubmit}>
                    <div className="form-group">
                        <label>Batch ID</label>
                        <input
                            type="text"
                            value={formData.batch_id}
                            onChange={(e) => setFormData({ ...formData, batch_id: e.target.value })}
                            placeholder="e.g. HB007"
                            required
                        />
                    </div>

                    <div className="form-group">
                        <label>Harvest IDs (comma separated)</label>
                        <input
                            type="text"
                            value={formData.harvests}
                            onChange={(e) => setFormData({ ...formData, harvests: e.target.value })}
                            placeholder="e.g. 1, 2"
                            required
                        />
                    </div>

                    <div className="form-group">
                        <label>Honey Type</label>
                        <input
                            type="text"
                            value={formData.honey_type}
                            onChange={(e) => setFormData({ ...formData, honey_type: e.target.value })}
                            placeholder="e.g. Wildflower"
                            required
                        />
                    </div>

                    <div className="form-group">
                        <label>Total Quantity (kg)</label>
                        <input
                            type="number"
                            step="0.1"
                            value={formData.total_quantity}
                            onChange={(e) => setFormData({ ...formData, total_quantity: e.target.value })}
                            required
                        />
                    </div>

                    <div className="form-group">
                        <label>Status</label>
                        <select
                            value={formData.status}
                            onChange={(e) => setFormData({ ...formData, status: e.target.value })}
                        >
                            <option value="created">Created</option>
                            <option value="quality_tested">Quality Tested</option>
                            <option value="approved">Approved</option>
                            <option value="processing">Processing</option>
                            <option value="packaged">Packaged</option>
                            <option value="shipped">Shipped</option>
                        </select>
                    </div>

                    <div className="form-group">
                        <label>Quality Score (0-100)</label>
                        <input
                            type="number"
                            min="0"
                            max="100"
                            value={formData.quality_score}
                            onChange={(e) => setFormData({ ...formData, quality_score: e.target.value })}
                        />
                    </div>

                    <button type="submit" className="btn-primary">Create Batch</button>
                </form>
            )}

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



// import React, { useState, useEffect } from 'react';
// import './BatchTracker.css';

// const BatchTracker = ({ token }) => {
//     const [batches, setBatches] = useState([]);
//     const [selectedBatch, setSelectedBatch] = useState(null);
//     const [loading, setLoading] = useState(true);
//     const [qrImages, setQrImages] = useState({});
//     const [qrLoading, setQrLoading] = useState(null);

//     useEffect(() => {
//         fetchBatches();
//     }, [token]);

//     const fetchBatches = async () => {
//         try {
//             const response = await fetch('https://honey-chain-project-backend.onrender.com/api/batch/', {
//                 headers: { 'Authorization': `Token ${token}` }
//             });
//             const data = await response.json();
//             setBatches(Array.isArray(data) ? data : (data.results ?? []));
//         } catch (error) {
//             console.error('Error fetching batches:', error);
//         } finally {
//             setLoading(false);
//         }
//     };

//     const getStatusColor = (status) => {
//         const colors = {
//             'created': '#FFA500',
//             'processing': '#4169E1',
//             'completed': '#32CD32',
//             'shipped': '#FF6347'
//         };
//         return colors[status] || '#808080';
//     };

//     const handleGenerateQR = async (batch) => {
//         setQrLoading(batch.id);
//         try {
//             const headers = { 'Authorization': `Token ${token}` };

//             const listRes = await fetch('https://honey-chain-project-backend.onrender.com/api/qr/', { headers });
//             const listData = await listRes.json();
//             const qrList = Array.isArray(listData) ? listData : (listData.results ?? []);
//             let qrEntry = qrList.find(q => q.batch === batch.id);

//             if (!qrEntry) {
//                 const createRes = await fetch('https://honey-chain-project-backend.onrender.com/api/qr/', {
//                     method: 'POST',
//                     headers: { ...headers, 'Content-Type': 'application/json' },
//                     body: JSON.stringify({ batch: batch.id, code_data: batch.batch_id })
//                 });
//                 qrEntry = await createRes.json();
//             }

//             if (!qrEntry.qr_image) {
//                 const genRes = await fetch(`https://honey-chain-project-backend.onrender.com/api/qr/${qrEntry.id}/generate/`, {
//                     method: 'POST',
//                     headers
//                 });
//                 qrEntry = await genRes.json();
//             }

//             setQrImages(prev => ({ ...prev, [batch.id]: qrEntry.qr_image }));
//         } catch (error) {
//             console.error('Error generating QR:', error);
//             alert('Failed to generate QR code');
//         } finally {
//             setQrLoading(null);
//         }
//     };

//     if (loading) {
//         return <div className="loading">Loading batches...</div>;
//     }

//     return (
//         <div className="batch-tracker">
//             <h1>📦 Batch Tracker</h1>

//             {batches.length === 0 ? (
//                 <p className="no-data">No batches found</p>
//             ) : (
//                 <div className="batches-list">
//                     {batches.map(batch => (
//                         <div
//                             key={batch.id}
//                             className="batch-item"
//                             onClick={() => setSelectedBatch(selectedBatch?.id === batch.id ? null : batch)}
//                         >
//                             <div className="batch-header">
//                                 <div className="batch-id">{batch.batch_id}</div>
//                                 <div
//                                     className="batch-status"
//                                     style={{ backgroundColor: getStatusColor(batch.status) }}
//                                 >
//                                     {batch.status.toUpperCase()}
//                                 </div>
//                             </div>

//                             {selectedBatch?.id === batch.id && (
//                                 <div className="batch-details">
//                                     <div className="detail-row">
//                                         <span className="label">Honey Type:</span>
//                                         <span className="value">{batch.honey_type}</span>
//                                     </div>
//                                     <div className="detail-row">
//                                         <span className="label">Quantity:</span>
//                                         <span className="value">{batch.total_quantity} kg</span>
//                                     </div>
//                                     <div className="detail-row">
//                                         <span className="label">Created:</span>
//                                         <span className="value">{new Date(batch.created_at).toLocaleDateString()}</span>
//                                     </div>

//                                     <div style={{ marginTop: '12px' }}>
//                                         <button
//                                             onClick={(e) => { e.stopPropagation(); handleGenerateQR(batch); }}
//                                             disabled={qrLoading === batch.id}
//                                             style={{
//                                                 padding: '8px 16px',
//                                                 background: '#667eea',
//                                                 color: 'white',
//                                                 border: 'none',
//                                                 borderRadius: '6px',
//                                                 cursor: 'pointer'
//                                             }}
//                                         >
//                                             {qrLoading === batch.id ? 'Generating...' : 'Generate / View QR'}
//                                         </button>

//                                         {qrImages[batch.id] && (
//                                             <div style={{ marginTop: '12px' }}>
//                                                 <img
//                                                     src={qrImages[batch.id]}
//                                                     alt="QR Code"
//                                                     style={{ width: '160px', height: '160px', border: '1px solid #ddd', borderRadius: '8px' }}
//                                                 />
//                                             </div>
//                                         )}
//                                     </div>
//                                 </div>
//                             )}
//                         </div>
//                     ))}
//                 </div>
//             )}
//         </div>
//     );
// };

// export default BatchTracker;
