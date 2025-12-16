# Contributing Guidelines

We welcome contributions to the "AWS MCP Servers" project! By following these guidelines, you help us maintain code quality, consistency, and a smooth development workflow.

## How to Contribute

1.  **Fork the Repository:** Start by forking the `awslab/mcp` repository to your GitHub account.
2.  **Clone Your Fork:** Clone your forked repository to your local machine:
    ```bash
    git clone https://github.com/YOUR_USERNAME/mcp.git
    cd mcp
    ```
3.  **Create a New Branch:** Always create a new branch for your work. Use a descriptive name (e.g., `feature/add-documentdb-server`, `fix/login-bug`).
    ```bash
    git checkout -b feature/your-feature-name
    ```
4.  **Make Your Changes:** Implement your feature or bug fix.
    *   Adhere to the project's coding style and conventions (refer to `CHECKLIST_DEVELOPMENT.md`).
    *   Write clear, concise code.
    *   Add tests for new functionality or bug fixes.
    *   Ensure all existing tests pass.
    *   Run linting and type-checking (`uv run ruff check .`, `uv run mypy .`).
5.  **Write Meaningful Commit Messages:** Follow the Conventional Commits specification (detailed below).
6.  **Push Your Branch:** Push your changes to your fork:
    ```bash
    git push origin feature/your-feature-name
    ```
7.  **Create a Pull Request:**
    *   Go to the original `awslab/mcp` repository on GitHub.
    *   Open a new Pull Request from your branch to the `main` branch.
    *   Fill out the Pull Request template (refer to `.github/PULL_REQUEST_TEMPLATE.md`).
    *   Ensure all CI checks pass.
    *   Address any feedback from reviewers.

## Conventional Commits

We follow the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) specification for all commit messages. This helps us generate consistent changelogs, understand the nature of changes at a glance, and automate versioning.

A commit message should be structured as follows:

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

### Type

The `type` is a mandatory keyword that describes the kind of change this commit is introducing. Common types include:

*   **`feat`**: A new feature
*   **`fix`**: A bug fix
*   **`docs`**: Documentation only changes
*   **`style`**: Changes that do not affect the meaning of the code (white-space, formatting, missing semicolons, etc.)
*   **`refactor`**: A code change that neither fixes a bug nor adds a feature
*   **`perf`**: A code change that improves performance
*   **`test`**: Adding missing tests or correcting existing tests
*   **`build`**: Changes that affect the build system or external dependencies (e.g., `uv`, `pip`)
*   **`ci`**: Changes to our CI configuration files and scripts (e.g., GitHub Actions)
*   **`chore`**: Other changes that don't modify src or test files
*   **`revert`**: Reverts a previous commit

### Scope (Optional)

The `scope` provides additional contextual information about the change. It is enclosed in parentheses and placed after the `type`.
Examples: `feat(parser)`, `fix(api)`, `docs(readme)`.

### Description

The `description` is a concise, imperative statement of the change. It should:

*   Be a short, one-line summary.
*   Use the imperative mood ("add", "change", "fix") rather than past tense ("added", "changed", "fixed").
*   Not be capitalized.
*   Not end with a period.

### Body (Optional)

The `body` provides more detailed contextual information about the change. It should start one blank line after the description.

### Footer (Optional)

The `footer` can contain information about breaking changes or reference issues.

*   **Breaking Changes:** Indicate breaking changes with `BREAKING CHANGE:`.
*   **Referencing Issues:** Use `Closes #123`, `Refs #456`, `Fixes #789` to link to issue trackers.

### Examples

*   `feat(authentication): add user login feature`
*   `fix(bug): correct invalid input validation`
*   `docs: update README with installation instructions`
*   `ci: add dependabot configuration`
*   `chore(deps): update requests to v2.30.0`
*   `refactor(auth): simplify token generation logic`

## Security Issue Notifications

If you discover a security vulnerability, please report it responsibly by contacting [maintainer-email@example.com] instead of opening a public issue. This allows us to address the issue privately before a public disclosure.

---
