# Development Task Checklist

This checklist outlines the standard steps for executing any development task within this project, ensuring consistency, quality, and thoroughness.

## Phase 1: Understanding and Planning

*   [ ] **Understand the Request:**
    *   Clearly comprehend the user's objective and specific requirements.
    *   Identify any ambiguities and seek clarification.
*   [ ] **Contextual Analysis:**
    *   Investigate relevant codebase areas, existing files, dependencies, and project conventions.
    *   Utilize `codebase_investigator` for complex analysis or `search_file_content`/`glob` for targeted searches.
*   [ ] **Formulate a Plan:**
    *   Outline a clear, coherent, and grounded approach to address the request.
    *   Break down complex tasks into smaller, manageable subtasks.
    *   Use the `write_todos` tool to track progress on subtasks.
*   [ ] **Identify Testing Strategy:**
    *   Determine how to verify the changes, including unit, integration, or end-to-end tests.
    *   Plan for new tests if necessary, or identify existing tests to modify/run.

## Phase 2: Implementation

*   [ ] **Adhere to Conventions:**
    *   Strictly follow existing project style, formatting, naming, and architectural patterns.
    *   Mimic surrounding code for idiomatic changes.
*   [ ] **Implement Changes:**
    *   Use appropriate tools (`replace`, `write_file`, `run_shell_command`) to make the planned modifications.
    *   Add comments sparingly, focusing on *why* complex logic exists.

## Phase 3: Verification and Finalization

*   [ ] **Run Tests:**
    *   Execute all identified relevant tests (unit, integration, etc.).
    *   Ensure all tests pass and no regressions are introduced.
*   [ ] **Check Standards (Linting, Type-checking, Build):**
    *   Run project-specific linting tools (e.g., `ruff check .`, `npm run lint`).
    *   Perform type-checking (e.g., `tsc`).
    *   Execute build commands to ensure the project compiles successfully.
*   [ ] **Review Changes (Self-review):**
    *   Carefully review all modifications, new code, and deleted code.
    *   Ensure the changes directly address the request and maintain code quality.
*   [ ] **Commit Changes:**
    *   Create clear, concise, and descriptive commit messages.
    *   Ensure all relevant files are staged and committed.

## Phase 4: Post-Completion

*   [ ] **Document (if necessary):**
    *   Update project documentation (`PLAN.md`, `ERROR_REGISTRY.md`, `CHANGELOG.md`) as appropriate.
*   [ ] **Awaiting Next Instruction:**
    *   Confirm completion and await further user input.
