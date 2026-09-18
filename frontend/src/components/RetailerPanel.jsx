import React, { useState, useEffect } from 'react';

const API_BASE = 'https://honey-chain-project-backend.onrender.com';

const RetailerPanel = ({ token }) => {
    const [tab, setTab] = useState('products');
    const [products, setProducts] = useState([]);
    const [sales, setSales] = useState([]);
    const [loading, setLoading] = useState(true);
    const [showForm, setShowForm] = useState(false);
    const [prodForm, setProdForm] = useState({
        retailer: '', name: '', batch_id: '', honey_type: '', price: '',
        quantity_available: '', unit: 'kg', description: '', quality_score: '', certification: ''
    });
    const [saleForm, setSaleForm] = useState({
        product: '', quantity: '', total_amount: '', customer_name: '',
        customer_phone: '', customer_email: '', payment_method: 'cash', notes: ''
    });

    const headers = { 'Authorization': `Token ${token}`, 'Content-Type': 'application/json' };

    useEffect(() => {
        fetchData();
    }, [token]);

    const fetchData = async () => {
        setLoading(true);
        try {
            const [prodRes, saleRes] = await Promise.all([
                fetch(`/api/retailer/products/`, { headers }),
                fetch(`/api/retailer/sales/`, { headers })
            ]);
            const prodData = await prodRes.json();
            const saleData = await saleRes.json();
            setProducts(Array.isArray(prodData) ? prodData : (prodData.results ?? []));
            setSales(Array.isArray(saleData) ? saleData : (saleData.results ?? []));
        } catch (err) {
            console.error('Error fetching retailer data:', err);
        } finally {
            setLoading(false);
        }
    };

    const handleProdSubmit = async (e) => {
        e.preventDefault();
        try {
            const res = await fetch(`/api/retailer/products/`, {
                method: 'POST',
                headers,
                body: JSON.stringify({
                    ...prodForm,
                    retailer: parseInt(prodForm.retailer),
                    price: parseFloat(prodForm.price),
                    quantity_available: parseFloat(prodForm.quantity_available),
                    quality_score: parseInt(prodForm.quality_score) || 0
                })
            });
            if (res.ok) {
                setShowForm(false);
                fetchData();
                alert('Product added!');
            } else {
                const err = await res.json();
                alert('Error: ' + JSON.stringify(err));
            }
        } catch (err) {
            alert('Error adding product');
        }
    };

    const handleSaleSubmit = async (e) => {
        e.preventDefault();
        try {
            const res = await fetch(`/api/retailer/sales/`, {
                method: 'POST',
                headers,
                body: JSON.stringify({
                    ...saleForm,
                    product: parseInt(saleForm.product),
                    quantity: parseFloat(saleForm.quantity),
                    total_amount: parseFloat(saleForm.total_amount)
                })
            });
            if (res.ok) {
                setShowForm(false);
                fetchData();
                alert('Sale recorded!');
            } else {
                const err = await res.json();
                alert('Error: ' + JSON.stringify(err));
            }
        } catch (err) {
            alert('Error recording sale');
        }
    };

    if (loading) return <div style={{ padding: '20px' }}>Loading...</div>;

    return (
        <div style={{ padding: '20px' }}>
            <h1>�' Retailer Panel</h1>

            <div style={{ display: 'flex', gap: '10px', marginBottom: '20px' }}>
                <button onClick={() => { setTab('products'); setShowForm(false); }}
                    style={{ padding: '10px 20px', background: tab === 'products' ? '#667eea' : '#e2e8f0', color: tab === 'products' ? 'white' : '#333', border: 'none', borderRadius: '6px', cursor: 'pointer' }}>
                    Products
                </button>
                <button onClick={() => { setTab('sales'); setShowForm(false); }}
                    style={{ padding: '10px 20px', background: tab === 'sales' ? '#667eea' : '#e2e8f0', color: tab === 'sales' ? 'white' : '#333', border: 'none', borderRadius: '6px', cursor: 'pointer' }}>
                    Sales
                </button>
                <button onClick={() => setShowForm(!showForm)}
                    style={{ padding: '10px 20px', background: '#48bb78', color: 'white', border: 'none', borderRadius: '6px', cursor: 'pointer', marginLeft: 'auto' }}>
                    {showForm ? 'Cancel' : `+ New ${tab === 'products' ? 'Product' : 'Sale'}`}
                </button>
            </div>

            {showForm && tab === 'products' && (
                <form onSubmit={handleProdSubmit} style={{ background: '#f7fafc', padding: '20px', borderRadius: '10px', marginBottom: '20px', display: 'grid', gridTemplateColumns: 'repeat(2, 1fr)', gap: '12px' }}>
                    <input placeholder="Retailer ID" value={prodForm.retailer} onChange={e => setProdForm({...prodForm, retailer: e.target.value})} required style={{ padding: '8px' }} />
                    <input placeholder="Product Name" value={prodForm.name} onChange={e => setProdForm({...prodForm, name: e.target.value})} required style={{ padding: '8px' }} />
                    <input placeholder="Batch ID" value={prodForm.batch_id} onChange={e => setProdForm({...prodForm, batch_id: e.target.value})} required style={{ padding: '8px' }} />
                    <input placeholder="Honey Type" value={prodForm.honey_type} onChange={e => setProdForm({...prodForm, honey_type: e.target.value})} required style={{ padding: '8px' }} />
                    <input placeholder="Price" type="number" step="0.01" value={prodForm.price} onChange={e => setProdForm({...prodForm, price: e.target.value})} required style={{ padding: '8px' }} />
                    <input placeholder="Quantity Available (kg)" type="number" value={prodForm.quantity_available} onChange={e => setProdForm({...prodForm, quantity_available: e.target.value})} required style={{ padding: '8px' }} />
                    <input placeholder="Quality Score (0-100)" type="number" value={prodForm.quality_score} onChange={e => setProdForm({...prodForm, quality_score: e.target.value})} style={{ padding: '8px' }} />
                    <input placeholder="Certification" value={prodForm.certification} onChange={e => setProdForm({...prodForm, certification: e.target.value})} style={{ padding: '8px' }} />
                    <input placeholder="Description" value={prodForm.description} onChange={e => setProdForm({...prodForm, description: e.target.value})} style={{ padding: '8px', gridColumn: 'span 2' }} />
                    <button type="submit" style={{ padding: '10px', background: '#667eea', color: 'white', border: 'none', borderRadius: '6px', gridColumn: 'span 2' }}>Add Product</button>
                </form>
            )}

            {showForm && tab === 'sales' && (
                <form onSubmit={handleSaleSubmit} style={{ background: '#f7fafc', padding: '20px', borderRadius: '10px', marginBottom: '20px', display: 'grid', gridTemplateColumns: 'repeat(2, 1fr)', gap: '12px' }}>
                    <input placeholder="Product ID" value={saleForm.product} onChange={e => setSaleForm({...saleForm, product: e.target.value})} required style={{ padding: '8px' }} />
                    <input placeholder="Quantity (kg)" type="number" value={saleForm.quantity} onChange={e => setSaleForm({...saleForm, quantity: e.target.value})} required style={{ padding: '8px' }} />
                    <input placeholder="Total Amount" type="number" step="0.01" value={saleForm.total_amount} onChange={e => setSaleForm({...saleForm, total_amount: e.target.value})} required style={{ padding: '8px' }} />
                    <input placeholder="Customer Name" value={saleForm.customer_name} onChange={e => setSaleForm({...saleForm, customer_name: e.target.value})} required style={{ padding: '8px' }} />
                    <input placeholder="Customer Phone" value={saleForm.customer_phone} onChange={e => setSaleForm({...saleForm, customer_phone: e.target.value})} style={{ padding: '8px' }} />
                    <input placeholder="Customer Email" value={saleForm.customer_email} onChange={e => setSaleForm({...saleForm, customer_email: e.target.value})} style={{ padding: '8px' }} />
                    <select value={saleForm.payment_method} onChange={e => setSaleForm({...saleForm, payment_method: e.target.value})} style={{ padding: '8px' }}>
                        <option value="cash">Cash</option>
                        <option value="card">Card</option>
                        <option value="online">Online</option>
                    </select>
                    <input placeholder="Notes" value={saleForm.notes} onChange={e => setSaleForm({...saleForm, notes: e.target.value})} style={{ padding: '8px' }} />
                    <button type="submit" style={{ padding: '10px', background: '#667eea', color: 'white', border: 'none', borderRadius: '6px', gridColumn: 'span 2' }}>Record Sale</button>
                </form>
            )}

            {tab === 'products' && (
                products.length === 0 ? <p style={{ color: '#888' }}>No products found</p> :
                products.map(p => (
                    <div key={p.id} style={{ background: 'white', border: '1px solid #eee', borderRadius: '8px', padding: '16px', marginBottom: '10px' }}>
                        <strong>{p.name}</strong> - {p.honey_type}
                        <div style={{ color: '#666', fontSize: '14px' }}>Price: ₹{p.price} | Qty: {p.quantity_available}{p.unit} | {p.is_available ? 'Available' : 'Out of Stock'}</div>
                    </div>
                ))
            )}

            {tab === 'sales' && (
                sales.length === 0 ? <p style={{ color: '#888' }}>No sales found</p> :
                sales.map(s => (
                    <div key={s.id} style={{ background: 'white', border: '1px solid #eee', borderRadius: '8px', padding: '16px', marginBottom: '10px' }}>
                        <strong>{s.customer_name}</strong> - ₹{s.total_amount}
                        <div style={{ color: '#666', fontSize: '14px' }}>Qty: {s.quantity}kg | Status: {s.status} | Payment: {s.payment_method}</div>
                    </div>
                ))
            )}
        </div>
    );
};

export default RetailerPanel;
