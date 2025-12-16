# Project Plan: LLM-Enhanced Distributed MCP Servers

## Project Goal
Implement a hybrid Large Language Model (LLM) system where a local LLM can boost and optimize provider LLMs, with both co-existing and running in parallel for an optimum developer experience. This core LLM integration will be preceded by a foundational wrapper phase, and subsequently followed by a suite of specialized Model Context Protocol (MCP) servers focusing on cloud-neutral context and document management to create robust, LLM-enhanced applications leveraging distributed capabilities.

## Assumptions
*   **Language:** Python
*   **MCP Definition:** Model Context Protocol (standardized specification for model capabilities/configuration).
*   **Core Focus:** Prioritize initial wrapper development, then hybrid LLM integration (local boosting provider), and foundational planning structures.
*   **Parallel Execution:** Local and provider LLMs, along with MCP servers, will be designed to run in parallel for optimal developer experience.
*   **Cloud Neutral Architecture:** The system will be designed to be cloud-neutral, avoiding vendor lock-in and allowing deployment across various cloud providers or on-premise environments.

## High-Level Roadmap

1.  **Foundational Setup & Project Structure:** Establish basic environment, core data models (including 'Plan' structures), and essential utilities.
2.  **Pre-LLM Wrapper Development:** Build the foundational wrapper that will eventually integrate with and manage LLMs.
3.  **Local LLM Integration:** Integrate local LLM models and fine-tune the wrapper for local boosting/optimization.
4.  **Provider LLM Integration:** Integrate external provider LLMs and enhance the wrapper for parallel execution and optimization.
5.  **MCP Foundational Elements:** Define MCP Data Models and the basic Server/Client Framework.
6.  **Document Management System:** Implement capabilities for scanning, analyzing, and indexing documents for LLM context.
7.  **Distributed MCP Server Development:** Develop specialized MCP servers focusing on cloud-neutral services.
8.  **Interactive Rules/Game Integration:** Implement interactive reasoning rules or game mechanics.
9.  **Hybrid LLM/MCP Orchestration & Refinement:** Orchestrate the hybrid LLM system with MCP servers, and refine the overall architecture.
10. **Testing & Optimization:** Comprehensive testing and performance optimization.

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
    *   **Status:** completed
    *   Based on the immediate need for the pre-LLM wrapper phase, define Python data models (e.g., using Pydantic) for core entities related to the wrapper's internal state, configuration, and its eventual interaction with a local LLM. This includes models for `WrapperConfig`, `LocalLLMConfig`, `ModelParameters`, `InferenceRequest`, and `InferenceResponse`.
*   **Task 1.3: Implement Generic Workspace Inventory (auto_register.py)**
    *   **Status:** completed
    *   Develop `workspace-automation/src/auto_register.py` to scan the project directory, respect `.gitignore`, and generate `file_registry.json` and `SYSTEM_INVENTORY.md`.
*   **Task 1.4: Implement Light Local Backup Script (simple_backup.sh)**
    *   **Status:** completed
    *   Develop `simple_backup.sh` to create timestamped copies of essential project files/directories in a local `backups/simple_copies` folder.
*   **Task 1.5: Implement Pre-Edit Backup Helper Script (pre_edit_backup.sh)**
    *   **Status:** completed
    *   Develop `pre_edit_backup.sh` to create timestamped copies of a file to `backups/pre_edit_snapshots` before it's edited.

### Phase 2: Pre-LLM Wrapper Development
**Status:** pending

*   **Task 2.1: Define Wrapper Architecture & Core Components:**
    *   **Status:** completed
    *   Design the high-level architecture for the wrapper that will eventually manage LLM interactions.
    *   Identify core components, interfaces, and data flows.
*   **Task 2.2: Implement Basic Wrapper Structure:**
    *   **Status:** completed
    *   Develop the initial Python classes and modules for the wrapper, focusing on its foundational structure without direct LLM integration yet.

### Phase 3: Local LLM Integration
**Status:** pending

*   **Task 3.1: Local LLM Environment Setup:**
    *   **Status:** pending
    *   Select and integrate a local LLM library (e.g., `ollama`, `llama-cpp-python`).
    *   Acquire and load a suitable tiny model.
*   **Task 3.2: Integrate Local LLM into Wrapper:**
    *   **Status:** pending
    *   Modify the wrapper to interact with the local LLM, enabling basic invocation and initial boosting/optimization strategies.

### Phase 4: Provider LLM Integration
**Status:** pending

*   **Task 4.1: Provider LLM Environment Setup:**
    *   **Status:** pending
    *   Choose and integrate with an external LLM provider (e.g., OpenAI, AWS Bedrock).
    *   Manage API calls, messages, and token usage.
*   **Task 4.2: Integrate Provider LLM into Wrapper:**
    *   **Status:** pending
    *   Enhance the wrapper to interact with the provider LLM, enabling parallel execution and further optimization strategies.
*   **Task 4.3: Develop Hybrid LLM Client:**
    *   **Status:** pending
    *   Create a generic Python class (`LLMClient`) to abstract and manage interactions with both local and provider LLMs, enabling boosting/optimization strategies and parallel execution.

### Phase 5: MCP Foundational Elements
**Status:** pending

*   **Task 5.1: Define MCP Data Models (Python using Pydantic) based on the Model Context Protocol specification**
    *   **Status:** pending
    *   Based on the Model Context Protocol specification, define Python data models (e.g., using Pydantic) for `ModelIdentification`, `ModelCapabilities`, `InferenceSettings`, `TokenizerDetails`, `RuntimeProperties`, and the overarching `ModelContext` object.
    *   This will establish the schema for how model information is communicated within the hybrid system.
*   **Task 5.2: Basic MCP Server/Client Framework (abstract base classes)**
    *   **Status:** pending
    *   Develop abstract Python classes for `MCPServer` and `MCPClient` that define the core interface for MCP interactions.
    *   Implement placeholder methods for `connect`, `cleanup`, `list_tools`, `call_tool`, etc., to guide future implementations.
*   **Task 5.3: Configuration Management for MCP servers (using .env and mcp.json)**
    *   **Status:** pending
    *   Implement a `Config` class to load settings from environment variables (e.g., from `.env`) and a dedicated `mcp.json` file for MCP-specific configurations (e.g., server addresses, model mappings).
    *   Ensure secure handling of sensitive information.

### Phase 6: Document Management System
**Status:** pending

*   **Task 6.1: Document Storage & Retrieval (e.g., Elasticsearch Integration)**
    *   **Status:** pending
    *   Set up and integrate with a document storage solution (e.g., Elasticsearch).
    *   Implement `ElasticsearchManager` for document indexing and retrieval.
*   **Task 6.2: Document Scanner & Parser:**
    *   **Status:** pending
    *   Develop `scan_documents()` functionality to ingest documents from various sources.
    *   Implement parsers for different document types.
*   **Task 6.3: Document Analysis Framework:**
    *   **Status:** pending
    *   Implement `analyze_documents()` to process document content.
    *   Develop `VectorDocument` structure for documents with embeddings (to be populated by LLM phase).

### Phase 7: Distributed MCP Server Development
**Status:** pending

*   **Task 7.1: Cloud-Neutral MCP Server for Generic Services:**
    *   **Status:** pending
    *   Develop an MCP server to expose capabilities for generic distributed services, not tied to a specific cloud provider.
*   **Task 7.2: Cloud-Specific MCP Server Examples (e.g., AWS, Azure, GCP):**
    *   **Status:** pending
    *   Develop example MCP servers for specific cloud services (e.g., AWS DocumentDB, Azure Cosmos DB, GCP Firestore), demonstrating cloud-neutral design principles.

### Phase 8: Interactive Rules/Game Integration
**Status:** pending

*   **Task 8.1: Implement Lateral Thinking Puzzle/Turtle Soup Game Rules:**
    *   **Status:** pending
    *   Develop `rules()` and `rules_solver()` functions to define the game mechanics.
    *   Focus on managing game state and player interactions (e.g., yes/no/irrelevant questions).

### Phase 9: Hybrid LLM/MCP Orchestration & Refinement
**Status:** pending

*   **Task 9.1: Hybrid LLM Orchestrator:**
    *   **Status:** pending
    *   Create a central `LLMOrchestrator` class responsible for intelligently routing requests between local and provider LLMs, applying boosting/optimization strategies.
    *   Manage parallel execution and selection criteria based on performance, cost, and specific task requirements.
*   **Task 9.2: MCP Registry/Discovery:**
    *   **Status:** pending
    *   Implement a mechanism for the orchestration layer to discover and register all available MCP servers (local and provider-based).
*   **Task 9.3: Cooperative Strategy Implementation:**
    *   **Status:** pending
    *   Define and implement strategies for "co-operative" behavior between LLMs and MCP servers, including chaining calls and parallel execution for enhanced capabilities.

### Phase 10: Testing & Optimization
**Status:** pending

*   **Task 10.1: Write Comprehensive Unit Tests:**
    *   **Status:** pending
    *   Develop unit tests for each class and function across the system.
*   **Task 10.2: Develop Integration Tests:**
    *   **Status:** pending
    *   Create integration tests to verify seamless interaction between components.
*   **Task 10.3: Perform Performance Benchmarking:**
    *   **Status:** pending
    *   Conduct benchmarking for all integrated components, with a focus on hybrid LLM performance.
*   **Task 10.4: Improve Error Handling & Robustness:**
    *   **Status:** pending
    *   Enhance error handling, logging, and implement robust failure recovery strategies.
