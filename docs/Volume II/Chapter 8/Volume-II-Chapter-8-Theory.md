# Volume II · Chapter 8 — Prompt Engineering for Medicine · Theory

> Source: split from `med-tech-curriculum-V1.md` (V1). From this split onward this chapter is maintained **independently** here. See `Volume-II-Chapter-8-context.md` for the AI interaction log.

**Prerequisites:** Ch 7.

**Learning outcomes — the student can:** design effective prompts (zero/few-shot, chain-of-thought); produce structured outputs; assess reliability and hallucination; apply basic safety/injection awareness in clinical apps.

**Topics (theory) — 8 h:**

| # | Topic | h |
|---|-------|---|
| 8.1 | Prompting fundamentals: zero/few-shot, roles, instructions | 2 |
| 8.2 | Chain-of-thought & reasoning prompts | 1 |
| 8.3 | Structured outputs (JSON, schemas), constrained generation | 1 |
| 8.4 | Retrieval-grounded prompting (intro to the RAG idea) | 1 |
| 8.5 | Reliability, hallucination & self-consistency; when NOT to trust | 2 |
| 8.6 | Safety & prompt-injection awareness in clinical apps | 1 |

**Datasets/tools:** local LLM via Ollama (MedGemma) or HF; Python.
**Assessment:** prompt-portfolio deliverable (**50%**); structured-extraction lab (**30%**); quiz (**20%**).
**Key decisions:** prompting vs. fine-tuning vs. RAG; how to measure reliability; guardrails.
**References:** plan §13 → *Medical LLMs*.
**Hours:** Theory **8** + Lab **10** = **18**.
