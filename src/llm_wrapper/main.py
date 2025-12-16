from typing import Any, Dict
from src.llm_wrapper.core.config import settings
from src.llm_wrapper.core.base import BaseLLMClient, LLMResponse
from src.llm_wrapper.core.router import RequestRouter # Import RequestRouter
from src.data_models.llm_wrapper import InferenceRequest, InferenceResponse
import logging
import datetime

logger = logging.getLogger(__name__)

class MCPOrchestrator:
    """
    The main orchestrator for the LLM wrapper. It acts as the "brain" of the wrapper,
    coordinating between MCP servers, local LLMs, and provider LLMs.
    """
    def __init__(self):
        """
        Initializes the MCPOrchestrator, loading configuration and setting up
        core components.
        """
        self.settings = settings
        logger.info(f"MCPOrchestrator initialized with settings: {self.settings.dict()}")
        
        self.router = RequestRouter() # Instantiate the router
        # Placeholders for other components
        self.context_manager: Any = None # Will be an instance of a context manager class
        self.mcp_client: Any = None # Will be an instance of an MCP client class
        
        logger.info("Core components initialized.")

    async def health_check(self) -> Dict[str, Any]:
        """
        Performs a health check of the orchestrator and its integrated components.
        
        Returns:
            Dict[str, Any]: A dictionary containing health status of various components.
        """
        status = {
            "status": "UP",
            "timestamp": datetime.datetime.now().isoformat(),
            "config_loaded": bool(self.settings),
            "router_status": "OK", # Router is now instantiated
            "local_llm_client_status": "OK", # Clients are instantiated within router
            "provider_llm_client_status": "OK", # Clients are instantiated within router
            "mcp_client_status": "N/A (not implemented)"
        }
        logger.info(f"Health check performed: {status}")
        return status

    async def process_request(self, request: InferenceRequest) -> InferenceResponse:
        """
        Processes an incoming LLM inference request, routing it to the appropriate LLM.
        """
        logger.info(f"Processing request for prompt: '{request.prompt[:50]}...' (model_id: {request.model_id or 'auto'})")
        
        # Determine routing based on the prompt (and potentially request.model_id in future)
        client, clean_prompt = self.router.determine_route(request.prompt)
        
        # TODO: Potential MCP Context Enrichment (Future Task)
        # enriched_prompt = await self.context_manager.enrich(clean_prompt) # Assuming async context manager
        
        # Generate response using the selected client
        response = await client.generate(
            prompt=clean_prompt,
            parameters=request.parameters.dict(), # Pass Pydantic model as dict
            context=request.context # Pass context
        )
        return response
