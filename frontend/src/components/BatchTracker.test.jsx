import { render, screen, waitFor } from '@testing-library/react';
import '@testing-library/jest-dom';
import BatchTracker from './BatchTracker';

describe('BatchTracker Component Tests', () => {
    const mockToken = 'test_token_123';

    beforeEach(() => {
        global.fetch = jest.fn();
    });

    afterEach(() => {
        jest.clearAllMocks();
    });

    test('renders batch tracker title', async () => {
        global.fetch.mockResolvedValue({
            json: async () => []
        });

        render(<BatchTracker token={mockToken} />);

        await waitFor(() => {
            expect(screen.getByText('📦 Batch Tracker')).toBeInTheDocument();
        });
    });

    test('displays batch items', async () => {
        const mockBatches = [
            {
                id: 1,
                batch_id: 'BATCH-2024-001',
                honey_type: 'Multifloral',
                total_quantity: 50,
                status: 'created',
                created_at: '2024-01-01'
            }
        ];

        global.fetch.mockResolvedValue({
            json: async () => mockBatches
        });

        render(<BatchTracker token={mockToken} />);

        await waitFor(() => {
            expect(screen.getByText('BATCH-2024-001')).toBeInTheDocument();
        });
    });

    test('shows correct batch status', async () => {
        const mockBatches = [
            {
                id: 1,
                batch_id: 'BATCH-2024-001',
                honey_type: 'Multifloral',
                total_quantity: 50,
                status: 'processing',
                created_at: '2024-01-01'
            }
        ];

        global.fetch.mockResolvedValue({
            json: async () => mockBatches
        });

        render(<BatchTracker token={mockToken} />);

        await waitFor(() => {
            expect(screen.getByText('PROCESSING')).toBeInTheDocument();
        });
    });

    test('handles no batches found', async () => {
        global.fetch.mockResolvedValue({
            json: async () => []
        });

        render(<BatchTracker token={mockToken} />);

        await waitFor(() => {
            expect(screen.getByText('No batches found')).toBeInTheDocument();
        });
    });
});
