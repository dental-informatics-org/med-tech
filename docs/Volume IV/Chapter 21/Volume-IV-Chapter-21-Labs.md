# Volume IV · Chapter 21 — RAG-vs-Fine-tune Paths & Synthetic Data · Labs

> Source: split from `med-tech-curriculum-V1.md` (V1). From this split onward this chapter is maintained **independently** here. See `Volume-IV-Chapter-21-context.md` for the AI interaction log.

**Prerequisites:** Ch 11, Ch 12, Ch 20.

**Learning outcomes — the student can:** decide between RAG and fine-tuning for book knowledge; generate quality-controlled synthetic Q&A/instruction data from sources; build image-text pairs; compare accuracy/hallucination of both paths.

**Labs (hands-on) — 16 h:**

| # | Lab | h |
|---|-----|---|
| 21a | Generate synthetic Q&A from a book chapter; QC filter | 4 |
| 21b | Fine-tune a small model on the synthetic set (QLoRA) | 5 |
| 21c | Build a RAG baseline over the same content | 3 |
| 21d | Head-to-head: accuracy & hallucination, RAG vs. fine-tune | 4 |

**Datasets/tools:** local LLM; HF `peft`/QLoRA; vector DB; eval harness.
**Assessment:** comparative study (**60%**); synthetic-data QC report (**20%**); quiz (**20%**).
**Key decisions:** RAG vs. fine-tune vs. both; synthetic-data quality gates; licensing of derived data.
**References:** plan §6; §13 → *Fine-tuning…*; *RAG…*.
**Hours:** Theory **8** + Lab **16** = **24**.
