#!/bin/bash

# Define colors
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${GREEN}Starting setup for python-hacking-scripts...${NC}"

# Check for Python 3
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}Error: Python 3 is not installed.${NC}"
    echo "Please install Python 3 (e.g., 'pkg install python' on Termux or 'sudo apt install python3' on Linux)."
    exit 1
fi

# Check for pip3
if ! command -v pip3 &> /dev/null; then
    echo -e "${RED}Error: pip3 is not installed.${NC}"
    echo "Please install pip3 (e.g., 'pkg install python-pip' on Termux or 'sudo apt install python3-pip' on Linux)."
    exit 1
fi

# Create a virtual environment
echo -e "${GREEN}Creating virtual environment...${NC}"
python3 -m venv venv

# Activate the virtual environment
if [ -f "venv/bin/activate" ]; then
    source venv/bin/activate
    echo -e "${GREEN}Virtual environment activated.${NC}"
else
    echo -e "${RED}Error: Failed to create or activate virtual environment.${NC}"
    exit 1
fi

# Install dependencies
echo -e "${GREEN}Installing dependencies from requirements.txt...${NC}"
pip3 install -r requirements.txt

if [ $? -eq 0 ]; then
    echo -e "${GREEN}Dependencies installed successfully.${NC}"
else
    echo -e "${RED}Error: Failed to install dependencies.${NC}"
    exit 1
fi

echo -e "${GREEN}Setup complete!${NC}"
echo "To start using the tools, activate the virtual environment with: source venv/bin/activate"
echo "Then run a tool, e.g., python3 tools/scanner.py --help"
