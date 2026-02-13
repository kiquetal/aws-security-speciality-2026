# Workflow Rules

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
