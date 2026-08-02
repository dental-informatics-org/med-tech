# Volume IV · Chapter 18 — Ingestion, OCR & Document Understanding · Labs

> Source: split from `med-tech-curriculum-V1.md` (V1). From this split onward this chapter is maintained **independently** here. See `Volume-IV-Chapter-18-context.md` for the AI interaction log.

**Prerequisites:** Ch 5, Ch 12.

**Learning outcomes — the student can:** parse born-digital and scanned medical books; run OCR handling medical vocabulary; extract layout/structure (sections, tables, references); build a clean, provenance-tagged text corpus.

**Labs (hands-on) — 14 h:**

| # | Lab | h |
|---|-----|---|
| 18a | Extract text from a born-digital medical PDF (PyMuPDF) | 3 |
| 18b | OCR a scanned page; measure & clean errors (Tesseract / doc model) | 4 |
| 18c | Layout-aware parsing (unstructured/Nougat/Marker) into sections | 4 |
| 18d | Build a provenance-tagged text corpus (page/section metadata) | 3 |

**Datasets/tools:** licensed/open medical texts; PyMuPDF, Tesseract, unstructured/Nougat/Marker.
**Assessment:** ingestion pipeline + corpus (**60%**); OCR-quality report (**20%**); quiz (**20%**).
**Key decisions:** born-digital vs. scanned handling; OCR engine; how much structure to preserve; **licensing (owned/licensed sources only)**.
**References:** plan §6; §13.
**Hours:** Theory **8** + Lab **14** = **22**.
