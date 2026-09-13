/**
 * Validator Utilities
 * Functions for validating user input
 */

/**
 * Validate email format
 * @param {string} email - Email to validate
 * @returns {boolean} Whether email is valid
 */
export const validateEmail = (email) => {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
};

/**
 * Validate password strength
 * @param {string} password - Password to validate
 * @returns {object} Validation result with details
 */
export const validatePassword = (password) => {
    const result = {
        isValid: false,
        strength: 'weak',
        errors: [],
    };

    if (password.length < 8) {
        result.errors.push('Password must be at least 8 characters');
    }
    if (!/[a-z]/.test(password)) {
        result.errors.push('Password must contain lowercase letters');
    }
    if (!/[A-Z]/.test(password)) {
        result.errors.push('Password must contain uppercase letters');
    }
    if (!/[0-9]/.test(password)) {
        result.errors.push('Password must contain numbers');
    }
    if (!/[!@#$%^&*]/.test(password)) {
        result.errors.push('Password must contain special characters');
    }

    result.isValid = result.errors.length === 0;
    if (result.isValid) {
        result.strength = 'strong';
    }

    return result;
};

/**
 * Validate phone number
 * @param {string} phone - Phone number to validate
 * @returns {boolean} Whether phone is valid
 */
export const validatePhoneNumber = (phone) => {
    const phoneRegex = /^[+]?[(]?[0-9]{3}[)]?[-\s]?[0-9]{3}[-\s]?[0-9]{4,6}$/;
    return phoneRegex.test(phone.replace(/\s/g, ''));
};

/**
 * Validate GPS coordinates
 * @param {number} latitude - Latitude value
 * @param {number} longitude - Longitude value
 * @returns {boolean} Whether coordinates are valid
 */
export const validateCoordinates = (latitude, longitude) => {
    const lat = parseFloat(latitude);
    const lon = parseFloat(longitude);
    return lat >= -90 && lat <= 90 && lon >= -180 && lon <= 180;
};

/**
 * Validate URL format
 * @param {string} url - URL to validate
 * @returns {boolean} Whether URL is valid
 */
export const validateURL = (url) => {
    try {
        new URL(url);
        return true;
    } catch (error) {
        return false;
    }
};

/**
 * Validate required field
 * @param {*} value - Value to check
 * @returns {boolean} Whether field is provided
 */
export const validateRequired = (value) => {
    return value !== null && value !== undefined && value !== '';
};

/**
 * Validate number range
 * @param {number} value - Value to check
 * @param {number} min - Minimum value
 * @param {number} max - Maximum value
 * @returns {boolean} Whether value is in range
 */
export const validateRange = (value, min, max) => {
    const num = parseFloat(value);
    return !isNaN(num) && num >= min && num <= max;
};
