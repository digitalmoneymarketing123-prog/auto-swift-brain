"""
OpenAI LLM Adapter

This is a reference implementation showing how to connect
an external LLM to Auto‑Swift Brain using the BaseLLMAdapter contract.

This adapter is intentionally simple and readable.
"""

import os
from typing import Optional, Dict

from backend.llm.base_adapter import BaseLLMAdapter


class OpenAIAdapter(BaseLLMAdapter):
    """
    OpenAI implementation of BaseLLMAdapter.
    """

    def __init__(self, model: str = "gpt-4o-mini"):
        api_key = os.getenv("OPENAI_API_KEY")

        if not api_key:
            raise RuntimeError(
                "OPENAI_API_KEY environment variable is not set"
            )

        try:
            from openai import OpenAI
        except ImportError:
            raise ImportError(
                "OpenAI SDK not installed. Run: pip install openai"
            )

        self.client = OpenAI(api_key=api_key)
        self.model = model

    def generate(self, prompt: str, context: Optional[Dict] = None) -> str:
        """
        Generate a response from OpenAI using prompt + optional context.
        """

        messages = []

        if context:
            messages.append({
                "role": "system",
                "content": f"Context:\n{context}"
            })

        messages.append({
            "role": "user",
            "content": prompt
        })

        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=0.2
        )

        return response.choices[0].message.content.strip()