# Contributing to Auto‑Swift Brain

Thank you for your interest in contributing.

Auto‑Swift Brain is a **decision orchestration framework**, not a general AI playground.
Please read this document carefully before opening issues or pull requests.

---

## Core Principles

All contributions must respect these principles:

- **LLM‑agnostic design**
- **Clear separation of concerns**
- **Decision logic is sacred**
- **Clarity over cleverness**
- **No feature bloat**

If a contribution weakens these principles, it will not be accepted.

---

## What This Project Needs

We welcome contributions in these areas:

- LLM adapters (Gemini, OpenClaw, local LLMs)
- Documentation improvements
- Architecture clarifications
- Decision‑logic refinements (with justification)
- UI clarity (chat‑first, minimal)

---

## What This Project Does NOT Accept

Please do NOT submit:

- CRM features
- Dashboards or analytics panels
- Gamification
- AI avatars or personalities
- Hard‑coded API keys
- Model‑specific logic inside the brain
- Prompt collections without context

---

## Adapter Contributions (Very Important)

All LLM integrations **must**:

- Extend `BaseLLMAdapter`
- Implement only `generate(prompt, context)`
- Use environment variables for secrets
- Contain no decision logic
- Return text only

Reference: