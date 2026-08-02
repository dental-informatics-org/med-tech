# Volume IV · Chapter 19 — Figures & Multimodal Understanding · Theory

> Source: split from `med-tech-curriculum-V1.md` (V1). From this split onward this chapter is maintained **independently** here. See `Volume-IV-Chapter-19-context.md` for the AI interaction log.

**Prerequisites:** Ch 18, Ch 7.

**Learning outcomes — the student can:** detect/extract figures; generate & curate captions with multimodal models; link images to text; make images retrievable; describe the SOTA and limits of medical image understanding.

**Topics (theory) — 8 h:**

| # | Topic | h |
|---|-------|---|
| 19.1 | Medical figures: radiology, histology, ECG, diagrams, charts | 1 |
| 19.2 | Figure detection & extraction from documents | 1 |
| 19.3 | Multimodal models (captioning, VQA): LLaVA-Med, MedGemma-multimodal | 2 |
| 19.4 | Image embeddings & multimodal retrieval | 2 |
| 19.5 | Linking figures to surrounding text & captions | 1 |
| 19.6 | SOTA & limits: reliability of medical image understanding | 1 |

**Datasets/tools:** multimodal HF models (LLaVA-Med/MedGemma), CLIP-style embeddings; vector DB.
**Assessment:** multimodal ingest+retrieval (**60%**); caption-quality report (**20%**); quiz (**20%**).
**Key decisions:** which multimodal model; how much to trust captions; image vs. caption embeddings.
**References:** plan §6; §13 → *Medical LLMs*.
**Hours:** Theory **8** + Lab **14** = **22**.
