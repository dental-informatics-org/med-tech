# Volume IV · Chapter 18 — Ingestion, OCR & Document Understanding · Theory

> Source: split from `med-tech-curriculum-V1.md` (V1). From this split onward this chapter is maintained **independently** here. See `Volume-IV-Chapter-18-context.md` for the AI interaction log.

**Prerequisites:** Ch 5, Ch 12.

**Learning outcomes — the student can:** parse born-digital and scanned medical books; run OCR handling medical vocabulary; extract layout/structure (sections, tables, references); build a clean, provenance-tagged text corpus.

**Topics (theory) — 8 h:**

| # | Topic | h |
|---|-------|---|
| 18.1 | Document types & challenges: PDFs, scans, layout, columns | 2 |
| 18.2 | OCR fundamentals & medical-text pitfalls (terms, dosages, tables) | 2 |
| 18.3 | Layout analysis & structure extraction (sections, headings, refs) | 2 |
| 18.4 | Tables, equations & footnotes; reading order | 1 |
| 18.5 | Provenance & metadata capture during ingestion | 1 |

**Datasets/tools:** licensed/open medical texts; PyMuPDF, Tesseract, unstructured/Nougat/Marker.
**Assessment:** ingestion pipeline + corpus (**60%**); OCR-quality report (**20%**); quiz (**20%**).
**Key decisions:** born-digital vs. scanned handling; OCR engine; how much structure to preserve; **licensing (owned/licensed sources only)**.
**References:** plan §6; §13.
**Hours:** Theory **8** + Lab **14** = **22**.
