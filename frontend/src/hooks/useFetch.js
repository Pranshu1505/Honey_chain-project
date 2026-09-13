import { useState, useCallback, useEffect } from 'react';

/**
 * useFetch Hook
 * Generic data fetching with loading, error, and caching states
 */
const useFetch = (fetchFn, deps = []) => {
    const [data, setData] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    const fetchData = useCallback(async () => {
        setLoading(true);
        setError(null);
        try {
            const result = await fetchFn();
            setData(result);
        } catch (err) {
            setError(err.message || 'An error occurred');
        } finally {
            setLoading(false);
        }
    }, [fetchFn]);

    useEffect(() => {
        fetchData();
    }, deps);

    const refetch = useCallback(fetchData, [fetchData]);

    return { data, loading, error, refetch };
};

export default useFetch;
