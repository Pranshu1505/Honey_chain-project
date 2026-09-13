/**
 * Helper Functions
 * General purpose utility functions
 */

/**
 * Calculate health score based on sensor data
 * @param {object} sensorData - Sensor readings
 * @returns {number} Health score 0-100
 */
export const calculateHealthScore = (sensorData) => {
    if (!sensorData) return 0;

    let score = 100;

    // Temperature scoring
    const { temperature, humidity, weight, soundLevel } = sensorData;

    if (temperature < 15 || temperature > 35) score -= 25;
    else if (temperature < 20 || temperature > 30) score -= 10;

    if (humidity < 40 || humidity > 80) score -= 20;
    else if (humidity < 50 || humidity > 70) score -= 5;

    if (weight < 10) score -= 30;

    if (soundLevel > 80) score -= 15;

    return Math.max(0, Math.min(100, score));
};

/**
 * Format batch data for display
 * @param {object} batch - Batch data
 * @returns {object} Formatted batch object
 */
export const formatBatchData = (batch) => {
    return {
        ...batch,
        formattedDate: new Date(batch.createdAt).toLocaleDateString(),
        statusLabel: batch.status.charAt(0).toUpperCase() + batch.status.slice(1),
    };
};

/**
 * Group array of objects by property
 * @param {array} array - Array to group
 * @param {string} property - Property to group by
 * @returns {object} Grouped object
 */
export const groupBy = (array, property) => {
    return array.reduce((groups, item) => {
        const key = item[property];
        if (!groups[key]) {
            groups[key] = [];
        }
        groups[key].push(item);
        return groups;
    }, {});
};

/**
 * Sort array by multiple properties
 * @param {array} array - Array to sort
 * @param {string} property - Property to sort by
 * @param {string} order - 'asc' or 'desc'
 * @returns {array} Sorted array
 */
export const sortBy = (array, property, order = 'asc') => {
    return [...array].sort((a, b) => {
        if (a[property] < b[property]) return order === 'asc' ? -1 : 1;
        if (a[property] > b[property]) return order === 'asc' ? 1 : -1;
        return 0;
    });
};

/**
 * Debounce function
 * @param {function} func - Function to debounce
 * @param {number} delay - Delay in milliseconds
 * @returns {function} Debounced function
 */
export const debounce = (func, delay = 300) => {
    let timeoutId;
    return (...args) => {
        clearTimeout(timeoutId);
        timeoutId = setTimeout(() => func(...args), delay);
    };
};

/**
 * Throttle function
 * @param {function} func - Function to throttle
 * @param {number} limit - Time limit in milliseconds
 * @returns {function} Throttled function
 */
export const throttle = (func, limit = 300) => {
    let lastCall = 0;
    return (...args) => {
        const now = Date.now();
        if (now - lastCall >= limit) {
            lastCall = now;
            func(...args);
        }
    };
};

/**
 * Generate unique ID
 * @returns {string} Unique ID
 */
export const generateId = () => {
    return `${Date.now()}-${Math.random().toString(36).substr(2, 9)}`;
};

/**
 * Deep clone object
 * @param {object} obj - Object to clone
 * @returns {object} Cloned object
 */
export const deepClone = (obj) => {
    return JSON.parse(JSON.stringify(obj));
};

/**
 * Merge objects deeply
 * @param {object} target - Target object
 * @param {object} source - Source object
 * @returns {object} Merged object
 */
export const deepMerge = (target, source) => {
    const output = Object.assign({}, target);
    if (isObject(target) && isObject(source)) {
        Object.keys(source).forEach((key) => {
            if (isObject(source[key])) {
                if (!(key in target)) {
                    Object.assign(output, { [key]: source[key] });
                } else {
                    output[key] = deepMerge(target[key], source[key]);
                }
            } else {
                Object.assign(output, { [key]: source[key] });
            }
        });
    }
    return output;
};

/**
 * Check if value is object
 * @param {*} item - Item to check
 * @returns {boolean} Whether item is object
 */
export const isObject = (item) => {
    return item && typeof item === 'object' && !Array.isArray(item);
};

/**
 * Check if array is empty
 * @param {array} arr - Array to check
 * @returns {boolean} Whether array is empty
 */
export const isEmpty = (arr) => {
    return Array.isArray(arr) && arr.length === 0;
};
