# Tasks: orchestrator-setup-repos

## 1. Directory Setup & Repository Workspace

- [x] 1.1 Create the `.ai/repositories/` directory structure and root symlink `.repositories/`
- [x] 1.2 Update `.gitignore` to ensure linked repositories in `.ai/repositories/` and `.repositories/` are excluded from tracking

## 2. Safety & Validation Logic

- [x] 2.1 Implement symlink path validation script to prevent recursive directory traversal loops below repo root
- [x] 2.2 Implement Git `index.lock` check utility to gracefully halt operations if target repository is locked by external processes

## 3. Git Agent Skill & Enforcement

- [x] 3.1 Create `git-agent` skill definition with explicit instruction for managing feature branches and Pull Requests
- [x] 3.2 Implement Push Policy guardrails in `git-agent` to block direct commits to `main`/`master` branches
- [x] 3.3 Add CLI integration for automated branch creation, committing, and Pull Request generation (`gh pr create`)

