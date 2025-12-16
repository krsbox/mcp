# Error Registry

This document tracks significant errors and issues encountered during the project development, along with their context, resolution, and impact.

## Identified Issues

### Issue ID: ERR-001
*   **Issue:** `python3 -m venv` failed due to `ensurepip` not being available.
*   **Context:** Initial attempt to create a Python virtual environment for the project.
*   **Resolution:** Switched to using `uv venv` as per user instruction, which successfully created the virtual environment without relying on `ensurepip`.
*   **Impact:** Required user intervention and a change in the virtual environment creation strategy. Highlighted a system-level dependency (`python3-venv` package) that was not installed.

### Issue ID: ERR-002
*   **Issue:** `pip install uv` step in GitHub Actions CI workflow conflicted with user's environment constraint ("pip is not installed as a safety measure").
*   **Context:** The `python-ci.yml` workflow initially included a step to install `uv` using `pip`.
*   **Resolution:** Modified `python-ci.yml` to remove the `uv` installation step entirely, assuming `uv` is manually installed and available in the GitHub Actions runner's PATH.
*   **Impact:** Required an adjustment to the CI workflow to respect environment-specific constraints regarding `pip` usage. Ensured consistency with the user's preferred tool setup.

### Issue ID: ERR-003
*   **Issue:** `git push` permissions denied to `awslabs/mcp`.
*   **Context:** Initial attempt to push committed changes to the `awslabs/mcp` remote repository.
*   **Resolution:** Explained that the `krsbox` user (and associated PAT) lacked write permissions to the `awslabs/mcp` repository. The user subsequently provided a valid remote URL to `krsbox/mcp.git`.
*   **Impact:** Clarified ownership and write permissions requirements for the target Git repository. Prevented pushing sensitive changes to an unauthorized public repository.

### Issue ID: ERR-004
*   **Issue:** `git push` failed with "Repository not found" for `https://github.com/krsbox/mcp`.
*   **Context:** Attempt to push to `https://github.com/krsbox/mcp.git` after changing the remote URL.
*   **Resolution:** Explained that the repository `krsbox/mcp.git` did not exist on GitHub. The user was instructed to create an empty public or private repository, which they then did, providing the correct URL `https://github.com/krsbox/mcp.git` (which then worked via HTTPS).
*   **Impact:** Confirmed the necessity of creating the GitHub repository before attempting to push to it. Clarified the process for setting up a new remote repository.
