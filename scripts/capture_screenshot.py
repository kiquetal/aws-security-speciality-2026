#!/usr/bin/env python3
"""Capture a headless Chrome screenshot of the index.html dashboard."""

import subprocess
import os
import sys

# Get absolute paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDEX_PATH = os.path.join(BASE_DIR, "design", "index.html")
OUTPUT_PATH = os.path.join(BASE_DIR, "diagrams", "dashboard.png")

def capture():
    print(f"📸 Capturing headless Chrome screenshot of {INDEX_PATH}...")
    
    # Ensure diagrams directory exists
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    
    cmd = [
        "google-chrome",
        "--headless",
        "--no-sandbox",
        "--disable-dev-shm-usage",
        "--disable-gpu",
        f"--screenshot={OUTPUT_PATH}",
        "--window-size=1440,900",
        "--virtual-time-budget=5000",
        f"file://{INDEX_PATH}"
    ]
    
    try:
        subprocess.run(cmd, capture_output=True, text=True, check=True)
        print(f"✅ Screenshot successfully saved to: {OUTPUT_PATH}")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error during capture: {e.stderr}", file=sys.stderr)
        sys.exit(1)
    except FileNotFoundError:
        print("❌ Error: google-chrome executable not found in PATH.", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    capture()
