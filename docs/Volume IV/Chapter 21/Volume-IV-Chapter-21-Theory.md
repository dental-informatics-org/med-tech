# Volume IV · Chapter 21 — RAG-vs-Fine-tune Paths & Synthetic Data · Theory

> Source: split from `med-tech-curriculum-V1.md` (V1). From this split onward this chapter is maintained **independently** here. See `Volume-IV-Chapter-21-context.md` for the AI interaction log.

**Prerequisites:** Ch 11, Ch 12, Ch 20.

**Learning outcomes — the student can:** decide between RAG and fine-tuning for book knowledge; generate quality-controlled synthetic Q&A/instruction data from sources; build image-text pairs; compare accuracy/hallucination of both paths.

**Topics (theory) — 8 h:**

| # | Topic | h |
|---|-------|---|
| 21.1 | Decision framework: RAG vs. fine-tune vs. both for book knowledge | 2 |
| 21.2 | Synthetic Q&A generation from source text (quality control) | 2 |
| 21.3 | Image-text pair construction for multimodal training | 1 |
| 21.4 | Risks: hallucinated synthetic data, contamination, licensing | 2 |
| 21.5 | Comparing paths: accuracy, faithfulness, cost | 1 |

**Datasets/tools:** local LLM; HF `peft`/QLoRA; vector DB; eval harness.
**Assessment:** comparative study (**60%**); synthetic-data QC report (**20%**); quiz (**20%**).
**Key decisions:** RAG vs. fine-tune vs. both; synthetic-data quality gates; licensing of derived data.
**References:** plan §6; §13 → *Fine-tuning…*; *RAG…*.
**Hours:** Theory **8** + Lab **16** = **24**.
