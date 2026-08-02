# Volume III · Chapter 13 — Vector Databases & Knowledge Storage · Labs

> Source: split from `med-tech-curriculum-V1.md` (V1). From this split onward this chapter is maintained **independently** here. See `Volume-III-Chapter-13-context.md` for the AI interaction log.

**Prerequisites:** Ch 12.

**Learning outcomes — the student can:** explain embeddings storage and ANN search; use Chroma/FAISS (and know Weaviate/Pinecone); design metadata & filtering; reason about where knowledge lives in hardware (RAM/NVMe) and how it scales.

**Labs (hands-on) — 12 h:**

| # | Lab | h |
|---|-----|---|
| 13a | Build & query a Chroma collection with metadata filters | 3 |
| 13b | Compare FAISS index types (recall/speed) | 3 |
| 13c | Persist & reload a vector store; measure memory footprint | 3 |
| 13d | Hybrid search: combine BM25 + vectors | 3 |

**Datasets/tools:** Chroma, FAISS, Weaviate (optional); embeddings model.
**Assessment:** vector-store lab (**50%**); benchmark report (**30%**); quiz (**20%**).
**Key decisions:** which vector DB; index type vs. recall/latency; RAM vs. disk; managed vs. local.
**References:** plan §13 → *RAG, vector databases & local inference*.
**Hours:** Theory **8** + Lab **12** = **20**.
