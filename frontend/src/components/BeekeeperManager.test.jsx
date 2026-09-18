import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import '@testing-library/jest-dom';
import BeekeeperManager from './BeekeeperManager';

describe('BeekeeperManager Component Tests', () => {
    const mockToken = 'test_token_123';

    beforeEach(() => {
        global.fetch = jest.fn();
    });

    afterEach(() => {
        jest.clearAllMocks();
    });

    test('renders beekeeper manager title', async () => {
        global.fetch.mockResolvedValue({
            json: async () => []
        });

        render(<BeekeeperManager token={mockToken} />);

        await waitFor(() => {
            expect(screen.getByText('🧑‍🌾 Beekeeper Management')).toBeInTheDocument();
        });
    });

    test('displays add beekeeper button', async () => {
        global.fetch.mockResolvedValue({
            json: async () => []
        });

        render(<BeekeeperManager token={mockToken} />);

        await waitFor(() => {
            expect(screen.getByText('Add Beekeeper')).toBeInTheDocument();
        });
    });

    test('shows form when add button clicked', async () => {
        global.fetch.mockResolvedValue({
            json: async () => []
        });

        render(<BeekeeperManager token={mockToken} />);

        const addButton = await screen.findByText('Add Beekeeper');
        fireEvent.click(addButton);

        expect(screen.getByText('Cancel')).toBeInTheDocument();
    });

    test('displays beekeeper list from API', async () => {
        const mockBeekeepers = [
            {
                id: 1,
                years_of_experience: 5,
                total_hives: 20,
                avg_honey_yield: 15.5,
                certification: 'ISO 9001'
            }
        ];

        global.fetch.mockResolvedValue({
            json: async () => mockBeekeepers
        });

        render(<BeekeeperManager token={mockToken} />);

        await waitFor(() => {
            expect(screen.getByText('Beekeeper #1')).toBeInTheDocument();
        });
    });

    test('handles form submission', async () => {
        global.fetch
            .mockResolvedValueOnce({ json: async () => [] })
            .mockResolvedValueOnce({ ok: true, json: async () => { } })
            .mockResolvedValueOnce({ json: async () => [] });

        render(<BeekeeperManager token={mockToken} />);

        const addButton = await screen.findByText('Add Beekeeper');
        fireEvent.click(addButton);

        const submitButton = screen.getByText('Create Beekeeper');
        fireEvent.click(submitButton);

        await waitFor(() => {
            expect(global.fetch).toHaveBeenCalledWith(
                'https://honey-chain-project-backend.onrender.com/api/beekeeper/profiles/',
                expect.objectContaining({
                    method: 'POST'
                })
            );
        });
    });
});
