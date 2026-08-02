# Volume II · Chapter 9 — Medical Domain Adaptation · Theory

> Source: split from `med-tech-curriculum-V1.md` (V1). From this split onward this chapter is maintained **independently** here. See `Volume-II-Chapter-9-context.md` for the AI interaction log.

**Prerequisites:** Ch 7, Ch 8.

**Learning outcomes — the student can:** distinguish continued pretraining vs. fine-tuning vs. instruction tuning; explain how Meditron/Clinical-Camel/MedGemma were adapted; choose an adaptation strategy; reason about data requirements and licensing.

**Topics (theory) — 10 h:**

| # | Topic | h |
|---|-------|---|
| 9.1 | Why adapt general LLMs to medicine; gaps & risks | 1 |
| 9.2 | Continued pretraining on biomedical corpora | 2 |
| 9.3 | Supervised fine-tuning & instruction tuning | 2 |
| 9.4 | Case studies: Meditron, Clinical-Camel, MedGemma, PubMedBERT | 2 |
| 9.5 | Data: sources, curation, quality, licensing for medical corpora | 2 |
| 9.6 | Choosing an adaptation strategy vs. RAG (decision framework) | 1 |

**Datasets/tools:** HF models (Meditron/MedGemma/PubMedBERT), `datasets`.
**Assessment:** adaptation-plan deliverable (**50%**); comparison lab (**30%**); quiz (**20%**).
**Key decisions:** pretrain vs. fine-tune vs. RAG; data licensing; base-model choice.
**References:** plan §13 → *Medical LLMs*; *Fine-tuning, alignment & benchmarks*.
**Hours:** Theory **10** + Lab **6** = **16**.
