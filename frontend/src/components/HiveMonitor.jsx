import React, { useState, useEffect } from 'react';
import './HiveMonitor.css';

const HiveMonitor = ({ token }) => {
    const [hives, setHives] = useState([]);
    const [selectedHive, setSelectedHive] = useState(null);
    const [sensors, setSensors] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        fetchHives();
    }, [token]);

    const fetchHives = async () => {
        try {
            const response = await fetch('http://localhost:8000/api/hive/', {
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
            const response = await fetch(`http://localhost:8000/api/sensor/?hive=${hiveId}`, {
                headers: { 'Authorization': `Token ${token}` }
            });
            const data = await response.json();
            setSensors(Array.isArray(data) ? data : (data.results ?? []));
            setSelectedHive(hiveId);
        } catch (error) {
            console.error('Error fetching sensor data:', error);
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
            <h1>🐝 Hive Monitor</h1>

            <div className="hives-grid">
                {hives.length === 0 ? (
                    <p className="no-data">No hives found</p>
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
                                <p><strong>Population:</strong> {hive.population}</p>
                                <p><strong>Frames:</strong> {hive.honey_frames}</p>
                            </div>
                        </div>
                    ))
                )}
            </div>

            {selectedHive && (
                <div className="sensor-data">
                    <h2>Sensor Data for Hive #{selectedHive}</h2>

                    {sensors.length === 0 ? (
                        <p className="no-data">No sensor data available</p>
                    ) : (
                        <div className="sensors-grid">
                            {sensors.map(sensor => (
                                <div key={sensor.id} className="sensor-card">
                                    <div className="sensor-type">{sensor.sensor_type.toUpperCase()}</div>
                                    <div className="sensor-value">
                                        {sensor.value} {sensor.unit}
                                    </div>
                                    <div className="sensor-timestamp">
                                        {new Date(sensor.timestamp).toLocaleString()}
                                    </div>
                                </div>
                            ))}
                        </div>
                    )}
                </div>
            )}
        </div>
    );
};

export default HiveMonitor;
