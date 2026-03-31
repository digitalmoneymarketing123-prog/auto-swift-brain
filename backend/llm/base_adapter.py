"""
Base LLM Adapter Interface

This file defines the contract for connecting any Large Language Model (LLM)
to Auto‑Swift Brain.

The core system must remain completely model‑agnostic.
All LLM integrations must follow this interface.
"""

from abc import ABC, abstractmethod
from typing import Optional, Dict


class BaseLLMAdapter(ABC):
    """
    Abstract base class for all LLM adapters.
    """

    @abstractmethod
    def generate(self, prompt: str, context: Optional[Dict] = None) -> str:
        """
        Generate a text response from the LLM.

        Parameters:
        - prompt: The primary instruction or query.
        - context: Optional structured context
          (conversation history, signals, decisions).

        Returns:
        - Generated text response.
        """
        pass