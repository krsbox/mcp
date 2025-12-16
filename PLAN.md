# Project Plan: LLM-Enhanced AWS MCP Servers

## Project Goal
Implement a core Large Language Model (LLM) integration, followed by a suite of specialized Model Context Protocol (MCP) servers focusing on AWS-specific context and document management. The aim is to create LLM-enhanced applications leveraging AWS capabilities.

## Assumptions
*   **Language:** Python
*   **MCP Definition:** Model Context Protocol (standardized specification for model capabilities/configuration).
*   **Core Focus:** Prioritize initial LLM integration and foundational planning structures.
*   **AWS Services Integration:** AWS services will be integrated to enhance LLM capabilities via MCP.

## High-Level Roadmap

1.  **Foundational Setup & Project Structure:** Establish basic environment, core data models (including 'Plan' structures), and essential utilities.
2.  **Core LLM Integration:** Implement initial local and provider-based LLM functionality.
3.  **Document Management System:** Implement capabilities for scanning, analyzing, and indexing documents for LLM context.
4.  **AWS MCP Server Development:** Develop specialized MCP servers for AWS services.
5.  **Interactive Rules/Game Integration:** Implement interactive reasoning rules or game mechanics.
6.  **MCP Orchestration & Refinement:** Orchestrate MCP servers and LLMs, and refine the overall system.
7.  **Testing & Optimization:** Comprehensive testing and performance optimization.

## Detailed Plan & Todo List

The following tasks are organized into phases, reflecting the detailed steps required to achieve the project goal.

### Phase 1: Foundational Setup & Project Structure
**Status:** in_progress

*   **Task 1.1: Project Setup & Virtual Environment**
    *   **Status:** completed
    *   Create project directory (already exists).
    *   Set up a Python virtual environment (using `uv venv`).
    *   Install core dependencies (`uv`, `pydantic` for config, `requests`, `httpx`).
*   **Task 1.2: Define Core Project Data Models (Python using Pydantic)**
    *   **Status:** pending
    *   Based on project needs and potential future "Plan" concepts, define Python data models (e.g., using Pydantic) for core entities such as `Plan`, `PlanStep`, `ProjectConfiguration`, and potentially foundational MCP-agnostic components.
*   **Task 1.3: Implement Generic Workspace Inventory (auto_register.py)**
    *   **Status:** completed
    *   Develop `workspace-automation/src/auto_register.py` to scan the project directory, respect `.gitignore`, and generate `file_registry.json` and `SYSTEM_INVENTORY.md`.
*   **Task 1.4: Implement Light Local Backup Script (simple_backup.sh)**
    *   **Status:** completed
    *   Develop `simple_backup.sh` to create timestamped copies of essential project files/directories in a local `backups/simple_copies` folder.
*   **Task 1.5: Implement Pre-Edit Backup Helper Script (pre_edit_backup.sh)**
    *   **Status:** completed
    *   Develop `pre_edit_backup.sh` to create timestamped copies of a file to `backups/pre_edit_snapshots` before it's edited.

### Phase 2: Core LLM Integration
**Status:** pending

*   **Task 2.1: Local LLM Environment Setup:**
    *   **Status:** pending
    *   Select and integrate a local LLM library.
    *   Acquire and load a suitable tiny model.
*   **Task 2.2: Provider LLM Integration:**
    *   **Status:** pending
    *   Choose and integrate with an external LLM provider (e.g., OpenAI, AWS Bedrock).
    *   Manage API calls, messages, and token usage.
*   **Task 2.3: Basic LLM Wrapper/Client:**
    *   **Status:** pending
    *   Create a generic Python class (`LLMClient`) to abstract LLM interactions for both local and provider models.

### Phase 3: Document Management System
**Status:** pending

*   **Task 3.1: Document Storage & Retrieval (e.g., Elasticsearch Integration)**
    *   **Status:** pending
    *   Set up and integrate with a document storage solution (e.g., Elasticsearch).
    *   Implement `ElasticsearchManager` for document indexing and retrieval.
*   **Task 3.2: Document Scanner & Parser:**
    *   **Status:** pending
    *   Develop `scan_documents()` functionality to ingest documents from various sources.
    *   Implement parsers for different document types.
*   **Task 3.3: Document Analysis Framework:**
    *   **Status:** pending
    *   Implement `analyze_documents()` to process document content.
    *   Develop `VectorDocument` structure for documents with embeddings (to be populated by LLM phase).

### Phase 4: AWS MCP Server Development
**Status:** pending

*   **Task 4.1: Define MCP Data Models (Python using Pydantic) based on the Model Context Protocol specification**
    *   **Status:** pending
    *   Based on the Model Context Protocol specification, define Python data models (e.g., using Pydantic) for `ModelIdentification`, `ModelCapabilities`, `InferenceSettings`, `TokenizerDetails`, `RuntimeProperties`, and the overarching `ModelContext` object.
    *   This will establish the schema for how model information is communicated.
*   **Task 4.2: Basic MCP Server/Client Framework (abstract base classes)**
    *   **Status:** pending
    *   Develop abstract Python classes for `MCPServer` and `MCPClient` that define the core interface for MCP interactions.
    *   Implement placeholder methods for `connect`, `cleanup`, `list_tools`, `call_tool`, etc., to guide future implementations.
*   **Task 4.3: Configuration Management for MCP servers (using .env and mcp.json)**
    *   **Status:** pending
    *   Implement a `Config` class to load settings from environment variables (e.g., from `.env`) and a dedicated `mcp.json` file for MCP-specific configurations (e.g., server addresses, model mappings).
    *   Ensure secure handling of sensitive information.
*   **Task 4.4: AWS DocumentDB MCP Server:**
    *   **Status:** pending
    *   Develop an MCP server specifically for Amazon DocumentDB.
    *   Implement tools for connection management, database operations, collection management, and document CRUD operations within DocumentDB.
*   **Task 4.5: AWS Cloud Control API Resources MCP Server:**
    *   **Status:** pending
    *   Develop an MCP server to list and manage resources via the AWS Cloud Control API (`awscc`).
    *   Expose capabilities to interact with various AWS services through this API.

### Phase 5: Interactive Rules/Game Integration
**Status:** pending

*   **Task 5.1: Implement Lateral Thinking Puzzle/Turtle Soup Game Rules:**
    *   **Status:** pending
    *   Develop `rules()` and `rules_solver()` functions to define the game mechanics.
    *   Focus on managing game state and player interactions (e.g., yes/no/irrelevant questions).

### Phase 6: MCP Orchestration & Refinement
**Status:** pending

*   **Task 6.1: MCP Registry/Discovery (discover and register MCP servers)**
    *   **Status:** pending
    *   Implement a mechanism for the orchestration layer to discover and register all available MCP servers (local and provider-based). This could be static (via `mcp.json`) or dynamic.
*   **Task 6.2: Orchestration Logic (analyze requests, select optimal LLM based on criteria)**
    *   **Status:** pending
    *   Create a central `LLMOrchestrator` class responsible for intelligent routing.
    *   Implement logic to analyze incoming user requests and, based on defined criteria (cost, latency, specific model features from `ModelContext`, local preference), select the most suitable LLM.
    *   Route the request via the chosen LLM's MCP interface.
*   **Task 6.3: Cooperative Strategy Implementation (define and implement chaining/routing logic)**
    *   **Status:** pending
    *   Define and implement strategies for "co-operative" behavior between LLMs. This might involve chaining calls (e.g., local LLM for initial draft, provider LLM for refinement) or parallel execution for comparative analysis.

### Phase 7: Testing & Optimization
**Status:** pending

*   **Task 7.1: Write Comprehensive Unit Tests:**
    *   **Status:** pending
    *   Develop unit tests for each class and function across the system.
*   **Task 7.2: Develop Integration Tests:**
    *   **Status:** pending
    *   Create integration tests to verify seamless interaction between components.
*   **Task 7.3: Perform Performance Benchmarking:**
    *   **Status:** pending
    *   Conduct benchmarking for all integrated components.
*   **Task 7.4: Improve Error Handling & Robustness:**
    *   **Status:** pending
    *   Enhance error handling, logging, and implement robust failure recovery strategies.