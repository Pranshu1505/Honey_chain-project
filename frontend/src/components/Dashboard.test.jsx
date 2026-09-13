import { render, screen, waitFor } from '@testing-library/react';
import '@testing-library/jest-dom';
import Dashboard from './Dashboard';

describe('Dashboard Component Tests', () => {
    const mockToken = 'test_token_123';

    beforeEach(() => {
        global.fetch = jest.fn();
    });

    afterEach(() => {
        jest.clearAllMocks();
    });

    test('renders dashboard title', () => {
        global.fetch.mockResolvedValue({
            json: async () => []
        });

        render(<Dashboard token={mockToken} />);

        expect(screen.getByText('Dashboard')).toBeInTheDocument();
    });

    test('displays stat cards', async () => {
        global.fetch.mockResolvedValue({
            json: async () => []
        });

        render(<Dashboard token={mockToken} />);

        await waitFor(() => {
            expect(screen.getByText('Beekeepers')).toBeInTheDocument();
            expect(screen.getByText('Hives')).toBeInTheDocument();
            expect(screen.getByText('Sensor Readings')).toBeInTheDocument();
            expect(screen.getByText('Batches')).toBeInTheDocument();
        });
    });

    test('fetches data from API', async () => {
        global.fetch.mockResolvedValue({
            json: async () => [{ id: 1 }]
        });

        render(<Dashboard token={mockToken} />);

        await waitFor(() => {
            expect(global.fetch).toHaveBeenCalled();
        });
    });

    test('displays welcome message', async () => {
        global.fetch.mockResolvedValue({
            json: async () => []
        });

        render(<Dashboard token={mockToken} />);

        await waitFor(() => {
            expect(screen.getByText('Welcome to Honey Chain!')).toBeInTheDocument();
        });
    });

    test('handles API errors gracefully', async () => {
        global.fetch.mockRejectedValue(new Error('API Error'));

        render(<Dashboard token={mockToken} />);

        await waitFor(() => {
            expect(screen.getByText('Dashboard')).toBeInTheDocument();
        });
    });
});
