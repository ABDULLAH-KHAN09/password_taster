#!/bin/bash

echo "🔐 Installing Password Taster..."
echo ""

# Check if python3 is installed
if ! command -v python3 &> /dev/null; then
    echo "📦 Installing Python3..."
    sudo apt update
    sudo apt install python3 -y
fi

# Copy to /usr/local/bin
sudo cp password_taster.py /usr/local/bin/password-taster
sudo chmod +x /usr/local/bin/password-taster

echo ""
echo "✅ Installation Complete!"
echo "🎯 Run 'password-taster' from anywhere"
echo ""
