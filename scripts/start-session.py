#!/usr/bin/env python3
"""Start a new blank or demo study session/drill in notes/question-tracker.md."""

import re
import sys
import os
import argparse
import random
from datetime import date
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
TRACKER_PATH = BASE_DIR / "notes" / "question-tracker.md"

DEFAULT_DOMAINS = "D1 Detection · D2 Incident Response · D3 Infrastructure Security · D4 Identity & Access Management · D5 Data Protection · D6 Governance"

# Realistic AWS Certified Security - Specialty (SCS-C03) demo questions for onboarding.
DEMO_QUESTIONS = [
    {"domain": "D1", "scenario": "GuardDuty detects SSH brute-force attacks against EC2 instances. You need to block source IPs automatically.", "your_answer": "B", "result": "✅", "correct": "B", "topic": "GuardDuty remediation via EventBridge"},
    {"domain": "D1", "scenario": "Analyze Amazon VPC Flow Logs for rejected TCP traffic on port 3389. Filter and log only rejected packets to CloudWatch Logs.", "your_answer": "A", "result": "✅", "correct": "A", "topic": "VPC Flow Logs Rejected Traffic Filtering"},
    {"domain": "D1", "scenario": "Configure AWS Security Hub to automatically import findings from external vulnerability scanners and standard AWS services.", "your_answer": "C", "result": "❌", "correct": "D", "topic": "Security Hub Custom Finder Integration"},
    {"domain": "D1", "scenario": "Set up a CloudTrail trail to log S3 data events for a highly sensitive bucket containing financial transactions.", "your_answer": "B", "result": "⚠️", "correct": "A", "topic": "CloudTrail S3 Data Event Logging"},
    {"domain": "D2", "scenario": "An EC2 instance is suspected of being compromised. Isolate the instance immediately in the VPC without rebooting.", "your_answer": "D", "result": "✅", "correct": "D", "topic": "Incident Response - EC2 Security Group Isolation"},
    {"domain": "D2", "scenario": "Automate forensic disk capture of a compromised EC2 instance EBS volume by taking a snapshot and sharing it with a security account.", "your_answer": "C", "result": "✅", "correct": "C", "topic": "Forensic EBS Snapshot Sharing"},
    {"domain": "D2", "scenario": "Establish AWS Systems Manager Session Manager access to EC2 instances in private subnets, logging all SSH-like sessions to encrypted S3.", "your_answer": "A", "result": "✅", "correct": "A", "topic": "Session Manager Private Endpoints"},
    {"domain": "D3", "scenario": "Protect a public-facing Application Load Balancer from Layer 7 SQL injection and cross-site scripting (XSS) attacks.", "your_answer": "C", "result": "✅", "correct": "C", "topic": "AWS WAF SQLi and XSS Protection Rules"},
    {"domain": "D3", "scenario": "Deploy AWS Network Firewall to inspect all inbound and outbound traffic across multiple public/private subnets in a VPC.", "your_answer": "A", "result": "❌", "correct": "B", "topic": "AWS Network Firewall Topologies"},
    {"domain": "D3", "scenario": "Establish a Route 53 Resolver DNS Firewall rule to block DNS exfiltration queries to known malicious domains.", "your_answer": "B", "result": "✅", "correct": "B", "topic": "Route 53 DNS Firewall Domain Blocking"},
    {"domain": "D4", "scenario": "Implement an IAM Permission Boundary to restrict administrative role privilege escalation on member accounts.", "your_answer": "D", "result": "✅", "correct": "D", "topic": "IAM Permission Boundaries"},
    {"domain": "D4", "scenario": "Configure cross-account IAM role assumption with external ID to prevent the 'confused deputy' security issue.", "your_answer": "C", "result": "✅", "correct": "C", "topic": "Cross-Account IAM AssumeRole with ExternalID"},
    {"domain": "D4", "scenario": "Audit unused IAM credentials, access keys older than 90 days, and console passwords without MFA across the organization.", "your_answer": "A", "result": "⚠️", "correct": "D", "topic": "IAM Credential Report"},
    {"domain": "D4", "scenario": "Set up a resource-based IAM policy on an S3 bucket to enforce TLS-only connections and block HTTP access.", "your_answer": "B", "result": "✅", "correct": "B", "topic": "S3 Bucket Policy Secure Transport"},
    {"domain": "D5", "scenario": "Configure cross-account S3 bucket access where objects are encrypted with a Customer Managed KMS key in the source account.", "your_answer": "A", "result": "❌", "correct": "C", "topic": "Cross-Account KMS Key Grants"},
    {"domain": "D5", "scenario": "Enable S3 Object Lock in Compliance mode to protect backups from deletion or modification by any user, including root.", "your_answer": "D", "result": "✅", "correct": "D", "topic": "S3 Object Lock Compliance Mode"},
    {"domain": "D5", "scenario": "Configure automatic rotation of database credentials stored in AWS Secrets Manager every 30 days using a Lambda template.", "your_answer": "B", "result": "✅", "correct": "B", "topic": "Secrets Manager Credentials Rotation"},
    {"domain": "D5", "scenario": "Implement envelope encryption of large files locally using KMS GenerateDataKey and local AES encryption.", "your_answer": "A", "result": "✅", "correct": "A", "topic": "KMS Envelope Encryption and Data Keys"},
    {"domain": "D6", "scenario": "Implement AWS Organizations Service Control Policies (SCPs) to restrict regions where resources can be created.", "your_answer": "C", "result": "✅", "correct": "C", "topic": "Organizations SCPs Region Lock"},
    {"domain": "D6", "scenario": "Set up AWS Config to automatically monitor and alert when S3 buckets are public or EBS volumes are unencrypted.", "your_answer": "D", "result": "✅", "correct": "D", "topic": "AWS Config Managed Rules Compliance"},
    {"domain": "D6", "scenario": "Deploy AWS CloudFormation Guard rules in your CI/CD pipeline to scan templates for security policy violations before deployment.", "your_answer": "B", "result": "❌", "correct": "A", "topic": "CloudFormation Guard Infrastructure Scan"}
]

def get_next_session_num():
    if not TRACKER_PATH.exists():
        return 1
    text = TRACKER_PATH.read_text(encoding="utf-8")
    session_nums = [int(n) for n in re.findall(r"^### Session (\d+)", text, re.MULTILINE)]
    return max(session_nums) + 1 if session_nums else 1

def start_session(questions_count, domains=DEFAULT_DOMAINS, demo_mode=False, quiz_mode=False, blank_mode=False):
    next_num = get_next_session_num()
    today = date.today().strftime("%Y-%m-%d")
    
    # If neither demo_mode nor blank_mode is explicitly requested, default to quiz_mode
    if not demo_mode and not blank_mode:
        quiz_mode = True
        
    # Select question sets
    chosen_qs = []
    if demo_mode or quiz_mode:
        # Pull random samples from the demo pool with replacement if count > pool size
        chosen_qs = random.choices(DEMO_QUESTIONS, k=questions_count)
        
    if demo_mode:
        # Calculate summary scores for the demo session
        correct_count = sum(1 for q in chosen_qs if q["result"] == "✅")
        partial_count = sum(1 for q in chosen_qs if q["result"] == "⚠️")
        wrong_count = sum(1 for q in chosen_qs if q["result"] == "❌")
        pct = int((correct_count / len(chosen_qs)) * 100) if chosen_qs else 0
        score_str = f"{correct_count} ✅ · {partial_count} ⚠️ · {wrong_count} ❌ ({pct}% correct)"
    else:
        score_str = "0 ✅ · 0 ⚠️ · 0 ❌ (0% correct)"

    # Generate new session markdown block
    lines = [
        "",
        f"### Session {next_num} — {today}",
        "",
        f"**Domains:** {domains}",
        f"**Score:** {score_str}",
        "",
        "| # | Domain | Question / Scenario | Your Answer | Result | Correct Answer | Review Topic |",
        "|---|---|---|---|---|---|---|",
    ]
    
    # Generate rows
    for i in range(1, questions_count + 1):
        if demo_mode:
            q = chosen_qs[i - 1]
            lines.append(f"| {i} | {q['domain']} | {q['scenario']} | {q['your_answer']} | {q['result']} | {q['correct']} | {q['topic']} |")
        elif quiz_mode:
            q = chosen_qs[i - 1]
            lines.append(f"| {i} | {q['domain']} | {q['scenario']} | | ⬜ | {q['correct']} | {q['topic']} |")
        else:
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
    
    if demo_mode:
        mode_text = "Demo/Onboarding (Pre-answered)"
    elif quiz_mode:
        mode_text = "Interactive Quiz (Unanswered)"
    else:
        mode_text = "Blank"
    print(f"✅ Successfully appended {mode_text} Session {next_num} ({questions_count} questions) to question-tracker.md")
    return next_num

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a new empty or demo practice session/drill.")
    parser.add_argument("-q", "--questions", type=int, default=25, help="Number of questions in this drill (default: 25)")
    parser.add_argument("-d", "--domains", type=str, default=DEFAULT_DOMAINS, help="Domains covered in this drill")
    parser.add_argument("--demo", action="store_true", help="Run in Pre-Answered Demo Local mode (pre-loaded answers, perfect for quick stats review)")
    parser.add_argument("--blank", action="store_true", help="Generate a completely blank/empty session for manual external logging")
    parser.add_argument("--quiz", action="store_true", help="Generate an interactive quiz with realistic scenarios but blank answers (default)")
    args = parser.parse_args()
    
    try:
        # Default to quiz mode if no mode is selected
        demo_mode = args.demo
        blank_mode = args.blank
        quiz_mode = args.quiz or (not args.demo and not args.blank)
        
        start_session(args.questions, args.domains, demo_mode=demo_mode, quiz_mode=quiz_mode, blank_mode=blank_mode)
    except Exception as e:
        print(f"❌ Error starting session: {e}", file=sys.stderr)
        sys.exit(1)
