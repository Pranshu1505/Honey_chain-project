@echo off
REM Honey Chain Automated Setup Script

echo ========================================
echo Honey Chain - Automated Setup
echo ========================================
echo.

REM Check Python version
echo [1/5] Checking Python version...
python --version
if errorlevel 1 (
    echo ERROR: Python not found. Please install Python 3.9+
    exit /b 1
)
echo.

REM Create virtual environment
echo [2/5] Creating virtual environment...
python -m venv venv
if errorlevel 1 (
    echo ERROR: Failed to create virtual environment
    exit /b 1
)
echo Virtual environment created successfully!
echo.

REM Activate virtual environment
echo [3/5] Activating virtual environment...
call venv\Scripts\activate.bat
echo Virtual environment activated!
echo.

REM Install dependencies
echo [4/5] Installing Python dependencies...
pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: Failed to install dependencies
    exit /b 1
)
echo Dependencies installed successfully!
echo.

REM Run migrations
echo [5/5] Running database migrations...
python manage.py migrate
if errorlevel 1 (
    echo ERROR: Failed to run migrations
    exit /b 1
)
echo.
echo Database migrations completed successfully!
echo.

echo ========================================
echo Setup Complete!
echo ========================================
echo.
echo To start the backend server, run:
echo   cd honey_chain
echo   venv\Scripts\activate
echo   python manage.py runserver
echo.
echo To start the frontend server, run (in another terminal):
echo   cd honey_chain\frontend
echo   npm install
echo   npm run dev
echo.
pause
