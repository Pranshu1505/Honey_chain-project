#!/usr/bin/env python
"""
Honey Chain - Automated Setup and Test Script
This script sets up the backend, runs migrations, and starts the server.
"""

import os
import sys
import subprocess
import platform

def print_header(title):
    """Print a formatted header"""
    print("\n" + "="*60)
    print(f"  {title}")
    print("="*60)

def run_command(cmd, description):
    """Run a command and report results"""
    print(f"\n▶ {description}...")
    try:
        result = subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} - SUCCESS")
        if result.stdout:
            print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} - FAILED")
        print(f"Error: {e.stderr}")
        return False
    except Exception as e:
        print(f"❌ {description} - ERROR: {str(e)}")
        return False

def setup_backend():
    """Setup backend environment"""
    print_header("BACKEND SETUP")
    
    # Check Python version
    if not run_command(f"{sys.executable} --version", "Checking Python version"):
        return False
    
    # Create virtual environment
    venv_path = os.path.join(os.getcwd(), 'venv')
    if not os.path.exists(venv_path):
        if not run_command(f"{sys.executable} -m venv venv", "Creating virtual environment"):
            return False
    else:
        print("✅ Virtual environment already exists")
    
    # Get pip executable
    if platform.system() == "Windows":
        pip_cmd = os.path.join(venv_path, 'Scripts', 'pip')
        activate_cmd = os.path.join(venv_path, 'Scripts', 'activate.bat')
    else:
        pip_cmd = os.path.join(venv_path, 'bin', 'pip')
        activate_cmd = os.path.join(venv_path, 'bin', 'activate')
    
    # Install dependencies
    if not run_command(f"{pip_cmd} install -r requirements.txt", "Installing dependencies"):
        return False
    
    # Run migrations
    python_cmd = os.path.join(venv_path, 'Scripts' if platform.system() == "Windows" else 'bin', 'python')
    if not run_command(f"{python_cmd} manage.py migrate", "Running database migrations"):
        return False
    
    return True

def start_backend():
    """Start Django development server"""
    print_header("STARTING BACKEND")
    
    venv_path = os.path.join(os.getcwd(), 'venv')
    python_cmd = os.path.join(venv_path, 'Scripts' if platform.system() == "Windows" else 'bin', 'python')
    
    print(f"\n▶ Starting Django development server on http://localhost:8000/")
    print("Press Ctrl+C to stop the server\n")
    
    try:
        subprocess.run(f"{python_cmd} manage.py runserver", shell=True)
    except KeyboardInterrupt:
        print("\n\nServer stopped")
    except Exception as e:
        print(f"Error starting server: {e}")

def setup_frontend():
    """Setup frontend environment"""
    print_header("FRONTEND SETUP")
    
    frontend_dir = os.path.join(os.getcwd(), 'frontend')
    if not os.path.exists(frontend_dir):
        print("❌ Frontend directory not found")
        return False
    
    os.chdir(frontend_dir)
    
    # Install npm dependencies
    if not run_command("npm install", "Installing npm dependencies"):
        return False
    
    os.chdir('..')
    return True

def start_frontend():
    """Start React development server"""
    print_header("STARTING FRONTEND")
    
    frontend_dir = os.path.join(os.getcwd(), 'frontend')
    os.chdir(frontend_dir)
    
    print(f"\n▶ Starting React development server on http://localhost:5173/")
    print("Press Ctrl+C to stop the server\n")
    
    try:
        subprocess.run("npm run dev", shell=True)
    except KeyboardInterrupt:
        print("\n\nServer stopped")
    except Exception as e:
        print(f"Error starting server: {e}")

def run_tests():
    """Run tests"""
    print_header("RUNNING TESTS")
    
    venv_path = os.path.join(os.getcwd(), 'venv')
    python_cmd = os.path.join(venv_path, 'Scripts' if platform.system() == "Windows" else 'bin', 'python')
    
    print("\n▶ Running backend tests...")
    run_command(f"{python_cmd} manage.py test", "Backend tests")
    
    frontend_dir = os.path.join(os.getcwd(), 'frontend')
    if os.path.exists(frontend_dir):
        print("\n▶ Running frontend tests...")
        os.chdir(frontend_dir)
        run_command("npm test", "Frontend tests")
        os.chdir('..')

def main():
    """Main entry point"""
    print_header("HONEY CHAIN - SETUP & TEST SCRIPT")
    
    print("""
This script will:
1. Create a Python virtual environment
2. Install all Python dependencies
3. Run database migrations
4. Optionally: Install npm packages and start servers
5. Run tests

USAGE:
  python setup_and_test.py                    # Setup only
  python setup_and_test.py --start-backend    # Setup and start backend
  python setup_and_test.py --start-frontend   # Setup and start frontend
  python setup_and_test.py --start-all        # Setup and start all
  python setup_and_test.py --test             # Setup and run tests
    """)
    
    # Parse arguments
    start_backend_flag = '--start-backend' in sys.argv
    start_frontend_flag = '--start-frontend' in sys.argv
    start_all_flag = '--start-all' in sys.argv
    run_tests_flag = '--test' in sys.argv
    
    # Setup backend
    if not setup_backend():
        print("\n❌ Backend setup failed. Please check errors above.")
        sys.exit(1)
    
    # Setup frontend if needed
    if start_frontend_flag or start_all_flag:
        if not setup_frontend():
            print("\n❌ Frontend setup failed. Please check errors above.")
            sys.exit(1)
    
    # Run tests if requested
    if run_tests_flag:
        run_tests()
        return
    
    # Start servers
    if start_backend_flag or start_all_flag:
        start_backend()
    elif start_frontend_flag:
        start_frontend()
    else:
        print_header("SETUP COMPLETE")
        print("""
✅ Backend is ready!

To start the backend server:
  cd honey_chain
  python setup_and_test.py --start-backend

To start the frontend server:
  cd honey_chain
  npm install --prefix frontend
  npm run dev --prefix frontend

To run all:
  python setup_and_test.py --start-all

To run tests:
  python setup_and_test.py --test
        """)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nSetup interrupted by user")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)
