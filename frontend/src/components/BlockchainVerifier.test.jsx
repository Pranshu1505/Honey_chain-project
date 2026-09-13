import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import '@testing-library/jest-dom';
import BlockchainVerifier from './BlockchainVerifier';

describe('BlockchainVerifier Component Tests', () => {
    const mockToken = 'test_token_123';

    beforeEach(() => {
        global.fetch = jest.fn();
    });

    afterEach(() => {
        jest.clearAllMocks();
    });

    test('renders blockchain verifier title', async () => {
        global.fetch.mockResolvedValue({
            json: async () => []
        });

        render(<BlockchainVerifier token={mockToken} />);

        await waitFor(() => {
            expect(screen.getByText('⛓️ Blockchain Verification')).toBeInTheDocument();
        });
    });

    test('displays verify form with batch ID input', async () => {
        global.fetch.mockResolvedValue({
            json: async () => []
        });

        render(<BlockchainVerifier token={mockToken} />);

        const input = await screen.findByPlaceholderText('e.g., BATCH-2024-001');
        expect(input).toBeInTheDocument();
    });

    test('displays blockchain records', async () => {
        const mockRecords = [
            {
                id: 1,
                batch_id: 'BATCH-2024-001',
                origin: 'Main Apiary',
                honey_type: 'Multifloral',
                quantity: 50,
                quality_score: 90,
                transaction_hash: 'abc123',
                block_number: 12345
            }
        ];

        global.fetch.mockResolvedValue({
            json: async () => mockRecords
        });

        render(<BlockchainVerifier token={mockToken} />);

        await waitFor(() => {
            expect(screen.getByText('All Blockchain Records')).toBeInTheDocument();
        });
    });

    test('verifies batch when form submitted', async () => {
        global.fetch
            .mockResolvedValueOnce({ json: async () => [] })
            .mockResolvedValueOnce({
                json: async () => ({
                    verified: true,
                    record: {
                        batch_id: 'BATCH-2024-001',
                        origin: 'Main Apiary',
                        honey_type: 'Multifloral',
                        quantity: 50,
                        quality_score: 90,
                        transaction_hash: 'abc123',
                        block_number: 12345
                    }
                })
            });

        render(<BlockchainVerifier token={mockToken} />);

        const input = await screen.findByPlaceholderText('e.g., BATCH-2024-001');
        const verifyButton = screen.getByText('Verify Batch');

        fireEvent.change(input, { target: { value: 'BATCH-2024-001' } });
        fireEvent.click(verifyButton);

        await waitFor(() => {
            expect(screen.getByText('Batch Verified!')).toBeInTheDocument();
        });
    });

    test('shows quality score in verification', async () => {
        global.fetch
            .mockResolvedValueOnce({ json: async () => [] })
            .mockResolvedValueOnce({
                json: async () => ({
                    verified: true,
                    record: {
                        batch_id: 'BATCH-2024-001',
                        origin: 'Main Apiary',
                        honey_type: 'Multifloral',
                        quantity: 50,
                        quality_score: 90,
                        transaction_hash: 'abc123',
                        block_number: 12345
                    }
                })
            });

        render(<BlockchainVerifier token={mockToken} />);

        const input = await screen.findByPlaceholderText('e.g., BATCH-2024-001');
        const verifyButton = screen.getByText('Verify Batch');

        fireEvent.change(input, { target: { value: 'BATCH-2024-001' } });
        fireEvent.click(verifyButton);

        await waitFor(() => {
            expect(screen.getByText('90/100')).toBeInTheDocument();
        });
    });
});
