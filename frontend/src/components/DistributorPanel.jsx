import React, { useState, useEffect } from 'react';

const API_BASE = 'http://localhost:8000';

const DistributorPanel = ({ token }) => {
    const [tab, setTab] = useState('shipments');
    const [shipments, setShipments] = useState([]);
    const [inventory, setInventory] = useState([]);
    const [loading, setLoading] = useState(true);
    const [showForm, setShowForm] = useState(false);
    const [shipForm, setShipForm] = useState({
        distributor: '', batch_id: '', destination: '', quantity: '',
        expected_delivery: '', tracking_number: '', notes: ''
    });
    const [invForm, setInvForm] = useState({
        distributor: '', batch_id: '', honey_type: '', quantity: '',
        received_date: '', expiry_date: '', quality_score: '', storage_location: ''
    });

    const headers = { 'Authorization': `Token ${token}`, 'Content-Type': 'application/json' };

    useEffect(() => {
        fetchData();
    }, [token]);

    const fetchData = async () => {
        setLoading(true);
        try {
            const [shipRes, invRes] = await Promise.all([
                fetch(`/api/distributor/shipments/`, { headers }),
                fetch(`/api/distributor/inventory/`, { headers })
            ]);
            const shipData = await shipRes.json();
            const invData = await invRes.json();
            setShipments(Array.isArray(shipData) ? shipData : (shipData.results ?? []));
            setInventory(Array.isArray(invData) ? invData : (invData.results ?? []));
        } catch (err) {
            console.error('Error fetching distributor data:', err);
        } finally {
            setLoading(false);
        }
    };

    const handleShipSubmit = async (e) => {
        e.preventDefault();
        try {
            const res = await fetch(`/api/distributor/shipments/`, {
                method: 'POST',
                headers,
                body: JSON.stringify({
                    ...shipForm,
                    distributor: parseInt(shipForm.distributor),
                    quantity: parseFloat(shipForm.quantity)
                })
            });
            if (res.ok) {
                setShowForm(false);
                fetchData();
                alert('Shipment created!');
            } else {
                const err = await res.json();
                alert('Error: ' + JSON.stringify(err));
            }
        } catch (err) {
            alert('Error creating shipment');
        }
    };

    const handleInvSubmit = async (e) => {
        e.preventDefault();
        try {
            const res = await fetch(`/api/distributor/inventory/`, {
                method: 'POST',
                headers,
                body: JSON.stringify({
                    ...invForm,
                    distributor: parseInt(invForm.distributor),
                    quantity: parseFloat(invForm.quantity),
                    quality_score: parseInt(invForm.quality_score)
                })
            });
            if (res.ok) {
                setShowForm(false);
                fetchData();
                alert('Inventory item added!');
            } else {
                const err = await res.json();
                alert('Error: ' + JSON.stringify(err));
            }
        } catch (err) {
            alert('Error adding inventory');
        }
    };

    if (loading) return <div style={{ padding: '20px' }}>Loading...</div>;

    return (
        <div style={{ padding: '20px' }}>
            <h1>ðŸ“¦ Distributor Panel</h1>

            <div style={{ display: 'flex', gap: '10px', marginBottom: '20px' }}>
                <button onClick={() => { setTab('shipments'); setShowForm(false); }}
                    style={{ padding: '10px 20px', background: tab === 'shipments' ? '#667eea' : '#e2e8f0', color: tab === 'shipments' ? 'white' : '#333', border: 'none', borderRadius: '6px', cursor: 'pointer' }}>
                    Shipments
                </button>
                <button onClick={() => { setTab('inventory'); setShowForm(false); }}
                    style={{ padding: '10px 20px', background: tab === 'inventory' ? '#667eea' : '#e2e8f0', color: tab === 'inventory' ? 'white' : '#333', border: 'none', borderRadius: '6px', cursor: 'pointer' }}>
                    Inventory
                </button>
                <button onClick={() => setShowForm(!showForm)}
                    style={{ padding: '10px 20px', background: '#48bb78', color: 'white', border: 'none', borderRadius: '6px', cursor: 'pointer', marginLeft: 'auto' }}>
                    {showForm ? 'Cancel' : `+ New ${tab === 'shipments' ? 'Shipment' : 'Inventory Item'}`}
                </button>
            </div>

            {showForm && tab === 'shipments' && (
                <form onSubmit={handleShipSubmit} style={{ background: '#f7fafc', padding: '20px', borderRadius: '10px', marginBottom: '20px', display: 'grid', gridTemplateColumns: 'repeat(2, 1fr)', gap: '12px' }}>
                    <input placeholder="Distributor ID" value={shipForm.distributor} onChange={e => setShipForm({...shipForm, distributor: e.target.value})} required style={{ padding: '8px' }} />
                    <input placeholder="Batch ID" value={shipForm.batch_id} onChange={e => setShipForm({...shipForm, batch_id: e.target.value})} required style={{ padding: '8px' }} />
                    <input placeholder="Destination" value={shipForm.destination} onChange={e => setShipForm({...shipForm, destination: e.target.value})} required style={{ padding: '8px' }} />
                    <input placeholder="Quantity (kg)" type="number" value={shipForm.quantity} onChange={e => setShipForm({...shipForm, quantity: e.target.value})} required style={{ padding: '8px' }} />
                    <input placeholder="Expected Delivery (YYYY-MM-DDTHH:MM)" type="datetime-local" value={shipForm.expected_delivery} onChange={e => setShipForm({...shipForm, expected_delivery: e.target.value})} required style={{ padding: '8px' }} />
                    <input placeholder="Tracking Number" value={shipForm.tracking_number} onChange={e => setShipForm({...shipForm, tracking_number: e.target.value})} required style={{ padding: '8px' }} />
                    <input placeholder="Notes" value={shipForm.notes} onChange={e => setShipForm({...shipForm, notes: e.target.value})} style={{ padding: '8px', gridColumn: 'span 2' }} />
                    <button type="submit" style={{ padding: '10px', background: '#667eea', color: 'white', border: 'none', borderRadius: '6px', gridColumn: 'span 2' }}>Create Shipment</button>
                </form>
            )}

            {showForm && tab === 'inventory' && (
                <form onSubmit={handleInvSubmit} style={{ background: '#f7fafc', padding: '20px', borderRadius: '10px', marginBottom: '20px', display: 'grid', gridTemplateColumns: 'repeat(2, 1fr)', gap: '12px' }}>
                    <input placeholder="Distributor ID" value={invForm.distributor} onChange={e => setInvForm({...invForm, distributor: e.target.value})} required style={{ padding: '8px' }} />
                    <input placeholder="Batch ID" value={invForm.batch_id} onChange={e => setInvForm({...invForm, batch_id: e.target.value})} required style={{ padding: '8px' }} />
                    <input placeholder="Honey Type" value={invForm.honey_type} onChange={e => setInvForm({...invForm, honey_type: e.target.value})} required style={{ padding: '8px' }} />
                    <input placeholder="Quantity (kg)" type="number" value={invForm.quantity} onChange={e => setInvForm({...invForm, quantity: e.target.value})} required style={{ padding: '8px' }} />
                    <input placeholder="Received Date" type="datetime-local" value={invForm.received_date} onChange={e => setInvForm({...invForm, received_date: e.target.value})} required style={{ padding: '8px' }} />
                    <input placeholder="Expiry Date" type="date" value={invForm.expiry_date} onChange={e => setInvForm({...invForm, expiry_date: e.target.value})} required style={{ padding: '8px' }} />
                    <input placeholder="Quality Score (0-100)" type="number" value={invForm.quality_score} onChange={e => setInvForm({...invForm, quality_score: e.target.value})} style={{ padding: '8px' }} />
                    <input placeholder="Storage Location" value={invForm.storage_location} onChange={e => setInvForm({...invForm, storage_location: e.target.value})} required style={{ padding: '8px' }} />
                    <button type="submit" style={{ padding: '10px', background: '#667eea', color: 'white', border: 'none', borderRadius: '6px', gridColumn: 'span 2' }}>Add Inventory</button>
                </form>
            )}

            {tab === 'shipments' && (
                shipments.length === 0 ? <p style={{ color: '#888' }}>No shipments found</p> :
                shipments.map(s => (
                    <div key={s.id} style={{ background: 'white', border: '1px solid #eee', borderRadius: '8px', padding: '16px', marginBottom: '10px' }}>
                        <strong>{s.tracking_number}</strong> - {s.batch_id} â†' {s.destination}
                        <div style={{ color: '#666', fontSize: '14px' }}>Qty: {s.quantity}kg | Status: {s.status}</div>
                    </div>
                ))
            )}

            {tab === 'inventory' && (
                inventory.length === 0 ? <p style={{ color: '#888' }}>No inventory found</p> :
                inventory.map(i => (
                    <div key={i.id} style={{ background: 'white', border: '1px solid #eee', borderRadius: '8px', padding: '16px', marginBottom: '10px' }}>
                        <strong>{i.batch_id}</strong> - {i.honey_type}
                        <div style={{ color: '#666', fontSize: '14px' }}>Qty: {i.quantity}kg | Location: {i.storage_location} | Status: {i.status}</div>
                    </div>
                ))
            )}
        </div>
    );
};

export default DistributorPanel;
