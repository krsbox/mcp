from typing import Any, Dict
from src.llm_wrapper.core.config import settings
from src.llm_wrapper.core.base import BaseLLMClient
from src.llm_wrapper.core.router import RequestRouter
from src.llm_wrapper.providers.local_client import LocalCLIClient # Import LocalCLIClient
from src.llm_wrapper.providers.remote_client import ProviderSDKClient # Import ProviderSDKClient
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
        
        # Instantiate clients and pass them to the router
        self.local_client = LocalCLIClient()
        self.provider_client = ProviderSDKClient()
        self.router = RequestRouter(self.local_client, self.provider_client)
        
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
            "router_status": "OK", 
            "local_llm_client_status": "OK",
            "provider_llm_client_status": "OK",
            "mcp_client_status": "N/A (not implemented)"
        }
        logger.info(f"Health check performed: {status}")
        return status

    async def process_request(self, request: InferenceRequest) -> InferenceResponse:
        """
        Processes an incoming LLM inference request, routing it to the appropriate LLM with fallback.
        """
        logger.info(f"Processing request for prompt: '{request.prompt[:50]}...' (model_id: {request.model_id or 'auto'})")
        
        # Use the router's generate_with_fallback method
        response = await self.router.generate_with_fallback(
            prompt=request.prompt,
            parameters=request.parameters.dict(),
            context=request.context
        )
        return response