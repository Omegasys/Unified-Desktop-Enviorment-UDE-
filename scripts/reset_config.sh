#!/bin/bash

# reset_config.sh
# Script to reset UDE configuration to default

# Check if the script is being run with superuser privileges
if [ "$EUID" -ne 0 ]; then
    echo "Please run as root or with sudo."
    exit 1
fi

echo "Resetting UDE configuration to default..."

# Step 1: Backup current configuration files (optional)
echo "Backing up current configuration files to ~/.config/ude_backup"
mkdir -p ~/.config/ude_backup
cp -r ~/.config/ude/* ~/.config/ude_backup/

# Step 2: Remove current UDE configuration files
echo "Removing current configuration files..."
rm -rf ~/.config/ude/*

# Step 3: Restore default configuration files
echo "Restoring default configuration files..."
cp config/ude-config.conf ~/.config/ude/
cp config/time-based-config.conf ~/.config/ude/

# Step 4: Notify user of successful reset
echo "UDE configuration has been reset to the default settings."

# Optional: Restart UDE
echo "To restart UDE, run: python3 src/main.py"
