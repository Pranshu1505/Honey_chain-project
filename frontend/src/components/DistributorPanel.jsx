import React, { useState, useEffect } from 'react';
import './DistributorPanel.css';

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

    if (loading) return <div className="dp-loading">Loading...</div>;

    return (
        <div className="dp-container">
            <h1>📦 Distributor Panel</h1>

            <div className="dp-tabs">
                <button
                    className={`dp-tab-btn ${tab === 'shipments' ? 'active' : ''}`}
                    onClick={() => { setTab('shipments'); setShowForm(false); }}
                >
                    Shipments
                </button>
                <button
                    className={`dp-tab-btn ${tab === 'inventory' ? 'active' : ''}`}
                    onClick={() => { setTab('inventory'); setShowForm(false); }}
                >
                    Inventory
                </button>
                <button
                    className="dp-new-btn"
                    onClick={() => setShowForm(!showForm)}
                >
                    {showForm ? 'Cancel' : `+ New ${tab === 'shipments' ? 'Shipment' : 'Inventory Item'}`}
                </button>
            </div>

            {showForm && tab === 'shipments' && (
                <form onSubmit={handleShipSubmit} className="dp-form">
                    <input placeholder="Distributor ID" value={shipForm.distributor} onChange={e => setShipForm({...shipForm, distributor: e.target.value})} required />
                    <input placeholder="Batch ID" value={shipForm.batch_id} onChange={e => setShipForm({...shipForm, batch_id: e.target.value})} required />
                    <input placeholder="Destination" value={shipForm.destination} onChange={e => setShipForm({...shipForm, destination: e.target.value})} required />
                    <input placeholder="Quantity (kg)" type="number" value={shipForm.quantity} onChange={e => setShipForm({...shipForm, quantity: e.target.value})} required />
                    <input placeholder="Expected Delivery" type="datetime-local" value={shipForm.expected_delivery} onChange={e => setShipForm({...shipForm, expected_delivery: e.target.value})} required />
                    <input placeholder="Tracking Number" value={shipForm.tracking_number} onChange={e => setShipForm({...shipForm, tracking_number: e.target.value})} required />
                    <input placeholder="Notes" value={shipForm.notes} onChange={e => setShipForm({...shipForm, notes: e.target.value})} className="dp-span-2" />
                    <button type="submit" className="dp-submit-btn dp-span-2">Create Shipment</button>
                </form>
            )}

            {showForm && tab === 'inventory' && (
                <form onSubmit={handleInvSubmit} className="dp-form">
                    <input placeholder="Distributor ID" value={invForm.distributor} onChange={e => setInvForm({...invForm, distributor: e.target.value})} required />
                    <input placeholder="Batch ID" value={invForm.batch_id} onChange={e => setInvForm({...invForm, batch_id: e.target.value})} required />
                    <input placeholder="Honey Type" value={invForm.honey_type} onChange={e => setInvForm({...invForm, honey_type: e.target.value})} required />
                    <input placeholder="Quantity (kg)" type="number" value={invForm.quantity} onChange={e => setInvForm({...invForm, quantity: e.target.value})} required />
                    <input placeholder="Received Date" type="datetime-local" value={invForm.received_date} onChange={e => setInvForm({...invForm, received_date: e.target.value})} required />
                    <input placeholder="Expiry Date" type="date" value={invForm.expiry_date} onChange={e => setInvForm({...invForm, expiry_date: e.target.value})} required />
                    <input placeholder="Quality Score (0-100)" type="number" value={invForm.quality_score} onChange={e => setInvForm({...invForm, quality_score: e.target.value})} />
                    <input placeholder="Storage Location" value={invForm.storage_location} onChange={e => setInvForm({...invForm, storage_location: e.target.value})} required />
                    <button type="submit" className="dp-submit-btn dp-span-2">Add Inventory</button>
                </form>
            )}

            {tab === 'shipments' && (
                shipments.length === 0 ? <p className="dp-no-data">No shipments found</p> :
                shipments.map(s => (
                    <div key={s.id} className="dp-card">
                        <strong>{s.tracking_number}</strong> - {s.batch_id} → {s.destination}
                        <div className="dp-card-meta">Qty: {s.quantity}kg | Status: {s.status}</div>
                    </div>
                ))
            )}

            {tab === 'inventory' && (
                inventory.length === 0 ? <p className="dp-no-data">No inventory found</p> :
                inventory.map(i => (
                    <div key={i.id} className="dp-card">
                        <strong>{i.batch_id}</strong> - {i.honey_type}
                        <div className="dp-card-meta">Qty: {i.quantity}kg | Location: {i.storage_location} | Status: {i.status}</div>
                    </div>
                ))
            )}
        </div>
    );
};

export default DistributorPanel;