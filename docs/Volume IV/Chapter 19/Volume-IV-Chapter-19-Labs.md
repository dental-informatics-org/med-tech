# Volume IV · Chapter 19 — Figures & Multimodal Understanding · Labs

> Source: split from `med-tech-curriculum-V1.md` (V1). From this split onward this chapter is maintained **independently** here. See `Volume-IV-Chapter-19-context.md` for the AI interaction log.

**Prerequisites:** Ch 18, Ch 7.

**Learning outcomes — the student can:** detect/extract figures; generate & curate captions with multimodal models; link images to text; make images retrievable; describe the SOTA and limits of medical image understanding.

**Labs (hands-on) — 14 h:**

| # | Lab | h |
|---|-----|---|
| 19a | Extract figures + captions from a medical document | 3 |
| 19b | Generate captions with a multimodal model; compare to originals | 4 |
| 19c | Multimodal retrieval: query text → return relevant figures | 4 |
| 19d | Link figures to text chunks; evaluate linkage quality | 3 |

**Datasets/tools:** multimodal HF models (LLaVA-Med/MedGemma), CLIP-style embeddings; vector DB.
**Assessment:** multimodal ingest+retrieval (**60%**); caption-quality report (**20%**); quiz (**20%**).
**Key decisions:** which multimodal model; how much to trust captions; image vs. caption embeddings.
**References:** plan §6; §13 → *Medical LLMs*.
**Hours:** Theory **8** + Lab **14** = **22**.
