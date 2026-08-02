# Volume III · Chapter 12 — Retrieval-Augmented Generation (RAG) · Theory

> Source: split from `med-tech-curriculum-V1.md` (V1). From this split onward this chapter is maintained **independently** here. See `Volume-III-Chapter-12-context.md` for the AI interaction log.

**Prerequisites:** Ch 7, Ch 8, Ch 11.

**Learning outcomes — the student can:** explain RAG architecture; build an ingest→embed→retrieve→generate pipeline; ground answers with citations; evaluate retrieval and answer faithfulness; reduce hallucination.

**Topics (theory) — 12 h:**

| # | Topic | h |
|---|-------|---|
| 12.1 | Why RAG; grounding vs. parametric knowledge | 1 |
| 12.2 | RAG architecture: retriever + generator; the pipeline | 2 |
| 12.3 | Chunking strategies for clinical documents | 2 |
| 12.4 | Embeddings & similarity search fundamentals | 2 |
| 12.5 | Prompt assembly, context windows, citation/provenance | 2 |
| 12.6 | RAG evaluation: retrieval metrics + answer faithfulness | 2 |
| 12.7 | Advanced: reranking, hybrid search, query rewriting | 1 |

**Datasets/tools:** LangChain/LlamaIndex or custom; embeddings model; Chroma; local LLM.
**Assessment:** working RAG system (**60%**); eval report (**20%**); quiz (**20%**).
**Key decisions:** chunk size/overlap; embedding model; RAG vs. fine-tune; citation strategy.
**References:** plan §13 → *RAG, vector databases & local inference*.
**Hours:** Theory **12** + Lab **18** = **30**.
