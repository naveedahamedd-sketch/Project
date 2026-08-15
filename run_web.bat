@echo off
REM Resume Generator Web Server Startup Script

echo =====================================
echo Resume Generator - Web Interface
echo =====================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    pause
    exit /b 1
)

REM Check if pip is installed
pip --version >nul 2>&1
if errorlevel 1 (
    echo Error: pip is not installed or not in PATH
    pause
    exit /b 1
)

REM Install requirements
echo Checking dependencies...
pip install -q -r requirements.txt

echo.
echo Starting Resume Generator Web Server...
echo.
echo Web Interface: http://localhost:5000
echo Create Resume: http://localhost:5000/create
echo Dashboard: http://localhost:5000/dashboard
echo.
echo Press Ctrl+C to stop the server
echo.

REM Start the Flask app
python app.py

pause
