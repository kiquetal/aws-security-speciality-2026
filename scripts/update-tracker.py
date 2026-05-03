#!/usr/bin/env python3
"""Regenerate summary sections in notes/question-tracker.md from session data."""

import re
from pathlib import Path
from collections import defaultdict

TRACKER = Path(__file__).resolve().parent.parent / "notes" / "question-tracker.md"

DOMAIN_NAMES = {
    "D1": "D1: Detection",
    "D2": "D2: Incident Response",
    "D3": "D3: Infrastructure Security",
    "D4": "D4: Identity & Access Management",
    "D5": "D5: Data Protection",
    "D6": "D6: Governance",
}

RESULT_MAP = {"✅": "correct", "⚠️": "partial", "❌": "wrong"}


def parse_sessions(text):
    """Parse all session blocks, return list of session metadata + question rows."""
    sessions = []
    # Split on session headers
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
            if not cols or cols[0].startswith("#") or cols[0].startswith("-"):
                continue
            if not re.match(r"\d+", cols[0]):
                continue
            q_num = int(cols[0])
            domain = cols[1] if len(cols) > 1 else ""
            result = ""
            for symbol, label in RESULT_MAP.items():
                # Result column is index 4 in standard table, but check all cols
                result_col = cols[4] if len(cols) > 4 else ""
                if symbol in result_col:
                    result = label
                    break
            review = cols[-1] if cols[-1] else ""
            retest = ""
            # Check for re-test column (sessions with 8 cols have it at index 6)
            if len(cols) >= 7:
                candidate = cols[6] if len(cols) == 8 else cols[-2]
                if re.match(r"Q\d+", candidate):
                    retest = candidate
            questions.append({
                "num": q_num, "domain": domain, "result": result,
                "review": review, "retest": retest,
            })
        sessions.append({
            "num": num, "date": date, "domains": domains_str,
            "questions": questions,
        })
    return sessions


def build_quick_stats(sessions):
    all_q = [q for s in sessions for q in s["questions"]]
    total = len(all_q)
    correct = sum(1 for q in all_q if q["result"] == "correct")
    partial = sum(1 for q in all_q if q["result"] == "partial")
    wrong = sum(1 for q in all_q if q["result"] == "wrong")
    retests = [q for q in all_q if q["retest"]]
    retests_passed = sum(1 for q in retests if q["result"] == "correct")
    pct = lambda n: f"{n / total * 100:.0f}%" if total else "0%"
    lines = [
        "## Quick Stats (Cumulative)",
        "",
        "| Metric | Value |",
        "|---|---|",
        f"| **Total Questions** | {total} |",
        f"| **✅ Correct** | {correct} ({pct(correct)}) |",
        f"| **⚠️ Partial** | {partial} ({pct(partial)}) |",
        f"| **❌ Wrong** | {wrong} ({pct(wrong)}) |",
        f"| **Sessions** | {len(sessions)} |",
        f"| **Re-tests Passed** | {retests_passed} of {len(retests)} |" if retests else "| **Re-tests Passed** | 0 |",
    ]
    return "\n".join(lines)


def build_domain_breakdown(sessions):
    counts = defaultdict(lambda: {"correct": 0, "partial": 0, "wrong": 0})
    for s in sessions:
        for q in s["questions"]:
            d = q["domain"].split("/")[0].strip()  # handle "D4/D6" → "D4"
            if d and q["result"]:
                counts[d][q["result"]] += 1
    lines = [
        "## Domain Breakdown",
        "",
        "| Domain | ✅ | ⚠️ | ❌ | Total | Score % | Weak? |",
        "|---|---|---|---|---|---|---|",
    ]
    for key in ["D1", "D2", "D3", "D4", "D5", "D6"]:
        c = counts.get(key, {"correct": 0, "partial": 0, "wrong": 0})
        total = c["correct"] + c["partial"] + c["wrong"]
        if total == 0:
            lines.append(f"| {DOMAIN_NAMES[key]} | 0 | 0 | 0 | 0 | — | — |")
        else:
            pct = c["correct"] / total * 100
            flag = "🔴" if pct < 50 else ("🟡" if pct < 80 else "🟢")
            lines.append(f"| {DOMAIN_NAMES[key]} | {c['correct']} | {c['partial']} | {c['wrong']} | {total} | {pct:.0f}% | {flag} |")
    lines.append("")
    lines.append("Legend: 🔴 < 50% — 🟡 50–79% — 🟢 ≥ 80%")
    return "\n".join(lines)


def build_weak_areas(sessions):
    """Collect review topics from ❌ and ⚠️ questions, group by topic."""
    topics = defaultdict(lambda: {"questions": [], "domains": set()})
    for s in sessions:
        for q in s["questions"]:
            if q["result"] in ("wrong", "partial") and q["review"]:
                t = q["review"]
                topics[t]["questions"].append(f"Q{q['num']}")
                d = q["domain"].split("/")[0].strip()
                if d:
                    topics[t]["domains"].add(d)
    # Sort by number of misses descending
    sorted_topics = sorted(topics.items(), key=lambda x: len(x[1]["questions"]), reverse=True)
    lines = [
        "## Weak Areas to Review",
        "",
        "| Priority | Topic | Questions | Domain | Count |",
        "|---|---|---|---|---|",
    ]
    for i, (topic, data) in enumerate(sorted_topics, 1):
        flag = "🔴" if len(data["questions"]) >= 2 else "🟡"
        qs = ", ".join(data["questions"])
        domains = ", ".join(sorted(data["domains"]))
        lines.append(f"| {flag} {i} | {topic} | {qs} | {domains} | {len(data['questions'])} |")
    return "\n".join(lines)


def build_session_index(sessions):
    lines = [
        "## Session Index",
        "",
        "| # | Date | Questions | ✅ | ⚠️ | ❌ | Domains Covered | Link |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for s in sessions:
        qs = s["questions"]
        if not qs:
            continue
        q_range = f"Q{qs[0]['num']}–Q{qs[-1]['num']}"
        c = sum(1 for q in qs if q["result"] == "correct")
        p = sum(1 for q in qs if q["result"] == "partial")
        w = sum(1 for q in qs if q["result"] == "wrong")
        # Build anchor: "### Session 1 — 2025-05-01" → "#session-1--2025-05-01"
        anchor = f"#session-{s['num']}--{s['date']}"
        lines.append(f"| {s['num']} | {s['date']} | {q_range} | {c} | {p} | {w} | {s['domains']} | [Jump]({anchor}) |")
    return "\n".join(lines)


def main():
    text = TRACKER.read_text(encoding="utf-8")
    sessions = parse_sessions(text)
    if not sessions:
        print("No sessions found. Nothing to update.")
        return

    # Rebuild computed sections
    new_stats = build_quick_stats(sessions)
    new_domains = build_domain_breakdown(sessions)
    new_weak = build_weak_areas(sessions)
    new_index = build_session_index(sessions)

    # Extract header (everything before Quick Stats) and sessions block (from ## Sessions onward)
    header_match = re.search(r"^(# .+?\n>.*?\n)", text, re.DOTALL)
    header = header_match.group(1) if header_match else "# SCS-C03 Question Tracker\n\n> Track every question attempted. Review ❌ and ⚠️ items before the exam.\n"

    sessions_match = re.search(r"(^## Sessions$.+)", text, re.MULTILINE | re.DOTALL)
    sessions_block = sessions_match.group(1) if sessions_match else ""

    output = f"""{header}
---

{new_stats}

{new_domains}

{new_weak}

---

{new_index}

---

{sessions_block}"""

    TRACKER.write_text(output, encoding="utf-8")
    print(f"Updated question-tracker.md — {len(sessions)} sessions, {sum(len(s['questions']) for s in sessions)} questions.")


if __name__ == "__main__":
    main()
