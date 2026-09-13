import { useState, useCallback } from 'react';

/**
 * useForm Hook
 * Simplifies form state management and validation
 */
const useForm = (initialValues, onSubmit) => {
    const [values, setValues] = useState(initialValues);
    const [errors, setErrors] = useState({});
    const [touched, setTouched] = useState({});
    const [loading, setLoading] = useState(false);

    const handleChange = useCallback((e) => {
        const { name, value, type, checked } = e.target;
        setValues((prev) => ({
            ...prev,
            [name]: type === 'checkbox' ? checked : value,
        }));
    }, []);

    const handleBlur = useCallback((e) => {
        const { name } = e.target;
        setTouched((prev) => ({
            ...prev,
            [name]: true,
        }));
    }, []);

    const handleSubmit = useCallback(
        async (e) => {
            e.preventDefault();
            setLoading(true);
            try {
                await onSubmit(values);
            } catch (err) {
                setErrors({ submit: err.message });
            } finally {
                setLoading(false);
            }
        },
        [values, onSubmit]
    );

    const resetForm = useCallback(() => {
        setValues(initialValues);
        setErrors({});
        setTouched({});
    }, [initialValues]);

    return {
        values,
        errors,
        touched,
        loading,
        handleChange,
        handleBlur,
        handleSubmit,
        setValues,
        setErrors,
        resetForm,
    };
};

export default useForm;
