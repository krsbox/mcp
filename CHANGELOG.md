# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Initial `CHANGELOG.md` file for tracking project evolution.
- New documentation files: `CHECKLIST_DEVELOPMENT.md`, `CHECKLIST_CODE_REVIEW.md`, `CHECKLIST_PROJECT_GROWTH.md`.
- GitHub Pull Request template: `PULL_REQUEST_TEMPLATE.md`.
- Infrastructure for automated system inventory updates (directory `workspace-automation/src/`, placeholder script `auto_register.py`, and GitHub Actions workflow `auto-inventory.yml`).

### Changed
- `GEMINI.md`: Updated to reference the newly added documentation files (`CHANGELOG.md`, checklists).
- `.github/workflows/python-ci.yml`: Added `ruff format --check` step for code style consistency.
- `.gitignore`: Added `backups/` entry (manually added, then committed by agent).

### Fixed
- `CHECKLIST_CODE_REVIEW.md`: Reverted accidental conversational text added to the file.

### Docs
- `ERROR_REGISTRY.md`: Added `ERR-005` entry regarding manual `.gitignore` modification.
