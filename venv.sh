#!/bin/bash

# Remove the .venv directory if it exists
rm -rf .venv

# Create a virtual environment with Python 3.10
python3.11 -m venv .venv

# Check if the virtual environment creation was successful
if [ $? -ne 0 ]; then
    exit 1
fi

# Activate the virtual environment
source .venv/bin/activate

# Check Python version
python --version

# Install required packages from requirements.txt
pip install pip-tools
pip install -r requirements.txt
