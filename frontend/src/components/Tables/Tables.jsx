/**
 * Tables Component
 * Reusable table component for displaying data
 */

import React from 'react';
import './Tables.css';

const Tables = ({ columns = [], data = [], striped = false }) => {
    return (
        <div className="table-container">
            <table className={`table ${striped ? 'table--striped' : ''}`}>
                <thead>
                    <tr>
                        {columns.map((col) => (
                            <th key={col.key}>{col.label}</th>
                        ))}
                    </tr>
                </thead>
                <tbody>
                    {data.map((row, idx) => (
                        <tr key={idx}>
                            {columns.map((col) => (
                                <td key={col.key}>{row[col.key]}</td>
                            ))}
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default Tables;
export { Tables };
