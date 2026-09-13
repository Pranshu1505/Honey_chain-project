import { render, screen, fireEvent } from '@testing-library/react';
import '@testing-library/jest-dom';
import Login from './Login';

describe('Login Component Tests', () => {
    test('renders login form', () => {
        const mockLoginSuccess = jest.fn();
        render(<Login onLoginSuccess={mockLoginSuccess} />);

        expect(screen.getByText('Honey Chain')).toBeInTheDocument();
        expect(screen.getByText('Blockchain-Based Honey Traceability')).toBeInTheDocument();
    });

    test('displays default credentials', () => {
        const mockLoginSuccess = jest.fn();
        render(<Login onLoginSuccess={mockLoginSuccess} />);

        const usernameInput = screen.getByPlaceholderText('admin');
        const passwordInput = screen.getByPlaceholderText('admin123');

        expect(usernameInput).toHaveValue('admin');
        expect(passwordInput).toHaveValue('admin123');
    });

    test('updates input values on change', () => {
        const mockLoginSuccess = jest.fn();
        render(<Login onLoginSuccess={mockLoginSuccess} />);

        const usernameInput = screen.getByPlaceholderText('admin');

        fireEvent.change(usernameInput, { target: { value: 'testuser' } });
        expect(usernameInput).toHaveValue('testuser');
    });

    test('shows loading state during login', async () => {
        const mockLoginSuccess = jest.fn();
        render(<Login onLoginSuccess={mockLoginSuccess} />);

        const loginButton = screen.getByRole('button', { name: /login/i });
        fireEvent.click(loginButton);

        expect(screen.getByRole('button', { name: /logging in/i })).toBeInTheDocument();
    });

    test('displays demo credentials', () => {
        const mockLoginSuccess = jest.fn();
        render(<Login onLoginSuccess={mockLoginSuccess} />);

        expect(screen.getByText('Demo Credentials:')).toBeInTheDocument();
        expect(screen.getByText('Username: admin')).toBeInTheDocument();
        expect(screen.getByText('Password: admin123')).toBeInTheDocument();
    });
});
