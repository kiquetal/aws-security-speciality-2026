# Workflow Rules

## Branch Policy
- **ALWAYS** work on the `main` branch. Never checkout, commit to, or push to any other branch.
- Before any git operation, verify you are on `main`: `git checkout main` if not.
- Push ONLY to `origin main`. Never push to `onboarding` or any other branch.

## Git Commit Policy
- **ALWAYS** wait for explicit user approval before executing any `git commit` command.
- When changes are ready to commit:
  1. Show the `git diff` output
  2. Propose a commit message following conventional commits format
  3. Wait for user confirmation (yes/no/modify)
  4. Only execute the commit after receiving approval

## Commit Message Format
Follow conventional commits:
- `feat:` for new features
- `fix:` for bug fixes
- `docs:` for documentation changes
- `refactor:` for code refactoring
- `test:` for test additions/changes
- `chore:` for maintenance tasks

## Question Generation — ZERO REPEAT ENFORCEMENT

**This is the #1 priority rule. It overrides all other question generation logic.**

Before generating ANY question:
1. **READ `notes/maintenance-plan.md` "Mastered Patterns" table FIRST.** This is mandatory.
2. **NEVER use pre-written questions from `notes/next-session.md`.** Those are stale. Always generate fresh at drill time.
3. For each question you plan to generate, verify the sub-pattern has < 3 correct attempts in the tracker.
4. If a sub-pattern appears in the mastered list → SKIP IT. Find a novel angle or different topic entirely.
5. Pre-written question banks become stale the moment the user masters a pattern. Treat `next-session.md` as TOPIC GUIDANCE ONLY, never as a question source.

**Violation of this rule = wasting limited study time. The user has explicitly flagged this as frustrating.**
