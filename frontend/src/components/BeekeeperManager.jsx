import React, { useState, useEffect } from 'react';
import './BeekeeperManager.css';

const BeekeeperManager = ({ token }) => {
    const [beekeepers, setBeekeepers] = useState([]);
    const [showForm, setShowForm] = useState(false);
    const [formData, setFormData] = useState({
        user: '',
        years_of_experience: '',
        total_hives: '',
        avg_honey_yield: '',
        certification: ''
    });
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        fetchBeekeepers();
    }, [token]);

    const fetchBeekeepers = async () => {
        try {
            const response = await fetch('https://honey-chain-project-backend.onrender.com/api/beekeeper/profile/', {
                headers: { 'Authorization': `Token ${token}` }
            });
            const data = await response.json();
            setBeekeepers(Array.isArray(data) ? data : (data.results ?? []));
        } catch (error) {
            console.error('Error fetching beekeepers:', error);
        } finally {
            setLoading(false);
        }
    };

    const handleSubmit = async (e) => {
        e.preventDefault();

        try {
            const response = await fetch('https://honey-chain-project-backend.onrender.com/api/beekeeper/profile/', {
                method: 'POST',
                headers: {
                    'Authorization': `Token ${token}`,
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(formData)
            });

            if (response.ok) {
                setFormData({
                    user: '',
                    years_of_experience: '',
                    total_hives: '',
                    avg_honey_yield: '',
                    certification: ''
                });
                setShowForm(false);
                fetchBeekeepers();
                alert('Beekeeper added successfully!');
            }
        } catch (error) {
            console.error('Error creating beekeeper:', error);
            alert('Error creating beekeeper');
        }
    };

    if (loading) {
        return <div className="loading">Loading beekeepers...</div>;
    }

    return (
        <div className="beekeeper-manager">
            <div className="header">
                <h1>🧑‍🌾 Beekeeper Management</h1>
                <button
                    className="btn-primary"
                    onClick={() => setShowForm(!showForm)}
                >
                    {showForm ? 'Cancel' : 'Add Beekeeper'}
                </button>
            </div>

            {showForm && (
                <form className="beekeeper-form" onSubmit={handleSubmit}>
                    <div className="form-group">
                        <label>User ID</label>
                        <input
                            type="number"
                            value={formData.user}
                            onChange={(e) => setFormData({ ...formData, user: e.target.value })}
                            required
                        />
                    </div>

                    <div className="form-group">
                        <label>Years of Experience</label>
                        <input
                            type="number"
                            value={formData.years_of_experience}
                            onChange={(e) => setFormData({ ...formData, years_of_experience: e.target.value })}
                            required
                        />
                    </div>

                    <div className="form-group">
                        <label>Total Hives</label>
                        <input
                            type="number"
                            value={formData.total_hives}
                            onChange={(e) => setFormData({ ...formData, total_hives: e.target.value })}
                            required
                        />
                    </div>

                    <div className="form-group">
                        <label>Average Honey Yield (kg)</label>
                        <input
                            type="number"
                            step="0.1"
                            value={formData.avg_honey_yield}
                            onChange={(e) => setFormData({ ...formData, avg_honey_yield: e.target.value })}
                            required
                        />
                    </div>

                    <div className="form-group">
                        <label>Certification</label>
                        <input
                            type="text"
                            value={formData.certification}
                            onChange={(e) => setFormData({ ...formData, certification: e.target.value })}
                            placeholder="ISO 9001, Organic, etc."
                        />
                    </div>

                    <button type="submit" className="btn-primary">Create Beekeeper</button>
                </form>
            )}

            <div className="beekeepers-list">
                {beekeepers.length === 0 ? (
                    <p className="no-data">No beekeepers found. Create one to get started!</p>
                ) : (
                    beekeepers.map(beekeeper => (
                        <div key={beekeeper.id} className="beekeeper-card">
                            <div className="card-header">
                                <h3>Beekeeper #{beekeeper.id}</h3>
                            </div>
                            <div className="card-body">
                                <p><strong>Experience:</strong> {beekeeper.years_of_experience} years</p>
                                <p><strong>Total Hives:</strong> {beekeeper.total_hives}</p>
                                <p><strong>Avg Yield:</strong> {beekeeper.avg_honey_yield} kg</p>
                                <p><strong>Certification:</strong> {beekeeper.certification || 'None'}</p>
                            </div>
                        </div>
                    ))
                )}
            </div>
        </div>
    );
};

export default BeekeeperManager;
