#!/bin/bash

echo "Starting Fire Department Hiring Scenarios App..."
echo "=============================================="
echo ""

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed."
    exit 1
fi

# Install requirements if needed
if [ ! -d "venv" ]; then
    echo "Installing dependencies..."
    pip3 install -r requirements.txt
    echo ""
fi

# Start the Flask app
echo "Starting server on http://127.0.0.1:5000"
echo "Press Ctrl+C to stop the server"
echo ""

python3 app.py
