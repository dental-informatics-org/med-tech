# Volume II · Chapter 9 — Medical Domain Adaptation · Labs

> Source: split from `med-tech-curriculum-V1.md` (V1). From this split onward this chapter is maintained **independently** here. See `Volume-II-Chapter-9-context.md` for the AI interaction log.

**Prerequisites:** Ch 7, Ch 8.

**Learning outcomes — the student can:** distinguish continued pretraining vs. fine-tuning vs. instruction tuning; explain how Meditron/Clinical-Camel/MedGemma were adapted; choose an adaptation strategy; reason about data requirements and licensing.

**Labs (hands-on) — 6 h:**

| # | Lab | h |
|---|-----|---|
| 9a | Compare a general vs. domain-adapted model on medical prompts | 2 |
| 9b | Prepare a small biomedical instruction dataset (format, clean) | 2 |
| 9c | Design an adaptation plan for a chosen clinical use case | 2 |

**Datasets/tools:** HF models (Meditron/MedGemma/PubMedBERT), `datasets`.
**Assessment:** adaptation-plan deliverable (**50%**); comparison lab (**30%**); quiz (**20%**).
**Key decisions:** pretrain vs. fine-tune vs. RAG; data licensing; base-model choice.
**References:** plan §13 → *Medical LLMs*; *Fine-tuning, alignment & benchmarks*.
**Hours:** Theory **10** + Lab **6** = **16**.
