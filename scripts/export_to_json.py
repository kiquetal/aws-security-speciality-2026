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
CHEAT_SHEET_PATH = BASE_DIR / "notes" / "cheat-sheet.md"
MAINTENANCE_PLAN_PATH = BASE_DIR / "notes" / "maintenance-plan.md"

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

def parse_maintenance_plan():
    """Parse week-by-week progress from notes/maintenance-plan.md."""
    if not MAINTENANCE_PLAN_PATH.exists():
        return []
    
    text = MAINTENANCE_PLAN_PATH.read_text(encoding="utf-8")
    weeks = []
    lines = text.splitlines()
    table_started = False
    for line in lines:
        if "Never-Seen Included" in line and "Status" in line:
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
            if len(cols) >= 5:
                week_num = cols[0]
                date_range = cols[1]
                focus = cols[2]
                never_seen = cols[3]
                status = cols[4]  # ✅ or ⬜
                
                is_completed = "✅" in status
                weeks.append({
                    "week": week_num,
                    "date": date_range,
                    "focus": focus,
                    "never_seen": never_seen,
                    "status": "completed" if is_completed else "pending",
                    "status_raw": status
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
                "session_num": num,
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
        # Handle multi-domain questions (e.g. D1/D2) by counting them for all listed domains
        domains = [d.strip() for d in q["domain_raw"].split("/") if d.strip()]
        for d in domains:
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
            weak_topics_dict[t]["questions"].append(f"S{q['session_num']}-Q{q['num']}")
            domains = [d.strip() for d in q["domain_raw"].split("/") if d.strip()]
            for d in domains:
                if d in DOMAIN_NAMES:
                    weak_topics_dict[t]["domains"].add(d)
                
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

def parse_cheat_sheet():
    """Parse notes/cheat-sheet.md into structured sections with subsections, lists, and tables."""
    if not CHEAT_SHEET_PATH.exists():
        return []
    
    text = CHEAT_SHEET_PATH.read_text(encoding="utf-8")
    lines = text.splitlines()
    
    sections = []
    current_section = None
    current_subsection = None
    
    # Simple table parsing state
    in_table = False
    table_headers = []
    table_rows = []
    
    for line in lines:
        line_stripped = line.strip()
        
        # Parse main headings: ## Section Name
        if line_stripped.startswith("## "):
            # If we were in a table, close it
            if in_table and current_subsection:
                current_subsection["items"].append({
                    "type": "table",
                    "headers": table_headers,
                    "rows": table_rows
                })
                in_table = False
                table_headers = []
                table_rows = []
            
            title = line_stripped[3:].strip()
            # Determine category (D1-D6 or other)
            category = "General"
            for d in ["D1", "D2", "D3", "D4", "D5", "D6"]:
                if d in title:
                    category = d
                    break
            
            current_section = {
                "title": title,
                "category": category,
                "subsections": []
            }
            sections.append(current_section)
            current_subsection = None
            continue
            
        # Parse subheadings: ### Subsection Name
        elif line_stripped.startswith("### "):
            if not current_section:
                continue
                
            # If we were in a table, close it
            if in_table and current_subsection:
                current_subsection["items"].append({
                    "type": "table",
                    "headers": table_headers,
                    "rows": table_rows
                })
                in_table = False
                table_headers = []
                table_rows = []
                
            sub_title = line_stripped[4:].strip()
            current_subsection = {
                "title": sub_title,
                "items": []
            }
            current_section["subsections"].append(current_subsection)
            continue
            
        # Parse bullet points or tables or regular text
        elif current_section:
            # If no subsection exists yet, create an empty-title one
            if not current_subsection:
                current_subsection = {
                    "title": "",
                    "items": []
                }
                current_section["subsections"].append(current_subsection)
                
            # Table row parsing
            if line_stripped.startswith("|"):
                parts = [c.strip() for c in line_stripped.split("|")[1:-1]]
                if not in_table:
                    # This is the header row
                    table_headers = parts
                    table_rows = []
                    in_table = True
                else:
                    # Check if it is the separator row like |---|---|
                    if all(re.match(r"^:?-+:?$", p) for p in parts if p):
                        continue
                    table_rows.append(parts)
                continue
            else:
                # If we were in a table and see a non-table line, close the table
                if in_table:
                    current_subsection["items"].append({
                        "type": "table",
                        "headers": table_headers,
                        "rows": table_rows
                    })
                    in_table = False
                    table_headers = []
                    table_rows = []
            
            # Bullet point parsing
            if line_stripped.startswith("- ") or line_stripped.startswith("* "):
                bullet_text = line_stripped[2:].strip()
                
                # Check for emojis/status
                is_insight = "🧠" in bullet_text
                is_warning = "⚠️" in bullet_text
                
                # Clean up the text (remove leading emojis if any)
                clean_text = bullet_text.replace("🧠", "").replace("⚠️", "").strip()
                
                current_subsection["items"].append({
                    "type": "bullet",
                    "text": clean_text,
                    "is_insight": is_insight,
                    "is_warning": is_warning
                })
                
            # Regular text
            elif line_stripped and not line_stripped.startswith("---") and not line_stripped.startswith(">"):
                current_subsection["items"].append({
                    "type": "text",
                    "text": line_stripped
                })
                
    # Close any trailing table at the very end of the file
    if in_table and current_subsection:
        current_subsection["items"].append({
            "type": "table",
            "headers": table_headers,
            "rows": table_rows
        })
        
    # Clean up subsections: discard those with no items
    for s in sections:
        s["subsections"] = [sub for sub in s["subsections"] if len(sub["items"]) > 0]
        
    return sections


def parse_all_faqs():
    """Parse all faq-*.md files in notes/ into structured FAQ list."""
    faq_dir = BASE_DIR / "notes"
    faq_files = sorted(faq_dir.glob("faq-*.md"))
    
    faqs = []
    
    for filepath in faq_files:
        filename = filepath.name
        try:
            text = filepath.read_text(encoding="utf-8")
        except Exception as e:
            print(f"Error reading {filename}: {e}")
            continue
            
        lines = text.splitlines()
        
        # Extract title from the first H1 line
        title = filename.replace("faq-", "").replace(".md", "").replace("-", " ").title()
        for line in lines:
            if line.strip().startswith("# "):
                title = line.strip()[2:].replace("FAQ:", "").replace("FAQ", "").strip()
                break
                
        sections = []
        current_section = None
        current_subsection = None
        
        in_table = False
        table_headers = []
        table_rows = []
        
        in_codeblock = False
        code_lines = []
        
        for line in lines:
            line_stripped = line.strip()
            
            # Skip H1 header line
            if line_stripped.startswith("# "):
                continue
                
            # Code block toggle
            if line_stripped.startswith("```"):
                if in_codeblock:
                    in_codeblock = False
                    if current_subsection:
                        current_subsection["items"].append({
                            "type": "code",
                            "text": "\n".join(code_lines)
                        })
                    code_lines = []
                else:
                    # Close any active table
                    if in_table and current_subsection:
                        current_subsection["items"].append({
                            "type": "table",
                            "headers": table_headers,
                            "rows": table_rows
                        })
                        in_table = False
                        table_headers = []
                        table_rows = []
                    in_codeblock = True
                    code_lines = []
                continue
                
            if in_codeblock:
                code_lines.append(line)
                continue
                
            # Parse H2 section headings: ## Section Name
            if line_stripped.startswith("## "):
                # If we were in a table, close it
                if in_table and current_subsection:
                    current_subsection["items"].append({
                        "type": "table",
                        "headers": table_headers,
                        "rows": table_rows
                    })
                    in_table = False
                    table_headers = []
                    table_rows = []
                
                section_title = line_stripped[3:].strip()
                current_section = {
                    "title": section_title,
                    "subsections": []
                }
                sections.append(current_section)
                current_subsection = None
                continue
                
            # Parse H3 subsection headings: ### Subsection Name
            elif line_stripped.startswith("### "):
                if not current_section:
                    # Create an implicit section if none exists
                    current_section = {
                        "title": "General",
                        "subsections": []
                    }
                    sections.append(current_section)
                    
                # If we were in a table, close it
                if in_table and current_subsection:
                    current_subsection["items"].append({
                        "type": "table",
                        "headers": table_headers,
                        "rows": table_rows
                    })
                    in_table = False
                    table_headers = []
                    table_rows = []
                    
                sub_title = line_stripped[4:].strip()
                current_subsection = {
                    "title": sub_title,
                    "items": []
                }
                current_section["subsections"].append(current_subsection)
                continue
                
            # Parse contents
            elif current_section:
                if not current_subsection:
                    current_subsection = {
                        "title": "",
                        "items": []
                    }
                    current_section["subsections"].append(current_subsection)
                    
                # Table rows
                if line_stripped.startswith("|"):
                    parts = [c.strip() for c in line_stripped.split("|")[1:-1]]
                    if not in_table:
                        table_headers = parts
                        table_rows = []
                        in_table = True
                    else:
                        if all(re.match(r"^:?-+:?$", p) for p in parts if p):
                            continue
                        table_rows.append(parts)
                    continue
                else:
                    if in_table:
                        current_subsection["items"].append({
                            "type": "table",
                            "headers": table_headers,
                            "rows": table_rows
                        })
                        in_table = False
                        table_headers = []
                        table_rows = []
                
                # Bullet points
                if line_stripped.startswith("- ") or line_stripped.startswith("* "):
                    bullet_text = line_stripped[2:].strip()
                    is_insight = "🧠" in bullet_text
                    is_warning = "⚠️" in bullet_text
                    clean_text = bullet_text.replace("🧠", "").replace("⚠️", "").strip()
                    
                    current_subsection["items"].append({
                        "type": "bullet",
                        "text": clean_text,
                        "is_insight": is_insight,
                        "is_warning": is_warning
                    })
                    
                # Blockquotes
                elif line_stripped.startswith(">"):
                    quote_text = line_stripped[1:].strip()
                    is_insight = "🧠" in quote_text
                    is_warning = "⚠️" in quote_text
                    clean_text = quote_text.replace("🧠", "").replace("⚠️", "").strip()
                    
                    current_subsection["items"].append({
                        "type": "blockquote",
                        "text": clean_text,
                        "is_insight": is_insight,
                        "is_warning": is_warning
                    })
                    
                # Regular text
                elif line_stripped and not line_stripped.startswith("---"):
                    current_subsection["items"].append({
                        "type": "text",
                        "text": line_stripped
                    })
                    
        # Close any trailing table
        if in_table and current_subsection:
            current_subsection["items"].append({
                "type": "table",
                "headers": table_headers,
                "rows": table_rows
            })
            
        # Close any trailing code block
        if in_codeblock and current_subsection and code_lines:
            current_subsection["items"].append({
                "type": "code",
                "text": "\n".join(code_lines)
            })
            
        # Filter subsections with actual items
        for s in sections:
            s["subsections"] = [sub for sub in s["subsections"] if len(sub["items"]) > 0]
        # Filter sections with actual subsections
        sections = [s for s in sections if len(s["subsections"]) > 0]
        
        faqs.append({
            "filename": filename,
            "title": title,
            "sections": sections
        })
        
    return faqs

def main():
    import sys
    is_blank = any(flag in sys.argv for flag in ["--blank", "--onboarding", "--live-demo"])
    
    print("Parsing study-plan.md...")
    weeks = parse_study_plan()
    
    print("Parsing notes/maintenance-plan.md...")
    maintenance_plan = parse_maintenance_plan()
    
    print("Parsing question-tracker.md...")
    sessions, domain_proficiency, weak_areas, stats = parse_tracker_sessions()
    
    print("Parsing cheat-sheet.md...")
    cheat_sheet = parse_cheat_sheet()
    
    print("Parsing notes/faq-*.md files...")
    faqs = parse_all_faqs()
    
    if is_blank:
        print("Override: Compiling clean slate for Live Demo (0 sessions, 0 hours, 0% stats)...")
        sessions = []
        weak_areas = []
        stats = {
            "total_questions": 0,
            "correct": 0,
            "partial": 0,
            "wrong": 0,
            "sessions_count": 0,
            "retests_total": 0,
            "retests_passed": 0,
            "accuracy_pct": 0
        }
        domain_proficiency = {}
        for d_code, name in DOMAIN_NAMES.items():
            domain_proficiency[d_code] = {
                "code": d_code,
                "name": name,
                "correct": 0,
                "partial": 0,
                "wrong": 0,
                "total": 0,
                "score_pct": 0,
                "status": "Critical"
            }
            
    tracker_data = {
        "stats": stats,
        "weeks": weeks,
        "maintenance_plan": maintenance_plan,
        "domain_proficiency": domain_proficiency,
        "weak_areas": weak_areas,
        "sessions": sessions,
        "cheat_sheet": cheat_sheet,
        "faqs": faqs
    }
    
    # Ensure export directory exists
    EXPORT_JS_PATH.parent.mkdir(parents=True, exist_ok=True)
    
    # Export as tracker_data.js
    js_content = f"// Automatically generated by scripts/export_to_json.py\nconst TRACKER_DATA = {json.dumps(tracker_data, indent=2)};\n"
    EXPORT_JS_PATH.write_text(js_content, encoding="utf-8")
    
    print(f"Successfully exported tracker data to {EXPORT_JS_PATH}")
    print(f"Parsed {stats['total_questions']} questions, {len(sessions)} sessions, {len(weeks)} study-plan weeks, {len(maintenance_plan)} maintenance weeks, {len(cheat_sheet)} cheat-sheet sections, {len(faqs)} FAQ guides.")

if __name__ == "__main__":
    main()
