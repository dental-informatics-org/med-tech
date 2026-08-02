# Volume II · Chapter 10 — Benchmarking & Hallucination · Theory

> Source: split from `med-tech-curriculum-V1.md` (V1). From this split onward this chapter is maintained **independently** here. See `Volume-II-Chapter-10-context.md` for the AI interaction log.

**Prerequisites:** Ch 8, Ch 9.

**Learning outcomes — the student can:** evaluate LLMs on medical benchmarks (MedQA/PubMedQA/MedMCQA); interpret results; measure hallucination; build an eval harness; explain why benchmark ≠ clinical safety.

**Topics (theory) — 8 h:**

| # | Topic | h |
|---|-------|---|
| 10.1 | Benchmark landscape: MedQA (USMLE), PubMedQA, MedMCQA | 2 |
| 10.2 | Metrics: accuracy, exact-match & their limits | 1 |
| 10.3 | Hallucination: definitions, causes, measurement | 2 |
| 10.4 | Faithfulness & grounding metrics | 1 |
| 10.5 | Benchmark ≠ clinical safety; distribution shift | 2 |

**Datasets/tools:** HF `datasets`/`evaluate`; local LLM.
**Assessment:** eval-harness deliverable (**50%**); hallucination report (**30%**); quiz (**20%**).
**Key decisions:** which benchmark supports which claim; honest reporting of limitations.
**References:** plan §13 → *Fine-tuning, alignment & benchmarks*; *Medical LLMs*.
**Hours:** Theory **8** + Lab **8** = **16**.
