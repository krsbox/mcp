# Project Plan: Hybrid LLM System with MCP Orchestration

## Project Goal
Implement a hybrid LLM system combining local and provider-based LLMs, orchestrated via the Model Context Protocol (MCP), to intelligently route requests based on various factors.

## Assumptions
*   **Language:** Python
*   **MCP Definition:** Model Context Protocol (standardized specification for model capabilities/configuration).
*   **Local LLM:** Tiny models for efficiency and resource constraints.
*   **Provider LLM:** External APIs (e.g., OpenAI, AWS Bedrock).

## High-Level Roadmap

1.  **Foundational Setup:** Establish the basic environment and core MCP structures.
2.  **Local LLM Integration:** Implement and integrate a local LLM.
3.  **Provider LLM Integration:** Implement and integrate at least one provider LLM.
4.  **MCP Orchestration & Routing:** Build the logic to intelligently choose and interact with LLMs.
5.  **Refinement & Testing:** Optimize and thoroughly test the system.

## Detailed Plan & Todo List

The following tasks are organized into phases, reflecting the detailed steps required to achieve the project goal.

### Phase 1: Foundational Setup & Core MCP Structures
**Status:** pending

*   **Task 1.1: Project Setup & Virtual Environment**
    *   **Status:** in_progress
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
*   **Task 1.4: Configuration Management for LLMs and MCP servers (using .env and mcp.json)**
    *   **Status:** pending
    *   Implement a `Config` class to load settings from environment variables (e.g., from `.env`) and a dedicated `mcp.json` file for MCP-specific configurations (e.g., server addresses, model mappings).
    *   Ensure secure handling of sensitive information.

### Phase 2: Local LLM Integration
**Status:** pending

*   **Task 2.1: Local LLM Environment Setup (choose library, install, acquire tiny model)**
    *   **Status:** pending
    *   Select a local LLM library (e.g., `ollama`, `llama-cpp-python`).
    *   Install the chosen library and its dependencies within the virtual environment.
    *   Acquire a suitable "tiny model" (e.g., quantized GGUF from Hugging Face Hub) and ensure it's accessible.
*   **Task 2.2: Implement Local LLM Wrapper (load model, generate text, handle params)**
    *   **Status:** pending
    *   Create a Python class (e.g., `LocalLLMService`) that encapsulates the selected local LLM library.
    *   Implement methods for loading the tiny model, generating text, and handling common inference parameters (e.g., `temperature`, `max_tokens`).
    *   Manage resource usage (e.g., CPU/GPU based on available hardware).
*   **Task 2.3: Local LLM MCP Server/Client (expose capabilities, translate requests)**
    *   **Status:** pending
    *   Develop an MCP server or client that integrates with the `LocalLLMService`.
    *   This component will expose the local LLM's `ModelContext` (capabilities, configuration) and translate incoming MCP requests into calls to the `LocalLLMService`.

### Phase 3: Provider LLM Integration
**Status:** pending

*   **Task 3.1: Choose a Provider LLM (e.g., OpenAI, AWS Bedrock) and obtain credentials**
    *   **Status:** pending
    *   Select at least one external LLM provider for initial integration.
    *   Securely obtain and store necessary API keys and credentials (e.g., in `.env` file).
*   **Task 3.2: Implement Provider LLM Wrapper (make API calls, handle messages, token management)**
    *   **Status:** pending
    *   Create a Python class (e.g., `OpenAILLMService`, `BedrockLLMService`) that uses the provider's SDK (`openai`, `boto3`).
    *   Implement methods for making API calls, handling chat messages, and managing token usage and limits.
*   **Task 3.3: Provider LLM MCP Server/Client (expose capabilities, handle authentication, translate requests)**
    *   **Status:** pending
    *   Develop an MCP server or client to encapsulate the chosen provider LLM.
    *   This will expose the provider LLM's `ModelContext` and translate MCP requests into provider-specific API calls, handling authentication securely.

### Phase 4: MCP Orchestration & Routing
**Status:** pending

*   **Task 4.1: MCP Registry/Discovery (discover and register MCP servers)**
    *   **Status:** pending
    *   Implement a mechanism for the orchestration layer to discover and register all available MCP servers (local and provider-based). This could be static (via `mcp.json`) or dynamic.
*   **Task 4.2: Orchestration Logic (analyze requests, select optimal LLM based on criteria)**
    *   **Status:** pending
    *   Create a central `LLMOrchestrator` class responsible for intelligent routing.
    *   Implement logic to analyze incoming user requests and, based on defined criteria (cost, latency, specific model features from `ModelContext`, local preference), select the most suitable LLM.
    *   Route the request via the chosen LLM's MCP interface.
*   **Task 4.3: Cooperative Strategy Implementation (define and implement chaining/routing logic)**
    *   **Status:** pending
    *   Define and implement strategies for "co-operative" behavior between LLMs. This might involve chaining calls (e.g., local LLM for initial draft, provider LLM for refinement) or parallel execution for comparative analysis.

### Phase 5: Refinement & Testing
**Status:** pending

*   **Task 5.1: Write Unit Tests for all components**
    *   **Status:** pending
    *   Develop comprehensive unit tests for each class and function across the system (MCP data models, LLM wrappers, MCP clients/servers, orchestrator).
*   **Task 5.2: Develop Integration Tests for end-to-end functionality**
    *   **Status:** pending
    *   Create integration tests to verify the seamless interaction between all components: local LLM, provider LLMs, MCP layers, and the orchestration logic.
*   **Task 5.3: Perform Performance Benchmarking**
    *   **Status:** pending
    *   Conduct performance benchmarking for both local and provider LLMs and the overall orchestration layer to identify bottlenecks and optimize.
*   **Task 5.4: Improve Error Handling & Robustness**
    *   **Status:** pending
    *   Enhance error handling mechanisms, logging, and implement strategies to ensure the system's robustness and graceful degradation under various failure scenarios.

---
