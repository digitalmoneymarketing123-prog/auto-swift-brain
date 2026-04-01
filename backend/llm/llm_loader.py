"""
LLM Loader

This module is responsible for:
- Reading llm_config.yaml
- Selecting the correct LLM adapter
- Returning a ready-to-use LLM client

This keeps Auto‑Swift Brain fully LLM‑agnostic.
"""

import yaml
from pathlib import Path

from backend.llm.openai_adapter import OpenAIAdapter


CONFIG_PATH = Path(__file__).resolve().parents[1] / "config" / "llm_config.yaml"


def load_llm():
    """
    Load and return the configured LLM adapter based on llm_config.yaml.
    """

    if not CONFIG_PATH.exists():
        raise FileNotFoundError(
            f"LLM config file not found at: {CONFIG_PATH}"
        )

    with open(CONFIG_PATH, "r", encoding="utf-8") as file:
        config = yaml.safe_load(file)

    llm_config = config.get("llm", {})
    provider = llm_config.get("provider")
    model = llm_config.get("model")

    if provider == "openai":
        return OpenAIAdapter(model=model)

    raise ValueError(
        f"Unsupported LLM provider: {provider}"
    )