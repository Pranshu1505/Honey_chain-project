import React, { useState, useEffect } from 'react';
import './HiveMonitor.css';

const HiveMonitor = ({ token }) => {
    const [hives, setHives] = useState([]);
    const [selectedHive, setSelectedHive] = useState(null);
    const [sensors, setSensors] = useState([]);
    const [loading, setLoading] = useState(true);
    const [showForm, setShowForm] = useState(false);
    const [formData, setFormData] = useState({
        apiary: '',
        hive_id: '',
        name: '',
        hive_type: 'langstroth',
        installation_date: '',
        population: '',
        honey_frames: ''
    });

    useEffect(() => {
        fetchHives();
    }, [token]);

    const fetchHives = async () => {
        try {
            const response = await fetch('https://honey-chain-project-backend.onrender.com/api/hive/', {
                headers: { 'Authorization': `Token ${token}` }
            });
            const data = await response.json();
            setHives(Array.isArray(data) ? data : (data.results ?? []));
        } catch (error) {
            console.error('Error fetching hives:', error);
        } finally {
            setLoading(false);
        }
    };

    const fetchSensorData = async (hiveId) => {
        try {
            const response = await fetch(`https://honey-chain-project-backend.onrender.com/api/sensor/?hive=${hiveId}`, {
                headers: { 'Authorization': `Token ${token}` }
            });
            const data = await response.json();
            setSensors(Array.isArray(data) ? data : (data.results ?? []));
            setSelectedHive(hiveId);
        } catch (error) {
            console.error('Error fetching sensor data:', error);
        }
    };

    const handleSubmit = async (e) => {
        e.preventDefault();

        try {
            const response = await fetch('https://honey-chain-project-backend.onrender.com/api/hive/', {
                method: 'POST',
                headers: {
                    'Authorization': `Token ${token}`,
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    ...formData,
                    apiary: Number(formData.apiary),
                    population: formData.population ? Number(formData.population) : 0,
                    honey_frames: formData.honey_frames ? Number(formData.honey_frames) : 0
                })
            });

            if (response.ok) {
                setFormData({
                    apiary: '',
                    hive_id: '',
                    name: '',
                    hive_type: 'langstroth',
                    installation_date: '',
                    population: '',
                    honey_frames: ''
                });
                setShowForm(false);
                fetchHives();
                alert('Hive added successfully!');
            } else {
                const errorData = await response.json().catch(() => ({}));
                alert('Error creating hive: ' + JSON.stringify(errorData));
            }
        } catch (error) {
            console.error('Error creating hive:', error);
            alert('Error creating hive');
        }
    };

    const getHealthStatus = (health_status) => {
        const statusMap = {
            'healthy': '✅ Healthy',
            'warning': '⚠️ Warning',
            'critical': '🔴 Critical'
        };
        return statusMap[health_status] || health_status;
    };

    if (loading) {
        return <div className="loading">Loading hives...</div>;
    }

    return (
        <div className="hive-monitor">
            <div className="header">
                <h1>🐝 Hive Monitor</h1>
                <button
                    className="btn-primary"
                    onClick={() => setShowForm(!showForm)}
                >
                    {showForm ? 'Cancel' : 'Add Hive'}
                </button>
            </div>

            {showForm && (
                <form className="hive-form" onSubmit={handleSubmit}>
                    <div className="form-group">
                        <label>Apiary ID</label>
                        <input
                            type="number"
                            value={formData.apiary}
                            onChange={(e) => setFormData({ ...formData, apiary: e.target.value })}
                            required
                        />
                    </div>

                    <div className="form-group">
                        <label>Hive ID</label>
                        <input
                            type="text"
                            value={formData.hive_id}
                            onChange={(e) => setFormData({ ...formData, hive_id: e.target.value })}
                            placeholder="e.g. HIVE-001"
                            required
                        />
                    </div>

                    <div className="form-group">
                        <label>Name</label>
                        <input
                            type="text"
                            value={formData.name}
                            onChange={(e) => setFormData({ ...formData, name: e.target.value })}
                            required
                        />
                    </div>

                    <div className="form-group">
                        <label>Hive Type</label>
                        <select
                            value={formData.hive_type}
                            onChange={(e) => setFormData({ ...formData, hive_type: e.target.value })}
                            required
                        >
                            <option value="langstroth">Langstroth</option>
                            <option value="topbar">Top-bar</option>
                            <option value="warre">Warré</option>
                        </select>
                    </div>

                    <div className="form-group">
                        <label>Installation Date</label>
                        <input
                            type="date"
                            value={formData.installation_date}
                            onChange={(e) => setFormData({ ...formData, installation_date: e.target.value })}
                            required
                        />
                    </div>

                    <div className="form-group">
                        <label>Population (bees)</label>
                        <input
                            type="number"
                            value={formData.population}
                            onChange={(e) => setFormData({ ...formData, population: e.target.value })}
                        />
                    </div>

                    <div className="form-group">
                        <label>Honey Frames</label>
                        <input
                            type="number"
                            value={formData.honey_frames}
                            onChange={(e) => setFormData({ ...formData, honey_frames: e.target.value })}
                        />
                    </div>

                    <button type="submit" className="btn-primary">Create Hive</button>
                </form>
            )}

            <div className="hives-grid">
                {hives.length === 0 ? (
                    <p className="no-data">No hives found. Add one to get started!</p>
                ) : (
                    hives.map(hive => (
                        <div
                            key={hive.id}
                            className={`hive-card ${selectedHive === hive.id ? 'selected' : ''}`}
                            onClick={() => fetchSensorData(hive.id)}
                        >
                            <div className="hive-id">{hive.hive_id}</div>
                            <div className="hive-status">{getHealthStatus(hive.health_status)}</div>
                            <div className="hive-info">
                                <p><strong>Name:</strong> {hive.name}</p>
                                <p><strong>Type:</strong> {hive.hive_type}</p>
                                <p><strong>Population:</strong> {hive.population}</p>
                                <p><strong>Honey Frames:</strong> {hive.honey_frames}</p>
                            </div>
                        </div>
                    ))
                )}
            </div>

            {selectedHive && (
                <div className="sensor-data">
                    <h2>Sensor Readings</h2>
                    <div className="sensors-grid">
                        {sensors.length === 0 ? (
                            <p className="no-data">No sensor data found for this hive.</p>
                        ) : (
                            sensors.map(sensor => (
                                <div key={sensor.id} className="sensor-card">
                                    <div className="sensor-type">{sensor.sensor_type}</div>
                                    <div className="sensor-value">{sensor.value}</div>
                                    <div className="sensor-timestamp">{sensor.timestamp}</div>
                                </div>
                            ))
                        )}
                    </div>
                </div>
            )}
        </div>
    );
};

export default HiveMonitor;


// import React, { useState, useEffect } from 'react';
// import './HiveMonitor.css';

// const HiveMonitor = ({ token }) => {
//     const [hives, setHives] = useState([]);
//     const [selectedHive, setSelectedHive] = useState(null);
//     const [sensors, setSensors] = useState([]);
//     const [loading, setLoading] = useState(true);

//     useEffect(() => {
//         fetchHives();
//     }, [token]);

//     const fetchHives = async () => {
//         try {
//             const response = await fetch('https://honey-chain-project-backend.onrender.com/api/hive/', {
//                 headers: { 'Authorization': `Token ${token}` }
//             });
//             const data = await response.json();
//             setHives(Array.isArray(data) ? data : (data.results ?? []));
//         } catch (error) {
//             console.error('Error fetching hives:', error);
//         } finally {
//             setLoading(false);
//         }
//     };

//     const fetchSensorData = async (hiveId) => {
//         try {
//             const response = await fetch(`https://honey-chain-project-backend.onrender.com/api/sensor/?hive=${hiveId}`, {
//                 headers: { 'Authorization': `Token ${token}` }
//             });
//             const data = await response.json();
//             setSensors(Array.isArray(data) ? data : (data.results ?? []));
//             setSelectedHive(hiveId);
//         } catch (error) {
//             console.error('Error fetching sensor data:', error);
//         }
//     };

//     const getHealthStatus = (health_status) => {
//         const statusMap = {
//             'healthy': '✅ Healthy',
//             'warning': '⚠️ Warning',
//             'critical': '🔴 Critical'
//         };
//         return statusMap[health_status] || health_status;
//     };

//     if (loading) {
//         return <div className="loading">Loading hives...</div>;
//     }

//     return (
//         <div className="hive-monitor">
//             <h1>🐝 Hive Monitor</h1>

//             <div className="hives-grid">
//                 {hives.length === 0 ? (
//                     <p className="no-data">No hives found</p>
//                 ) : (
//                     hives.map(hive => (
//                         <div
//                             key={hive.id}
//                             className={`hive-card ${selectedHive === hive.id ? 'selected' : ''}`}
//                             onClick={() => fetchSensorData(hive.id)}
//                         >
//                             <div className="hive-id">{hive.hive_id}</div>
//                             <div className="hive-status">{getHealthStatus(hive.health_status)}</div>
//                             <div className="hive-info">
//                                 <p><strong>Population:</strong> {hive.population}</p>
//                                 <p><strong>Frames:</strong> {hive.honey_frames}</p>
//                             </div>
//                         </div>
//                     ))
//                 )}
//             </div>

//             {selectedHive && (
//                 <div className="sensor-data">
//                     <h2>Sensor Data for Hive #{selectedHive}</h2>

//                     {sensors.length === 0 ? (
//                         <p className="no-data">No sensor data available</p>
//                     ) : (
//                         <div className="sensors-grid">
//                             {sensors.map(sensor => (
//                                 <div key={sensor.id} className="sensor-card">
//                                     <div className="sensor-type">{sensor.sensor_type.toUpperCase()}</div>
//                                     <div className="sensor-value">
//                                         {sensor.value} {sensor.unit}
//                                     </div>
//                                     <div className="sensor-timestamp">
//                                         {new Date(sensor.timestamp).toLocaleString()}
//                                     </div>
//                                 </div>
//                             ))}
//                         </div>
//                     )}
//                 </div>
//             )}
//         </div>
//     );
// };

// export default HiveMonitor;
