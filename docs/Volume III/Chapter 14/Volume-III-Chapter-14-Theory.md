# Volume III · Chapter 14 — Training Pipeline: Pre-training → Fine-tuning → Alignment (DPO) · Theory

> Source: split from `med-tech-curriculum-V1.md` (V1). From this split onward this chapter is maintained **independently** here. See `Volume-III-Chapter-14-context.md` for the AI interaction log.

**Prerequisites:** Ch 11, Ch 12.

**Learning outcomes — the student can:** describe the full three-stage pipeline; reason about data/compute for pretraining; run domain fine-tuning; build preference data and apply DPO; compare RLHF vs. DPO; manage training runs with tracking.

**Topics (theory) — 16 h:**

| # | Topic | h |
|---|-------|---|
| 14.1 | The three-stage pipeline overview (pretrain→SFT→align) | 1 |
| 14.2 | Pretraining: data scale, objectives, tokenization, compute | 2 |
| 14.3 | Domain fine-tuning on medical corpora (e.g., MedFineWeb) | 2 |
| 14.4 | Instruction/supervised fine-tuning data design | 2 |
| 14.5 | Preference alignment: RLHF overview | 2 |
| 14.6 | Direct Preference Optimization (DPO): theory & practice | 3 |
| 14.7 | Safety alignment for medical outputs | 2 |
| 14.8 | Training infra: checkpoints, mixed precision, distributed basics, experiment tracking | 2 |

**Datasets/tools:** HF `transformers`/`trl`/`peft`, DPO; experiment tracking (W&B or MLflow); GPU.
**Assessment:** aligned model across stages (**60%**); training report (**20%**); quiz (**20%**).
**Key decisions:** pretrain vs. fine-tune vs. align scope; DPO vs. RLHF; data quality vs. quantity; compute budget.
**References:** plan §13 → *Fine-tuning, alignment & benchmarks*; *Medical LLMs*; *Clinical datasets*.
**Hours:** Theory **16** + Lab **20** = **36**.
