#!/bin/bash
# Resume Generator Web Server Startup Script

echo "====================================="
echo "Resume Generator - Web Interface"
echo "====================================="
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed or not in PATH"
    exit 1
fi

# Check if pip is installed
if ! command -v pip3 &> /dev/null; then
    echo "Error: pip3 is not installed or not in PATH"
    exit 1
fi

# Check if requirements are installed
echo "Checking dependencies..."
pip3 install -q -r requirements.txt

echo ""
echo "Starting Resume Generator Web Server..."
echo ""
echo "🚀 Web Interface: http://localhost:5000"
echo "📝 Create Resume: http://localhost:5000/create"
echo "📊 Dashboard: http://localhost:5000/dashboard"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

# Start the Flask app
python3 app.py
