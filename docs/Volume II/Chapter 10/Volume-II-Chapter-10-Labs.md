# Volume II · Chapter 10 — Benchmarking & Hallucination · Labs

> Source: split from `med-tech-curriculum-V1.md` (V1). From this split onward this chapter is maintained **independently** here. See `Volume-II-Chapter-10-context.md` for the AI interaction log.

**Prerequisites:** Ch 8, Ch 9.

**Learning outcomes — the student can:** evaluate LLMs on medical benchmarks (MedQA/PubMedQA/MedMCQA); interpret results; measure hallucination; build an eval harness; explain why benchmark ≠ clinical safety.

**Labs (hands-on) — 8 h:**

| # | Lab | h |
|---|-----|---|
| 10a | Run a model on a MedQA-style set; compute accuracy | 3 |
| 10b | Build a small eval harness with the `evaluate` library | 2 |
| 10c | Hallucination test: craft adversarial clinical prompts, score | 3 |

**Datasets/tools:** HF `datasets`/`evaluate`; local LLM.
**Assessment:** eval-harness deliverable (**50%**); hallucination report (**30%**); quiz (**20%**).
**Key decisions:** which benchmark supports which claim; honest reporting of limitations.
**References:** plan §13 → *Fine-tuning, alignment & benchmarks*; *Medical LLMs*.
**Hours:** Theory **8** + Lab **8** = **16**.
