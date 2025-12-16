# Project Plan: AWS MCP Servers for Contextual LLM Enhancement

## Project Goal
Implement a suite of specialized Model Context Protocol (MCP) servers focusing on AWS-specific context and document management to enhance future LLM applications. LLM integration is a subsequent phase.

## Assumptions
*   **Language:** Python
*   **MCP Definition:** Model Context Protocol (standardized specification for model capabilities/configuration).
*   **Core Focus:** AWS services integration and efficient document management.
*   **Future Integration:** LLM orchestration and interaction will be integrated in a later phase.

## High-Level Roadmap

1.  **Foundational Setup & Core MCP Structures:** Establish the basic environment and core MCP structures.
2.  **Document Management System:** Implement capabilities for scanning, analyzing, and indexing documents.
3.  **AWS MCP Server Development:** Develop specialized MCP servers for AWS services (e.g., DocumentDB).
4.  **Interactive Rules/Game Integration:** Implement interactive reasoning rules or game mechanics.
5.  **Future LLM Integration:** Plan and integrate LLM functionality (e.g., hybrid LLM system, routing).
6.  **Refinement & Testing:** Optimize and thoroughly test the system.

## Detailed Plan & Todo List

The following tasks are organized into phases, reflecting the detailed steps required to achieve the project goal.

### Phase 1: Foundational Setup & Core MCP Structures
**Status:** in_progress

*   **Task 1.1: Project Setup & Virtual Environment**
    *   **Status:** completed
    *   Create project directory (already exists).
    *   Set up a Python virtual environment (using `uv venv`).
    *   Install core dependencies (`uv`, `pydantic` for config, `requests`, `httpx`).
*   **Task 1.2: Define MCP Data Models (Python using Pydantic) based on the Model Context Protocol specification**
    *   **Status:** pending
    *   Based on the Model Context Protocol specification, define Python data models (e.g., using Pydantic) for `ModelIdentification`, `ModelCapabilities`, `InferenceSettings`, `TokenizerDetails`, `RuntimeProperties`, and the overarching `ModelContext` object.
    *   This will establish the schema for how model information is communicated.
*   **Task 1.3: Basic MCP Server/Client Framework (abstract base classes)**
    *   **Status:** pending
    *   Develop abstract Python classes for `MCPServer` and `MCPClient` that define the core interface for MCP interactions.
    *   Implement placeholder methods for `connect`, `cleanup`, `list_tools`, `call_tool`, etc., to guide future implementations.
*   **Task 1.4: Configuration Management for MCP servers (using .env and mcp.json)**
    *   **Status:** pending
    *   Implement a `Config` class to load settings from environment variables (e.g., from `.env`) and a dedicated `mcp.json` file for MCP-specific configurations (e.g., server addresses, model mappings).
    *   Ensure secure handling of sensitive information.
*   **Task 1.5: Implement Generic Workspace Inventory (auto_register.py)**
    *   **Status:** completed
    *   Develop `workspace-automation/src/auto_register.py` to scan the project directory, respect `.gitignore`, and generate `file_registry.json` and `SYSTEM_INVENTORY.md`.
*   **Task 1.6: Implement Light Local Backup Script (simple_backup.sh)**
    *   **Status:** completed
    *   Develop `simple_backup.sh` to create timestamped copies of essential project files/directories in a local `backups/simple_copies` folder.

### Phase 2: Document Management System
**Status:** pending

*   **Task 2.1: Document Storage & Retrieval (e.g., Elasticsearch Integration)**
    *   **Status:** pending
    *   Set up and integrate with a document storage solution (e.g., Elasticsearch).
    *   Implement `ElasticsearchManager` for document indexing and retrieval.
*   **Task 2.2: Document Scanner & Parser:**
    *   **Status:** pending
    *   Develop `scan_documents()` functionality to ingest documents from various sources.
    *   Implement parsers for different document types.
*   **Task 2.3: Document Analysis Framework:**
    *   **Status:** pending
    *   Implement `analyze_documents()` to process document content.
    *   Develop `VectorDocument` structure for documents with embeddings (to be populated in future LLM phase).

### Phase 3: AWS MCP Server Development
**Status:** pending

*   **Task 3.1: AWS DocumentDB MCP Server:**
    *   **Status:** pending
    *   Develop an MCP server specifically for Amazon DocumentDB.
    *   Implement tools for connection management, database operations, collection management, and document CRUD operations within DocumentDB.
*   **Task 3.2: AWS Cloud Control API Resources MCP Server:**
    *   **Status:** pending
    *   Develop an MCP server to list and manage resources via the AWS Cloud Control API (`awscc`).
    *   Expose capabilities to interact with various AWS services through this API.

### Phase 4: Interactive Rules/Game Integration
**Status:** pending

*   **Task 4.1: Implement Lateral Thinking Puzzle/Turtle Soup Game Rules:**
    *   **Status:** pending
    *   Develop `rules()` and `rules_solver()` functions to define the game mechanics.
    *   Focus on managing game state and player interactions (e.g., yes/no/irrelevant questions).

### Phase 5: Future LLM Integration
**Status:** pending

*   **Task 5.1: Local LLM Environment Setup:**
    *   **Status:** pending
    *   Select and integrate a local LLM library.
    *   Acquire and load a suitable tiny model.
*   **Task 5.2: Provider LLM Integration:**
    *   **Status:** pending
    *   Choose and integrate with an external LLM provider (e.g., OpenAI, AWS Bedrock).
    *   Manage API calls, messages, and token usage.
*   **Task 5.3: MCP Orchestration & Routing:**
    *   **Status:** pending
    *   Implement logic to intelligently choose and interact with LLMs based on requests and criteria.

### Phase 6: Refinement & Testing
**Status:** pending

*   **Task 6.1: Write Comprehensive Unit Tests:**
    *   **Status:** pending
    *   Develop unit tests for all components across the system.
*   **Task 6.2: Develop Integration Tests:**
    *   **Status:** pending
    *   Create integration tests to verify seamless interaction between components.
*   **Task 6.3: Perform Performance Benchmarking:**
    *   **Status:** pending
    *   Conduct benchmarking for all integrated components.
*   **Task 6.4: Improve Error Handling & Robustness:**
    *   **Status:** pending
    *   Enhance error handling, logging, and implement robust failure recovery strategies.
