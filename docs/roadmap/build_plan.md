# Auto‑Swift Brain — Build Roadmap

This document defines the deliberate build plan for Auto‑Swift Brain.
The goal is to maintain clarity, prevent feature creep, and protect the core philosophy.

---

## ✅ Completed (Foundation)

The following components are intentionally complete and stable:

- Clean repository structure
- Clear README and contribution rules
- LLM‑agnostic architecture
- Base LLM adapter contract
- One reference adapter (OpenAI)
- LLM adapter documentation
- Central configuration (`llm_config.yaml`)

This foundation allows others to extend the system without changing the core.

---

## 🟡 Next (Planned)

These will be added step‑by‑step, without rushing:

- Runtime selection of LLM adapter via config
- Decision signal detection (hesitation, risk, repetition)
- Minimal execution engine (one action at a time)
- Chat‑first UI scaffolding (no dashboards)
- Weekly review logic (text‑based, no metrics overload)

Each addition must improve clarity, not complexity.

---

## 🚫 Explicit Non‑Goals

The following will **not** be built:

- CRM features
- Dashboards or analytics panels
- Gamification or scoring
- AI personalities or avatars
- Hard‑coded model dependencies
- Prompt collections without context

These are deliberate exclusions.

---

## Philosophy Reminder

Auto‑Swift Brain exists to:
> Improve judgment, not automate thinking away.

If a feature weakens decision quality or increases noise, it does not belong here.