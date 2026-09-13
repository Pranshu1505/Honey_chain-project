import { render, screen, waitFor } from '@testing-library/react';
import '@testing-library/jest-dom';
import HiveMonitor from './HiveMonitor';

describe('HiveMonitor Component Tests', () => {
    const mockToken = 'test_token_123';

    beforeEach(() => {
        global.fetch = jest.fn();
    });

    afterEach(() => {
        jest.clearAllMocks();
    });

    test('renders hive monitor title', async () => {
        global.fetch.mockResolvedValue({
            json: async () => []
        });

        render(<HiveMonitor token={mockToken} />);

        await waitFor(() => {
            expect(screen.getByText('🐝 Hive Monitor')).toBeInTheDocument();
        });
    });

    test('displays hive cards', async () => {
        const mockHives = [
            {
                id: 1,
                hive_id: 'HIVE-001',
                health_status: 'healthy',
                population: 50000,
                honey_frames: 8
            }
        ];

        global.fetch.mockResolvedValue({
            json: async () => mockHives
        });

        render(<HiveMonitor token={mockToken} />);

        await waitFor(() => {
            expect(screen.getByText('HIVE-001')).toBeInTheDocument();
        });
    });

    test('displays sensor data when hive selected', async () => {
        const mockHives = [
            {
                id: 1,
                hive_id: 'HIVE-001',
                health_status: 'healthy',
                population: 50000,
                honey_frames: 8
            }
        ];

        global.fetch
            .mockResolvedValueOnce({ json: async () => mockHives })
            .mockResolvedValueOnce({
                json: async () => [
                    {
                        id: 1,
                        sensor_type: 'temperature',
                        value: 32.5,
                        unit: '°C',
                        timestamp: '2024-01-01T10:00:00Z'
                    }
                ]
            });

        render(<HiveMonitor token={mockToken} />);

        await waitFor(() => {
            expect(screen.getByText('TEMPERATURE')).toBeInTheDocument();
        });
    });

    test('shows health status correctly', async () => {
        const mockHives = [
            {
                id: 1,
                hive_id: 'HIVE-001',
                health_status: 'warning',
                population: 50000,
                honey_frames: 8
            }
        ];

        global.fetch.mockResolvedValue({
            json: async () => mockHives
        });

        render(<HiveMonitor token={mockToken} />);

        await waitFor(() => {
            expect(screen.getByText('⚠️ Warning')).toBeInTheDocument();
        });
    });
});
