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
                quiz = data.get("quiz", False)
                blank = data.get("blank", False)
                
                # Execute start-session.py
                start_script = os.path.join(BASE_DIR, "scripts", "start-session.py")
                cmd_args = [sys.executable, start_script, "--questions", str(questions), "--domains", domains]
                if demo:
                    cmd_args.append("--demo")
                elif blank:
                    cmd_args.append("--blank")
                elif quiz:
                    cmd_args.append("--quiz")
                
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
        elif self.path == "/api/record-answer":
            try:
                import re
                from pathlib import Path
                # Read content length and load JSON body
                content_length = int(self.headers.get('Content-Length', 0))
                body = self.rfile.read(content_length).decode('utf-8')
                data = json.loads(body) if body else {}
                
                session_num = int(data.get("session_num"))
                question_num = int(data.get("question_num"))
                your_answer = str(data.get("your_answer", "")).strip()
                result = str(data.get("result", "")).strip() # ✅, ❌, or ⚠️
                
                # Update notes/question-tracker.md
                tracker_path = os.path.join(BASE_DIR, "notes", "question-tracker.md")
                if not os.path.exists(tracker_path):
                    raise Exception("question-tracker.md does not exist")
                
                content = Path(tracker_path).read_text(encoding="utf-8")
                
                # Split content by sessions to find the target session
                sessions = re.split(r"(?=^### Session \d+)", content, flags=re.MULTILINE)
                
                updated_sessions = []
                session_found = False
                for session_part in sessions:
                    header = re.match(r"### Session (\d+)", session_part)
                    if header and int(header.group(1)) == session_num:
                        session_found = True
                        # This is our target session block. Let's find the question row.
                        lines = session_part.splitlines()
                        for i, line in enumerate(lines):
                            match = re.match(r"^\|\s*(\d+)\s*\|", line)
                            if match and int(match.group(1)) == question_num:
                                # Strip leading/trailing '|' and whitespace
                                stripped_line = line.strip().strip("|")
                                cols = [c.strip() for c in stripped_line.split("|")]
                                if len(cols) >= 6:
                                    # cols[0] = question_num
                                    # cols[1] = domain
                                    # cols[2] = scenario
                                    # cols[3] = your_answer
                                    # cols[4] = result
                                    # cols[5] = correct_answer
                                    # cols[6] = review_topic (optional)
                                    cols[3] = your_answer
                                    cols[4] = result
                                    # Reconstruct the line
                                    lines[i] = "| " + " | ".join(cols) + " |"
                                break
                        session_part = "\n".join(lines)
                    updated_sessions.append(session_part)
                
                if not session_found:
                    raise Exception(f"Session {session_num} not found in question-tracker.md")
                
                # Combine back
                new_content = "".join(updated_sessions)
                Path(tracker_path).write_text(new_content, encoding="utf-8")
                
                # After updating, run compile and export
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
                    "message": f"Recorded Question {question_num} in Session {session_num} successfully!"
                }
                self.wfile.write(json.dumps(response).encode("utf-8"))
                print(f"✅ [API] Recorded answer '{your_answer}' ({result}) for Q{question_num} in Session {session_num}.")
                
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
                print(f"❌ [API Error] Record answer failed: {e}")
        elif self.path == "/api/reset-demo":
            try:
                tracker_path = os.path.join(BASE_DIR, "notes", "question-tracker.md")
                
                # Baseline content for question-tracker.md
                baseline_content = """# SCS-C03 Question Tracker

> Track every question attempted. Review ❌ and ⚠️ items before the exam.

---

## Quick Stats (Cumulative)

| Metric | Value |
|---|---|
| **Total Questions** | 0 |
| **✅ Correct** | 0 (0%) |
| **⚠️ Partial** | 0 (0%) |
| **❌ Wrong** | 0 (0%) |
| **Sessions** | 1 |
| **Re-tests Passed** | 0 |

## Domain Breakdown

| Domain | Exam Weight | ✅ | ⚠️ | ❌ | Total | Score % | Weak? |
|---|---|---|---|---|---|---|---|
| D1: Detection | 16% | 0 | 0 | 0 | 0 | — | — |
| D2: Incident Response | 14% | 0 | 0 | 0 | 0 | — | — |
| D3: Infrastructure Security | 18% | 0 | 0 | 0 | 0 | — | — |
| D4: Identity & Access Management | 20% | 0 | 0 | 0 | 0 | — | — |
| D5: Data Protection | 18% | 0 | 0 | 0 | 0 | — | — |
| D6: Governance | 14% | 0 | 0 | 0 | 0 | — | — |

Legend: 🔴 < 50% — 🟡 50–79% — 🟢 ≥ 80%

## Weak Areas to Review

| Priority | Topic | Questions | Domain | Count |
|---|---|---|---|---|

---

## Session Index

| # | Date | Questions | ✅ | ⚠️ | ❌ | Domains Covered | Link |
|---|---|---|---|---|---|---|---|

---

## Sessions

### Session 1 — 2026-06-20

**Domains:** D1 Detection · D2 Incident Response · D3 Infrastructure Security · D4 Identity & Access Management · D5 Data Protection · D6 Governance
**Score:** 0 ✅ · 0 ⚠️ · 0 ❌ (0% correct)

| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Review Topic |
|---|---|---|---|---|---|---|
"""
                with open(tracker_path, "w", encoding="utf-8") as f:
                    f.write(baseline_content)
                
                # Re-run compilation/exports
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
                    "message": "Demo tracker and session state reset to clean baseline successfully!"
                }
                self.wfile.write(json.dumps(response).encode("utf-8"))
                print("🔄 [API] Demo tracker reset to clean baseline successfully.")
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
                print(f"❌ [API Error] Reset failed: {e}")
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
