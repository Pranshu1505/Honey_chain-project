/**
 * Retailer Management Service
 * Handles all retailer-related API calls
 */

import { apiCall } from './base';

const RetailerService = {
    // Retailer management
    list: () => apiCall('/retailer/'),

    get: (id) => apiCall(`/retailer/${id}/`),

    create: (data) => apiCall('/retailer/', {
        method: 'POST',
        body: JSON.stringify(data)
    }),

    update: (id, data) => apiCall(`/retailer/${id}/`, {
        method: 'PUT',
        body: JSON.stringify(data)
    }),

    // Inventory
    getInventory: (retailerId) =>
        apiCall(`/retailer/${retailerId}/inventory/`),

    getInventoryItem: (retailerId, productId) =>
        apiCall(`/retailer/${retailerId}/inventory/${productId}/`),

    updateInventory: (retailerId, productId, quantity) =>
        apiCall(`/retailer/${retailerId}/inventory/${productId}/`, {
            method: 'PUT',
            body: JSON.stringify({ quantity })
        }),

    getInventoryStatus: (retailerId) =>
        apiCall(`/retailer/${retailerId}/inventory-status/`),

    // Products
    listProducts: (retailerId) =>
        apiCall(`/retailer/${retailerId}/products/`),

    getProduct: (retailerId, productId) =>
        apiCall(`/retailer/${retailerId}/products/${productId}/`),

    createProduct: (retailerId, data) =>
        apiCall(`/retailer/${retailerId}/products/`, {
            method: 'POST',
            body: JSON.stringify(data)
        }),

    updateProduct: (retailerId, productId, data) =>
        apiCall(`/retailer/${retailerId}/products/${productId}/`, {
            method: 'PUT',
            body: JSON.stringify(data)
        }),

    deleteProduct: (retailerId, productId) =>
        apiCall(`/retailer/${retailerId}/products/${productId}/`, { method: 'DELETE' }),

    // Sales
    listSales: (retailerId) =>
        apiCall(`/retailer/${retailerId}/sales/`),

    getSale: (retailerId, saleId) =>
        apiCall(`/retailer/${retailerId}/sales/${saleId}/`),

    recordSale: (retailerId, data) =>
        apiCall(`/retailer/${retailerId}/sales/`, {
            method: 'POST',
            body: JSON.stringify(data)
        }),

    getSalesReport: (retailerId, startDate, endDate) =>
        apiCall(`/retailer/${retailerId}/sales-report/?start=${startDate}&end=${endDate}`),

    getDailySales: (retailerId, date) =>
        apiCall(`/retailer/${retailerId}/sales/daily/?date=${date}`),

    // Customer management
    listCustomers: (retailerId) =>
        apiCall(`/retailer/${retailerId}/customers/`),

    getCustomer: (retailerId, customerId) =>
        apiCall(`/retailer/${retailerId}/customers/${customerId}/`),

    getCustomerPurchaseHistory: (retailerId, customerId) =>
        apiCall(`/retailer/${retailerId}/customers/${customerId}/purchases/`),

    // Reviews and ratings
    getProductReviews: (retailerId, productId) =>
        apiCall(`/retailer/${retailerId}/products/${productId}/reviews/`),

    addProductReview: (retailerId, productId, review) =>
        apiCall(`/retailer/${retailerId}/products/${productId}/reviews/`, {
            method: 'POST',
            body: JSON.stringify(review)
        }),

    getProductRating: (retailerId, productId) =>
        apiCall(`/retailer/${retailerId}/products/${productId}/rating/`),
};

export default RetailerService;
