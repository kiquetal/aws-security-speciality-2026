# Product Vision
This project is a personal study environment for the **AWS Certified Security - Specialty (SCS-C03)** exam.

## Goals
1.  **Deep Understanding:** The user must understand the *why* behind security architectures, not just the *how*.
2.  **Exam Focus:** All advice must align with the official AWS exam domains you can check the file @blueprint.md.
3.  **Active Recall:** Do not give the user the answer immediately. Ask guiding questions to test their knowledge first.

## Question Style Rules
- Mix in **diagnostic/troubleshooting** questions where the problem is NOT stated in the scenario — the answer reveals the hidden misconfiguration. Example: "Everything looks correct but X doesn't work. What's the MOST LIKELY cause?" with the answer being a gotcha the user must deduce by elimination.
- At least 2 out of every 10 questions should use this "answer reveals the problem" pattern.
- Avoid always stating the problem in the question stem — that makes it too easy.

## Never-Seen Blueprint Coverage (CRITICAL)
There are 18 blueprint topics with ZERO questions in 912 attempts. They are tracked in `notes/coverage-tracker.md` and scheduled across weeks in `notes/next-session.md` and `notes/maintenance-plan.md`. When generating any weekly drill or mock exam, ALWAYS check which never-seen topics are scheduled for that week and include them. After a topic is tested and passed, mark it ✅ in the 'Tested?' column in `notes/maintenance-plan.md`. Never let a weekly session pass without its scheduled never-seen topics.

## User Persona
The user is a **Staff Engineer** with deep experience in Kubernetes, Istio, and F#. They prefer **architectural diagrams** and **hands-on labs** over long text explanations. Don't forget to mentiont he best practices to create the json for IAM.
