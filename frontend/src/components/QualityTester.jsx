import React, { useState, useEffect } from 'react';
import './QualityTester.css';

const QualityTester = ({ token }) => {
    const [tests, setTests] = useState([]);
    const [batches, setBatches] = useState([]);
    const [showForm, setShowForm] = useState(false);
    const [formData, setFormData] = useState({
        batch: '',
        acidity: '',
        moisture: '',
        color_intensity: '',
        aroma_grade: '',
        is_approved: false
    });
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        fetchData();
    }, [token]);

    const fetchData = async () => {
        try {
            const [testsRes, batchesRes] = await Promise.all([
                fetch('http://192.168.1.11:8000/api/processing/quality-test/', {
                    headers: { 'Authorization': `Token ${token}` }
                }),
                fetch('http://192.168.1.11:8000/api/batch/', {
                    headers: { 'Authorization': `Token ${token}` }
                })
            ]);

            const testsData = await testsRes.json();
            const batchesData = await batchesRes.json();

            setTests(Array.isArray(testsData) ? testsData : (testsData.results ?? []));
            setBatches(Array.isArray(batchesData) ? batchesData : (batchesData.results ?? []));
        } catch (error) {
            console.error('Error fetching data:', error);
        } finally {
            setLoading(false);
        }
    };

    const handleSubmit = async (e) => {
        e.preventDefault();

        try {
            const response = await fetch('http://192.168.1.11:8000/api/processing/quality-test/', {
                method: 'POST',
                headers: {
                    'Authorization': `Token ${token}`,
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    ...formData,
                    acidity: parseFloat(formData.acidity),
                    moisture: parseFloat(formData.moisture),
                    color_intensity: parseInt(formData.color_intensity)
                })
            });

            if (response.ok) {
                setFormData({
                    batch: '',
                    acidity: '',
                    moisture: '',
                    color_intensity: '',
                    aroma_grade: '',
                    is_approved: false
                });
                setShowForm(false);
                fetchData();
                alert('Quality test recorded successfully!');
            }
        } catch (error) {
            console.error('Error creating test:', error);
            alert('Error recording quality test');
        }
    };

    if (loading) {
        return <div className="loading">Loading quality tests...</div>;
    }

    return (
        <div className="quality-tester">
            <div className="header">
                <h1>✅ Quality Testing</h1>
                <button
                    className="btn-primary"
                    onClick={() => setShowForm(!showForm)}
                >
                    {showForm ? 'Cancel' : 'New Test'}
                </button>
            </div>

            {showForm && (
                <form className="quality-form" onSubmit={handleSubmit}>
                    <div className="form-group">
                        <label>Batch</label>
                        <select
                            value={formData.batch}
                            onChange={(e) => setFormData({ ...formData, batch: e.target.value })}
                            required
                        >
                            <option value="">Select Batch</option>
                            {batches.map(batch => (
                                <option key={batch.id} value={batch.id}>
                                    {batch.batch_id}
                                </option>
                            ))}
                        </select>
                    </div>

                    <div className="form-group">
                        <label>Acidity (pH)</label>
                        <input
                            type="number"
                            step="0.1"
                            value={formData.acidity}
                            onChange={(e) => setFormData({ ...formData, acidity: e.target.value })}
                            required
                        />
                    </div>

                    <div className="form-group">
                        <label>Moisture (%)</label>
                        <input
                            type="number"
                            step="0.1"
                            value={formData.moisture}
                            onChange={(e) => setFormData({ ...formData, moisture: e.target.value })}
                            required
                        />
                    </div>

                    <div className="form-group">
                        <label>Color Intensity</label>
                        <input
                            type="number"
                            min="0"
                            max="100"
                            value={formData.color_intensity}
                            onChange={(e) => setFormData({ ...formData, color_intensity: e.target.value })}
                            required
                        />
                    </div>

                    <div className="form-group">
                        <label>Aroma Grade</label>
                        <select
                            value={formData.aroma_grade}
                            onChange={(e) => setFormData({ ...formData, aroma_grade: e.target.value })}
                            required
                        >
                            <option value="">Select Grade</option>
                            <option value="excellent">Excellent</option>
                            <option value="good">Good</option>
                            <option value="acceptable">Acceptable</option>
                            <option value="poor">Poor</option>
                        </select>
                    </div>

                    <div className="form-group checkbox">
                        <label>
                            <input
                                type="checkbox"
                                checked={formData.is_approved}
                                onChange={(e) => setFormData({ ...formData, is_approved: e.target.checked })}
                            />
                            Approve Quality Test
                        </label>
                    </div>

                    <button type="submit" className="btn-primary">Record Test</button>
                </form>
            )}

            <div className="tests-list">
                {tests.length === 0 ? (
                    <p className="no-data">No quality tests found</p>
                ) : (
                    tests.map(test => (
                        <div key={test.id} className="test-card">
                            <div className="card-header">
                                <h3>Batch #{test.batch}</h3>
                                <span className={`approval-badge ${test.is_approved ? 'approved' : 'pending'}`}>
                                    {test.is_approved ? '✅ Approved' : '⏳ Pending'}
                                </span>
                            </div>
                            <div className="card-body">
                                <p><strong>Acidity:</strong> {test.acidity} pH</p>
                                <p><strong>Moisture:</strong> {test.moisture}%</p>
                                <p><strong>Color:</strong> {test.color_intensity}/100</p>
                                <p><strong>Aroma:</strong> {test.aroma_grade}</p>
                            </div>
                        </div>
                    ))
                )}
            </div>
        </div>
    );
};

export default QualityTester;
