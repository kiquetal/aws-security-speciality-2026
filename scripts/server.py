#!/usr/bin/env python3
"""Custom HTTP Server for Aether Guard.

Serves static files from the design directory and handles /api/sync POST requests
to dynamically execute the question sync scripts.
"""

import http.server
import socketserver
import subprocess
import os
import json
import sys

PORT = int(os.environ.get("PORT", 8188))
DIRECTORY = "design"

# Get absolute path to the project root directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class AetherGuardHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        # Always serve from the static design directory
        super().__init__(*args, directory=os.path.join(BASE_DIR, DIRECTORY), **kwargs)

    def do_POST(self):
        if self.path == "/api/sync":
            try:
                # 1. Execute update-tracker.py
                tracker_script = os.path.join(BASE_DIR, "scripts", "update-tracker.py")
                res1 = subprocess.run([sys.executable, tracker_script], capture_output=True, text=True, cwd=BASE_DIR)
                if res1.returncode != 0:
                    raise Exception(f"update-tracker.py failed:\n{res1.stderr}")
                
                # 2. Execute export_to_json.py
                export_script = os.path.join(BASE_DIR, "scripts", "export_to_json.py")
                res2 = subprocess.run([sys.executable, export_script], capture_output=True, text=True, cwd=BASE_DIR)
                if res2.returncode != 0:
                    raise Exception(f"export_to_json.py failed:\n{res2.stderr}")

                # Success response
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.send_header("Access-Control-Allow-Origin", "*")
                self.end_headers()
                
                response = {
                    "status": "success", 
                    "message": "Study tracker synchronized successfully!"
                }
                self.wfile.write(json.dumps(response).encode("utf-8"))
                print("🔄 [API] Study tracker synchronized successfully via live Sync Button.")
                
            except Exception as e:
                self.send_response(500)
                self.send_header("Content-Type", "application/json")
                self.send_header("Access-Control-Allow-Origin", "*")
                self.end_headers()
                
                response = {
                    "status": "error", 
                    "message": str(e)
                }
                self.wfile.write(json.dumps(response).encode("utf-8"))
                print(f"❌ [API Error] Sync failed: {e}")
        elif self.path == "/api/start-session":
            try:
                # Read content length and load JSON body
                content_length = int(self.headers.get('Content-Length', 0))
                body = self.rfile.read(content_length).decode('utf-8')
                data = json.loads(body) if body else {}
                
                questions = data.get("questions", 25)
                domains = data.get("domains", "D1 Detection · D2 Incident Response · D3 Infrastructure Security · D4 Identity & Access Management · D5 Data Protection · D6 Governance")
                demo = data.get("demo", False)
                
                # Execute start-session.py
                start_script = os.path.join(BASE_DIR, "scripts", "start-session.py")
                cmd_args = [sys.executable, start_script, "--questions", str(questions), "--domains", domains]
                if demo:
                    cmd_args.append("--demo")
                
                res_start = subprocess.run(cmd_args, capture_output=True, text=True, cwd=BASE_DIR)
                if res_start.returncode != 0:
                    raise Exception(f"start-session.py failed:\n{res_start.stderr}")
                
                # After starting session, compile trackers
                tracker_script = os.path.join(BASE_DIR, "scripts", "update-tracker.py")
                res1 = subprocess.run([sys.executable, tracker_script], capture_output=True, text=True, cwd=BASE_DIR)
                if res1.returncode != 0:
                    raise Exception(f"update-tracker.py failed:\n{res1.stderr}")
                
                export_script = os.path.join(BASE_DIR, "scripts", "export_to_json.py")
                res2 = subprocess.run([sys.executable, export_script], capture_output=True, text=True, cwd=BASE_DIR)
                if res2.returncode != 0:
                    raise Exception(f"export_to_json.py failed:\n{res2.stderr}")

                # Success response
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.send_header("Access-Control-Allow-Origin", "*")
                self.end_headers()
                
                response = {
                    "status": "success", 
                    "message": "Practice session generated successfully!"
                }
                self.wfile.write(json.dumps(response).encode("utf-8"))
                print(f"🚀 [API] New session ({questions} questions) generated successfully.")
                
            except Exception as e:
                self.send_response(500)
                self.send_header("Content-Type", "application/json")
                self.send_header("Access-Control-Allow-Origin", "*")
                self.end_headers()
                
                response = {
                    "status": "error", 
                    "message": str(e)
                }
                self.wfile.write(json.dumps(response).encode("utf-8"))
                print(f"❌ [API Error] Start session failed: {e}")
        else:
            self.send_error(404, "Endpoint not found")

    def do_OPTIONS(self):
        # Support preflight CORS if needed
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS, GET")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

def run():
    # Change current working directory to the project root
    os.chdir(BASE_DIR)
    
    # Set socket options to reuse addresses immediately
    socketserver.TCPServer.allow_reuse_address = True
    
    try:
        with socketserver.TCPServer(("", PORT), AetherGuardHandler) as httpd:
            print("====================================================")
            print("🛡️  Aether Guard — Live Sync Server Active  🛡️")
            print("====================================================")
            print(f"👉 Portal is live at: http://localhost:{PORT}")
            print(f"🔄 Sync API is ready at: http://localhost:{PORT}/api/sync")
            print("ℹ️  Press Ctrl+C to stop the server")
            print("====================================================")
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n👋 Stopping Aether Guard server. Safe journeys!")
        sys.exit(0)
    except Exception as e:
        print(f"❌ Error starting server: {e}")
        sys.exit(1)

if __name__ == "__main__":
    run()
