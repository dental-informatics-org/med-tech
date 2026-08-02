# Volume III · Chapter 14 — Training Pipeline: Pre-training → Fine-tuning → Alignment (DPO) · Labs

> Source: split from `med-tech-curriculum-V1.md` (V1). From this split onward this chapter is maintained **independently** here. See `Volume-III-Chapter-14-context.md` for the AI interaction log.

**Prerequisites:** Ch 11, Ch 12.

**Learning outcomes — the student can:** describe the full three-stage pipeline; reason about data/compute for pretraining; run domain fine-tuning; build preference data and apply DPO; compare RLHF vs. DPO; manage training runs with tracking.

**Labs (hands-on) — 20 h:**

| # | Lab | h |
|---|-----|---|
| 14a | Continued pretraining (small) on a biomedical corpus | 5 |
| 14b | Build an SFT dataset & run supervised fine-tuning | 5 |
| 14c | Create a preference dataset (chosen/rejected) for a clinical behavior | 3 |
| 14d | Run DPO on the SFT model | 5 |
| 14e | Track experiments & compare stages (metrics, safety checks) | 2 |

**Datasets/tools:** HF `transformers`/`trl`/`peft`, DPO; experiment tracking (W&B or MLflow); GPU.
**Assessment:** aligned model across stages (**60%**); training report (**20%**); quiz (**20%**).
**Key decisions:** pretrain vs. fine-tune vs. align scope; DPO vs. RLHF; data quality vs. quantity; compute budget.
**References:** plan §13 → *Fine-tuning, alignment & benchmarks*; *Medical LLMs*; *Clinical datasets*.
**Hours:** Theory **16** + Lab **20** = **36**.
