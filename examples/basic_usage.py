"""
Basic usage example for Auto‑Swift Brain.

This shows how to:
- Load the configured LLM via llm_config.yaml
- Send a prompt
- Receive a response
"""

from backend.llm.llm_loader import load_llm


def main():
    llm = load_llm()

    response = llm.generate(
        prompt="Write a concise professional follow-up email after a sales call.",
        context={
            "tone": "professional",
            "goal": "schedule next meeting"
        }
    )

    print(response)


if __name__ == "__main__":
    main()