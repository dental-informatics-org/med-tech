# Volume II · Chapter 8 — Prompt Engineering for Medicine · Labs

> Source: split from `med-tech-curriculum-V1.md` (V1). From this split onward this chapter is maintained **independently** here. See `Volume-II-Chapter-8-context.md` for the AI interaction log.

**Prerequisites:** Ch 7.

**Learning outcomes — the student can:** design effective prompts (zero/few-shot, chain-of-thought); produce structured outputs; assess reliability and hallucination; apply basic safety/injection awareness in clinical apps.

**Labs (hands-on) — 10 h:**

| # | Lab | h |
|---|-----|---|
| 8a | Prompt iteration on a clinical QA task; zero- vs. few-shot | 3 |
| 8b | Chain-of-thought vs. direct on clinical reasoning; measure | 2 |
| 8c | Structured extraction: prompt an LLM to output a JSON clinical summary | 3 |
| 8d | Hallucination probe: design tests, log failures | 2 |

**Datasets/tools:** local LLM via Ollama (MedGemma) or HF; Python.
**Assessment:** prompt-portfolio deliverable (**50%**); structured-extraction lab (**30%**); quiz (**20%**).
**Key decisions:** prompting vs. fine-tuning vs. RAG; how to measure reliability; guardrails.
**References:** plan §13 → *Medical LLMs*.
**Hours:** Theory **8** + Lab **10** = **18**.
