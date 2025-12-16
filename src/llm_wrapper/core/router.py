import re
from typing import Tuple, List, Any
from llm_wrapper.core.base import BaseLLMClient
from llm_wrapper.providers.local_client import LocalCLIClient
from llm_wrapper.providers.remote_client import ProviderSDKClient
import logging

logger = logging.getLogger(__name__)

class RequestRouter:
    """Traffic controller for LLM requests."""
    
    def __init__(self):
        # Instantiate clients once to reuse resources
        self.local_client = LocalCLIClient()
        self.provider_client = ProviderSDKClient()
        logger.info("RequestRouter initialized with LocalCLIClient and ProviderSDKClient.")

    def determine_route(self, prompt: str) -> Tuple[BaseLLMClient, str]:
        """
        Decides which client to use based on prompt analysis.
        Returns: (Client instance, clean_prompt)
        """
        # 1. Check for Explicit Tags
        if "@local" in prompt.lower():
            logger.info("Explicit @local tag found. Routing to LocalCLIClient.")
            return self.local_client, prompt.replace("@local", "").strip()
        
        if "@cloud" in prompt.lower() or "@provider" in prompt.lower():
            logger.info("Explicit @cloud/@provider tag found. Routing to ProviderSDKClient.")
            return self.provider_client, prompt.replace("@cloud", "").replace("@provider", "").strip()

        # 2. Rule-Based Complexity/Privacy Check
        if self._is_high_complexity(prompt):
            logger.info("Prompt detected as high complexity. Routing to ProviderSDKClient.")
            return self.provider_client, prompt
            
        # Default to local for simple tasks to save cost/latency
        logger.info("Prompt detected as low complexity/default. Routing to LocalCLIClient.")
        return self.local_client, prompt

    def _is_high_complexity(self, prompt: str) -> bool:
        """Heuristic to detect tasks requiring the 'Provider' tier."""
        # Keywords suggesting coding, complex logic, or math
        complex_patterns = [
            r"\b(write a function|debug|refactor|python|javascript)\b",
            r"\b(solve|calculate|theorem|complex)\b",
            r"\b(analyze|summarize this 50 page)\b",
            r"\b(generate code|implement solution)\b" # Added common coding-related phrases
        ]
        
        # If prompt is long (> 200 chars, reduced from 500 for more aggressive provider routing on verbosity)
        if len(prompt) > 200:
            logger.debug(f"Prompt length ({len(prompt)}) > 200. Considered high complexity.")
            return True
            
        # Check against complex patterns
        is_complex = any(re.search(pattern, prompt, re.IGNORECASE) for pattern in complex_patterns)
        if is_complex:
            logger.debug("Prompt matched complex pattern. Considered high complexity.")
        return is_complex