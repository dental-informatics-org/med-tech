# Volume III · Chapter 15 — Evaluation, Bias, Fairness & Clinical Safety · Theory

> Source: split from `med-tech-curriculum-V1.md` (V1). From this split onward this chapter is maintained **independently** here. See `Volume-III-Chapter-15-context.md` for the AI interaction log.

**Prerequisites:** Ch 10, Ch 14.

**Learning outcomes — the student can:** design rigorous clinical evaluation; measure subgroup bias/fairness; assess calibration and safety (red-teaming); explain the benchmark-to-clinic gap; run clinician-in-the-loop evaluation.

**Topics (theory) — 12 h:**

| # | Topic | h |
|---|-------|---|
| 15.1 | Evaluation beyond accuracy: task-appropriate metrics | 2 |
| 15.2 | Bias & fairness: subgroup analysis, disparate performance | 2 |
| 15.3 | Calibration & uncertainty in clinical models | 2 |
| 15.4 | Safety: harmful outputs, refusal, red-teaming | 2 |
| 15.5 | Benchmark vs. clinical validity; prospective vs. retrospective | 2 |
| 15.6 | Human evaluation & clinician-in-the-loop protocols | 2 |

**Datasets/tools:** `evaluate`, fairness libraries; local LLM.
**Assessment:** safety/fairness eval report (**60%**); red-team catalog (**20%**); quiz (**20%**).
**Key decisions:** which subgroups & metrics; acceptable risk thresholds; when a model is **not** safe to deploy.
**References:** plan §13 → *Medical LLMs*; *Fine-tuning, alignment & benchmarks*.
**Hours:** Theory **12** + Lab **10** = **22**.
