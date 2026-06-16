#!/bin/bash

# Aether Guard Study Portal Local Server Launcher
# Automatically recompiles logs and spins up a local web server.

# Get script directory
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$DIR"

echo "============================================="
echo "🛡️  Aether Guard — AWS SCS-C03 Study Portal  🛡️"
echo "============================================="

# 1. Recompile tracker logs to ensure fresh data
echo "🔄 Compiling question logs and study plan..."
python3 scripts/export_to_json.py

if [ $? -ne 0 ]; then
    echo "⚠️  Warning: Failed to recompile logs. Using existing tracker_data.js."
fi

# 2. Determine available web servers
PORT=8188
echo ""
echo "🌐 Starting local web server on port $PORT..."

if command -v python3 &>/dev/null; then
    echo "⚡ Using Python 3 Live Sync Server..."
    echo ""
    python3 scripts/server.py
elif command -v npx &>/dev/null; then
    echo "⚡ Using Node npx http-server..."
    echo "👉 Portal is live at: http://localhost:$PORT"
    echo "ℹ️  Press Ctrl+C to stop the server"
    echo ""
    npx -y http-server design -p $PORT
elif command -v php &>/dev/null; then
    echo "⚡ Using PHP built-in server..."
    echo "👉 Portal is live at: http://localhost:$PORT"
    echo "ℹ️  Press Ctrl+C to stop the server"
    echo ""
    php -S localhost:$PORT -t design
else
    echo "❌ No built-in servers (Python, Node/npx, PHP) found."
    echo "👉 However, you can still open the file directly in your browser:"
    echo "   file://$DIR/design/index.html"
fi
