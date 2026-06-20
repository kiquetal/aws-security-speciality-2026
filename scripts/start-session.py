#!/usr/bin/env python3
"""Start a new blank study session/drill in notes/question-tracker.md and recompile tracker data."""

import re
import sys
import os
import argparse
from datetime import date
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
TRACKER_PATH = BASE_DIR / "notes" / "question-tracker.md"

DEFAULT_DOMAINS = "D1 Detection · D2 Incident Response · D3 Infrastructure Security · D4 Identity & Access Management · D5 Data Protection · D6 Governance"

def get_next_session_num():
    if not TRACKER_PATH.exists():
        return 1
    text = TRACKER_PATH.read_text(encoding="utf-8")
    session_nums = [int(n) for n in re.findall(r"^### Session (\d+)", text, re.MULTILINE)]
    return max(session_nums) + 1 if session_nums else 1

def start_session(questions_count, domains=DEFAULT_DOMAINS):
    next_num = get_next_session_num()
    today = date.today().strftime("%Y-%m-%d")
    
    # Generate new session markdown block
    lines = [
        "",
        f"### Session {next_num} — {today}",
        "",
        f"**Domains:** {domains}",
        f"**Score:** 0 ✅ · 0 ⚠️ · 0 ❌ (0% correct)",
        "",
        "| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Review Topic |",
        "|---|---|---|---|---|---|---|",
    ]
    
    # Generate blank rows
    for i in range(1, questions_count + 1):
        lines.append(f"| {i} | | | | ⬜ | | |")
        
    lines.append("") # End with newline
    session_md = "\n".join(lines)
    
    # Read current content and append
    text = TRACKER_PATH.read_text(encoding="utf-8")
    
    # Ensure there is a ## Sessions header
    if "## Sessions" not in text:
        text += "\n\n## Sessions"
        
    # Append new session
    text = text.rstrip() + "\n" + session_md
    TRACKER_PATH.write_text(text, encoding="utf-8")
    print(f"✅ Successfully appended Session {next_num} ({questions_count} questions) to question-tracker.md")
    return next_num

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a new empty practice session/drill.")
    parser.add_argument("-q", "--questions", type=int, default=25, help="Number of questions in this drill (default: 25)")
    parser.add_argument("-d", "--domains", type=str, default=DEFAULT_DOMAINS, help="Domains covered in this drill")
    args = parser.parse_args()
    
    try:
        start_session(args.questions, args.domains)
    except Exception as e:
        print(f"❌ Error starting session: {e}", file=sys.stderr)
        sys.exit(1)
