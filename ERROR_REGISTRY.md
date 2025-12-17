# Error Registry

This document tracks significant errors and issues encountered during the project development, along with their context, resolution, and impact. This registry is specifically for documenting *problems* and their resolutions, distinct from the `AGENT_LOG.md` which records *all significant actions* taken by the agent.

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

### Issue ID: ERR-005
*   **Issue:** `backups/` directory manually added to `.gitignore`.
*   **Context:** While performing git status after updating `GEMINI.md`, it was observed that `backups/` was added to `.gitignore`. This change was not initiated by the agent.
*   **Resolution:** The change was accepted as it is a reasonable addition to `.gitignore` for development practices related to project growth and backup management. No further action required from the agent regarding this specific entry.
*   **Impact:** Minor. Ensures backup directories are not tracked by Git, which is a common and recommended practice.

### Issue ID: ERR-006
*   **Issue:** Manual error during editing led to unintended conversational text being included in `GEMINI.md`.
*   **Context:** User was editing `GEMINI.md` and accidentally introduced extraneous conversational text. The user subsequently corrected the file.
*   **Resolution:** User manually corrected the `GEMINI.md` file, removing the unintended content.
*   **Impact:** Minor, as the error was promptly identified and corrected by the user. Reinforces the importance of careful manual editing of critical project documentation.

### Issue ID: ERR-007
*   **Issue:** Failure to execute `git-changelog` via `uv run`.
*   **Context:** After installing `git-changelog` via `uv pip install git-changelog` and attempting to run it using `uv run git-changelog` (and `uv run python -m git_changelog`), the command initially failed with "No such file or directory" or "No module named".
*   **Resolution:** Reinstalling `git-changelog` using `uv pip install git-changelog` resolved the issue, allowing `uv run git-changelog --output CHANGELOG.md` to execute successfully. This highlighted intricacies in `uv`'s environment management and executable paths.
*   **Impact:** Temporarily delayed the initial generation of `CHANGELOG.md` and required troubleshooting of `uv` command invocation.

### Issue ID: ERR-008
*   **Issue:** Bandit SAST tool removed from CI due to reported system overhead.
*   **Context:** Bandit was integrated into `python-ci.yml` for security scanning. However, the user reported concerns about the system overhead introduced by the scan, especially for an LLM project.
*   **Resolution:** The Bandit scan step and its dependency (`bandit`) were removed from the CI workflow (`python-ci.yml`) and `requirements.txt` respectively, to reduce CI overhead.
*   **Impact:** Automated SAST is currently not performed in CI, increasing reliance on manual security review. This highlights a need to re-evaluate lighter security scanning alternatives in the future that align with the project's performance requirements.

### Issue ID: ERR-009
*   **Issue:** Markdown linter (`markdownlint-cli`) implementation deferred due to system overhead concerns and prioritization of light backup options.
*   **Context:** Integration of `markdownlint-cli` into CI for documentation quality was proposed. However, the user expressed concerns over system overhead for LLM projects and prioritized implementing lighter backup options, leading to the deferral of this implementation.
*   **Resolution:** Implementation of `markdownlint-cli` and related configuration deferred.
*   **Impact:** Lack of automated documentation formatting and spell checking in CI. Requires manual checks for documentation quality. This highlights a need to re-evaluate lighter or Python-native alternatives for documentation linting in the future.

### Issue ID: ERR-010
*   **Issue:** Agent oversight: Failed to commit code immediately after marking a task as completed in `PLAN.md`.
*   **Context:** After completing the documentation update for `PLAN.md` (marking Task 1.2 as completed), the agent failed to commit the associated code changes (`src/data_models/`). This led to a discrepancy between `PLAN.md`'s status and the actual committed codebase state.
*   **Resolution:** The missing code was subsequently committed in a separate action. The agent will enhance its internal process to ensure code changes and corresponding documentation updates (like `PLAN.md` status changes) are committed synchronously, or at least that any pending code commits are highlighted immediately.
*   **Impact:** Minor delay in development process due to necessary corrective action. Highlighted a need for stricter internal adherence to change management protocols for the agent.

### Issue ID: ERR-011
*   **Issue:** Clarification on unified backup strategy: Initial misunderstanding regarding the deprecation of `simple_backup.sh`.
*   **Context:** The agent initially deprecated `simple_backup.sh` assuming a "pre-edit only" backup strategy. User clarified that both `pre_edit_backup.sh` and `simple_backup.sh` functionalities are valued and should be part of the unified backup.
*   **Resolution:** Re-evaluation of the unified backup strategy to incorporate both `pre_edit_backup.sh` for individual file snapshots and `simple_backup.sh` for periodic project snapshots. `simple_backup.sh` functionality is reinstated.
*   **Impact:** The "Unified Backup Orchestration" design (Task 11.1) now explicitly includes both backup methods as an interim strategy. This ensures comprehensive protection for both granular file edits and broader project documents/configuration.