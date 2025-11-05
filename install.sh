#!/bin/bash
# Exit immediately if a command exits with a non-zero status.
set -e

echo "--- [1/5] Updating system packages (apt-get) ---"
sudo apt-get update -qq

echo "--- [2/5] Installing system dependencies (espeak-ng, python3-venv) ---"
# Install espeak-ng for kokoro and python3-venv to create the virtual environment
sudo apt-get install -qq -y espeak-ng python3-venv > /dev/null 2>&1

VENV_DIR="venv"

# Check if the virtual environment directory already exists
if [ ! -d "$VENV_DIR" ]; then
    echo "--- [3/5] Creating Python virtual environment at '$VENV_DIR' ---"
    python3 -m venv $VENV_DIR
else
    echo "--- [3/5] Python virtual environment '$VENV_DIR' already exists ---"
fi

echo "--- [4/5] Activating virtual environment ---"
# Activate the virtual environment for this script's session
# Note the correct path for Windows is 'Scripts'
source "$VENV_DIR/bin/activate"

echo "--- [5/5] Upgrading pip and installing requirements from requirements.txt ---"
# Upgrade pip and install all requirements
pip install --upgrade pip > /dev/null
pip install -r requirements.txt

echo ""
echo "--- Setup Complete! ---"
echo ""
echo "You can start your server with:"
echo "  python main.py"
echo ""
