---
name: Pull Request
about: Propose changes to the project
title: "[TYPE]: Short Description"
labels: ''
assignees: ''

---

## Description

Please provide a concise description of the changes in this Pull Request.

Fixes # (issue)

## Code Review Checklist

This checklist is based on `CHECKLIST_CODE_REVIEW.md` and provides a structured approach for conducting code reviews, aiming to improve code quality, maintain consistency, and ensure best practices are followed across the project.

### General Checks

*   [ ] **Purpose & Scope:** Does the code correctly implement the intended feature or fix the bug described? Is the scope appropriate, or does it try to do too much?
*   [ ] **Readability & Clarity:**
    *   [ ] Is the code easy to understand? Are variable, function, and class names clear and descriptive?
    *   [ ] Are comments clear, concise, and explain *why* something is done (not just *what*)? Are there any unnecessary comments?
    *   [ ] Is the code well-formatted and consistent with project style guidelines (indentation, spacing, line breaks)?
*   [ ] **Adherence to Conventions:**
    *   [ ] Does the code follow the project's coding standards, style guides, and architectural patterns? (Refer to `DESIGN_GUIDELINES.md` and `CONTRIBUTING.md`).
    *   [ ] Are framework-specific idioms used correctly?

### Functionality & Logic

*   [ ] **Correctness:** Does the code behave as expected under various conditions (happy path, edge cases, error conditions)?
*   [ ] **Completeness:** Are all requirements of the task addressed? Are there any missing pieces?
*   [ ] **Error Handling:** Is error handling robust? Are errors logged appropriately? Are exceptions handled gracefully?
*   [ ] **Security:** Are there any obvious security vulnerabilities (e.g., injection flaws, improper data validation, sensitive data exposure)?
*   [ ] **Efficiency:** Is the code reasonably efficient? Are there any obvious performance bottlenecks?

### Testing

*   [ ] **Unit Tests:** Are new/modified unit tests present and do they adequately cover the changes? Do they pass?
*   [ ] **Integration/E2E Tests:** If applicable, are integration or end-to-end tests updated or added? Do they pass?
*   [ ] **Test Quality:** Are tests clear, maintainable, and effective? Do they test edge cases?

### Documentation & Maintainability

*   [ ] **Documentation Updates:** Is internal documentation (code comments, READMEs) updated to reflect changes?
*   [ ] **API Changes:** If APIs are affected, is the documentation (if any) updated?
*   [ ] **Maintainability:** Is the code designed in a way that makes it easy to maintain, debug, and extend in the future?
*   [ ] **Dependencies:** Are new dependencies necessary? If so, are they justified and correctly added?

### Before Approval

*   [ ] **Build & Lint Checks:** Have all automated build, linting, and type-checking steps passed successfully?
*   [ ] **No Unnecessary Changes:** Are there any unrelated changes, commented-out code, or temporary debugging statements that should be removed?
*   [ ] **No Credentials/Sensitive Info:** Are there any hardcoded credentials or sensitive information?
