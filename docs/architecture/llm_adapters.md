# LLM Adapters — How to Plug Your Own AI into Auto‑Swift Brain

Auto‑Swift Brain is **LLM‑agnostic by design**.  
This means the core decision logic never depends on a specific AI provider.

Any Large Language Model that supports **text‑in / text‑out** can be connected.

---

## Core Principle

The brain logic must **never** know:
- which LLM is used
- how authentication works
- how requests are sent
- vendor‑specific limits or pricing

All interaction with AI happens through a **single adapter contract**.

---

## The Adapter Contract

Every LLM adapter must implement the following interface:

```python
class BaseLLMAdapter:
    def generate(self, prompt: str, context: dict | None = None) -> str:
        pass