import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import '@testing-library/jest-dom';
import QualityTester from './QualityTester';

describe('QualityTester Component Tests', () => {
    const mockToken = 'test_token_123';

    beforeEach(() => {
        global.fetch = jest.fn();
    });

    afterEach(() => {
        jest.clearAllMocks();
    });

    test('renders quality tester title', async () => {
        global.fetch.mockResolvedValue({
            json: async () => []
        });

        render(<QualityTester token={mockToken} />);

        await waitFor(() => {
            expect(screen.getByText('✅ Quality Testing')).toBeInTheDocument();
        });
    });

    test('displays new test button', async () => {
        global.fetch.mockResolvedValue({
            json: async () => []
        });

        render(<QualityTester token={mockToken} />);

        const newTestButton = await screen.findByText('New Test');
        expect(newTestButton).toBeInTheDocument();
    });

    test('shows quality test form when button clicked', async () => {
        global.fetch.mockResolvedValue({
            json: async () => []
        });

        render(<QualityTester token={mockToken} />);

        const newTestButton = await screen.findByText('New Test');
        fireEvent.click(newTestButton);

        expect(screen.getByText('Record Test')).toBeInTheDocument();
    });

    test('displays quality tests from API', async () => {
        const mockTests = [
            {
                id: 1,
                batch: 1,
                acidity: 3.5,
                moisture: 17.2,
                color_intensity: 95,
                aroma_grade: 'excellent',
                is_approved: true
            }
        ];

        global.fetch.mockResolvedValue({
            json: async () => mockTests
        });

        render(<QualityTester token={mockToken} />);

        await waitFor(() => {
            expect(screen.getByText('Batch #1')).toBeInTheDocument();
        });
    });

    test('shows approval badge for approved tests', async () => {
        const mockTests = [
            {
                id: 1,
                batch: 1,
                acidity: 3.5,
                moisture: 17.2,
                color_intensity: 95,
                aroma_grade: 'excellent',
                is_approved: true
            }
        ];

        global.fetch.mockResolvedValue({
            json: async () => mockTests
        });

        render(<QualityTester token={mockToken} />);

        await waitFor(() => {
            expect(screen.getByText('✅ Approved')).toBeInTheDocument();
        });
    });
});
