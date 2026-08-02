# Volume III · Chapter 15 — Evaluation, Bias, Fairness & Clinical Safety · Labs

> Source: split from `med-tech-curriculum-V1.md` (V1). From this split onward this chapter is maintained **independently** here. See `Volume-III-Chapter-15-context.md` for the AI interaction log.

**Prerequisites:** Ch 10, Ch 14.

**Learning outcomes — the student can:** design rigorous clinical evaluation; measure subgroup bias/fairness; assess calibration and safety (red-teaming); explain the benchmark-to-clinic gap; run clinician-in-the-loop evaluation.

**Labs (hands-on) — 10 h:**

| # | Lab | h |
|---|-----|---|
| 15a | Subgroup fairness analysis on a clinical model | 3 |
| 15b | Calibration curves & reliability diagrams | 2 |
| 15c | Red-team a medical LLM; catalog failure modes | 3 |
| 15d | Design a human-eval rubric & run a mini study | 2 |

**Datasets/tools:** `evaluate`, fairness libraries; local LLM.
**Assessment:** safety/fairness eval report (**60%**); red-team catalog (**20%**); quiz (**20%**).
**Key decisions:** which subgroups & metrics; acceptable risk thresholds; when a model is **not** safe to deploy.
**References:** plan §13 → *Medical LLMs*; *Fine-tuning, alignment & benchmarks*.
**Hours:** Theory **12** + Lab **10** = **22**.
