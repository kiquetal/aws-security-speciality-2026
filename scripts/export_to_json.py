#!/usr/bin/env python3
"""Parse question-tracker.md and study-plan.md, then export them to design/tracker_data.js."""

import re
import json
from pathlib import Path
from collections import defaultdict

BASE_DIR = Path(__file__).resolve().parent.parent
TRACKER_PATH = BASE_DIR / "notes" / "question-tracker.md"
STUDY_PLAN_PATH = BASE_DIR / "study-plan.md"
EXPORT_JS_PATH = BASE_DIR / "design" / "tracker_data.js"

DOMAIN_NAMES = {
    "D1": "Detection",
    "D2": "Incident Response",
    "D3": "Infrastructure Security",
    "D4": "Identity & Access Management",
    "D5": "Data Protection",
    "D6": "Governance",
}

RESULT_MAP = {"✅": "correct", "⚠️": "partial", "❌": "wrong"}

def parse_study_plan():
    """Parse week-by-week progress from study-plan.md."""
    if not STUDY_PLAN_PATH.exists():
        return []
    
    text = STUDY_PLAN_PATH.read_text(encoding="utf-8")
    # Find progress tracker table
    weeks = []
    lines = text.splitlines()
    table_started = False
    for line in lines:
        if "Domain / Focus" in line and "Status" in line:
            table_started = True
            continue
        if table_started:
            if not line.strip() or not line.startswith("|"):
                if weeks:  # End of table
                    break
                continue
            if "---" in line:
                continue
            cols = [c.strip() for c in line.split("|")[1:-1]]
            if len(cols) >= 3:
                week_num = cols[0]
                focus = cols[1]
                status = cols[2]  # ✅ or ⬜ or In progress
                notes = cols[3] if len(cols) > 3 else ""
                
                # Clean status
                is_completed = "✅" in status
                weeks.append({
                    "week": week_num,
                    "focus": focus,
                    "status": "completed" if is_completed else ("in_progress" if "In progress" in status or "⬜" not in status else "pending"),
                    "status_raw": status,
                    "notes": notes
                })
    return weeks

def parse_tracker_sessions():
    """Parse sessions and questions from question-tracker.md."""
    if not TRACKER_PATH.exists():
        return [], {}, []

    text = TRACKER_PATH.read_text(encoding="utf-8")
    
    # Split sessions
    sessions = []
    parts = re.split(r"(?=^### Session \d+)", text, flags=re.MULTILINE)
    
    for part in parts:
        header = re.match(r"### Session (\d+) — (\d{4}-\d{2}-\d{2})", part)
        if not header:
            continue
        num, date = int(header.group(1)), header.group(2)
        
        # Extract domains line
        domains_match = re.search(r"\*\*Domains:\*\*\s*(.+)", part)
        domains_str = domains_match.group(1).strip() if domains_match else ""
        
        # Parse table rows (skip header + separator)
        rows = re.findall(r"^\|(.+)\|$", part, re.MULTILINE)
        questions = []
        for row in rows:
            cols = [c.strip() for c in row.split("|")]
            # Skip header/separator rows
            if not cols or cols[0].startswith("#") or cols[0].startswith("-") or cols[0].lower() == "domain" or cols[0] == "":
                continue
            if not re.match(r"\d+", cols[0]):
                continue
            
            q_num = int(cols[0])
            domain = cols[1] if len(cols) > 1 else ""
            scenario = cols[2] if len(cols) > 2 else ""
            your_answer = cols[3] if len(cols) > 3 else ""
            
            # Figure out result
            result_symbol = cols[4] if len(cols) > 4 else ""
            result = "unknown"
            for symbol, label in RESULT_MAP.items():
                if symbol in result_symbol:
                    result = label
                    break
            
            # Correct answer column (index 5)
            correct_answer = cols[5] if len(cols) > 5 else ""
            
            # Let's look at remaining columns to figure out Retest and Review
            retest = ""
            review = ""
            if len(cols) == 8: # | # | Domain | Scenario | Your Answer | Result | Correct Answer | Re-test of | Review Topic |
                retest = cols[6]
                review = cols[7]
            elif len(cols) == 7: # | # | Domain | Scenario | Your Answer | Result | Correct Answer | Review Topic |
                review = cols[6]
            
            # Clean retest
            if retest == "—" or retest == "-":
                retest = ""
                
            questions.append({
                "num": q_num,
                "domain": domain.split("/")[0].strip(), # Handles e.g., D4/D6 -> D4
                "domain_raw": domain,
                "scenario": scenario,
                "your_answer": your_answer,
                "result": result,
                "correct_answer": correct_answer,
                "retest": retest,
                "review": review
            })
            
        sessions.append({
            "num": num,
            "date": date,
            "domains": domains_str,
            "questions": questions
        })
        
    # Re-calculate accurate cumulative stats
    all_q = [q for s in sessions for q in s["questions"]]
    total_q = len(all_q)
    correct = sum(1 for q in all_q if q["result"] == "correct")
    partial = sum(1 for q in all_q if q["result"] == "partial")
    wrong = sum(1 for q in all_q if q["result"] == "wrong")
    
    retests = [q for q in all_q if q["retest"]]
    retests_total = len(retests)
    retests_passed = sum(1 for q in retests if q["result"] == "correct")
    
    # Calculate domain breakdown
    domain_counts = defaultdict(lambda: {"correct": 0, "partial": 0, "wrong": 0, "unknown": 0})
    for q in all_q:
        d = q["domain"]
        if d in DOMAIN_NAMES:
            domain_counts[d][q["result"]] += 1
            
    domain_proficiency = {}
    for d_code, name in DOMAIN_NAMES.items():
        c = domain_counts.get(d_code, {"correct": 0, "partial": 0, "wrong": 0, "unknown": 0})
        total = c["correct"] + c["partial"] + c["wrong"] + c["unknown"]
        score_pct = int(round(c["correct"] / total * 100)) if total > 0 else 0
        domain_proficiency[d_code] = {
            "code": d_code,
            "name": name,
            "correct": c["correct"],
            "partial": c["partial"],
            "wrong": c["wrong"],
            "total": total,
            "score_pct": score_pct,
            "status": "Master" if score_pct >= 85 else ("Solid" if score_pct >= 75 else ("Passing" if score_pct >= 65 else "Critical"))
        }

    # Calculate Weak Areas
    weak_topics_dict = defaultdict(lambda: {"questions": [], "domains": set()})
    for q in all_q:
        if q["result"] in ("wrong", "partial") and q["review"]:
            t = q["review"]
            weak_topics_dict[t]["questions"].append(f"Q{q['num']}")
            if q["domain"]:
                weak_topics_dict[t]["domains"].add(q["domain"])
                
    weak_areas = []
    sorted_topics = sorted(weak_topics_dict.items(), key=lambda x: len(x[1]["questions"]), reverse=True)
    for i, (topic, data) in enumerate(sorted_topics, 1):
        weak_areas.append({
            "priority": i,
            "topic": topic,
            "questions": data["questions"],
            "domains": list(data["domains"]),
            "count": len(data["questions"]),
            "level": "red" if len(data["questions"]) >= 3 else "yellow"
        })
        
    stats = {
        "total_questions": total_q,
        "correct": correct,
        "partial": partial,
        "wrong": wrong,
        "sessions_count": len(sessions),
        "retests_total": retests_total,
        "retests_passed": retests_passed,
        "accuracy_pct": int(round(correct / total_q * 100)) if total_q > 0 else 0
    }
    
    return sessions, domain_proficiency, weak_areas, stats

def main():
    print("Parsing study-plan.md...")
    weeks = parse_study_plan()
    
    print("Parsing question-tracker.md...")
    sessions, domain_proficiency, weak_areas, stats = parse_tracker_sessions()
    
    tracker_data = {
        "stats": stats,
        "weeks": weeks,
        "domain_proficiency": domain_proficiency,
        "weak_areas": weak_areas,
        "sessions": sessions
    }
    
    # Ensure export directory exists
    EXPORT_JS_PATH.parent.mkdir(parents=True, exist_ok=True)
    
    # Export as tracker_data.js
    js_content = f"// Automatically generated by scripts/export_to_json.py\nconst TRACKER_DATA = {json.dumps(tracker_data, indent=2)};\n"
    EXPORT_JS_PATH.write_text(js_content, encoding="utf-8")
    
    print(f"Successfully exported tracker data to {EXPORT_JS_PATH}")
    print(f"Parsed {stats['total_questions']} questions, {len(sessions)} sessions, {len(weeks)} study-plan weeks.")

if __name__ == "__main__":
    main()
