# Volume III · Chapter 12 — Retrieval-Augmented Generation (RAG) · Labs

> Source: split from `med-tech-curriculum-V1.md` (V1). From this split onward this chapter is maintained **independently** here. See `Volume-III-Chapter-12-context.md` for the AI interaction log.

**Prerequisites:** Ch 7, Ch 8, Ch 11.

**Learning outcomes — the student can:** explain RAG architecture; build an ingest→embed→retrieve→generate pipeline; ground answers with citations; evaluate retrieval and answer faithfulness; reduce hallucination.

**Labs (hands-on) — 18 h:**

| # | Lab | h |
|---|-----|---|
| 12a | Build a basic RAG over clinical guidelines (ingest→embed→retrieve→answer) | 5 |
| 12b | Chunking experiments: compare strategies on retrieval quality | 3 |
| 12c | Add citations/provenance to answers | 3 |
| 12d | Evaluate RAG: retrieval recall + faithfulness scoring | 4 |
| 12e | Add reranking / hybrid search; measure improvement | 3 |

**Datasets/tools:** LangChain/LlamaIndex or custom; embeddings model; Chroma; local LLM.
**Assessment:** working RAG system (**60%**); eval report (**20%**); quiz (**20%**).
**Key decisions:** chunk size/overlap; embedding model; RAG vs. fine-tune; citation strategy.
**References:** plan §13 → *RAG, vector databases & local inference*.
**Hours:** Theory **12** + Lab **18** = **30**.
