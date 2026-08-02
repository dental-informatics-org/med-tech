# Volume III · Chapter 13 — Vector Databases & Knowledge Storage · Theory

> Source: split from `med-tech-curriculum-V1.md` (V1). From this split onward this chapter is maintained **independently** here. See `Volume-III-Chapter-13-context.md` for the AI interaction log.

**Prerequisites:** Ch 12.

**Learning outcomes — the student can:** explain embeddings storage and ANN search; use Chroma/FAISS (and know Weaviate/Pinecone); design metadata & filtering; reason about where knowledge lives in hardware (RAM/NVMe) and how it scales.

**Topics (theory) — 8 h:**

| # | Topic | h |
|---|-------|---|
| 13.1 | Vector embeddings & similarity metrics (cosine, dot, L2) | 1 |
| 13.2 | ANN indexes: HNSW, IVF; recall vs. speed | 2 |
| 13.3 | Vector DBs compared: Chroma, Weaviate, Pinecone, FAISS | 2 |
| 13.4 | Metadata, filtering & hybrid (keyword+vector) search | 1 |
| 13.5 | Where knowledge lives: RAM vs. NVMe; persistence; scaling | 2 |

**Datasets/tools:** Chroma, FAISS, Weaviate (optional); embeddings model.
**Assessment:** vector-store lab (**50%**); benchmark report (**30%**); quiz (**20%**).
**Key decisions:** which vector DB; index type vs. recall/latency; RAM vs. disk; managed vs. local.
**References:** plan §13 → *RAG, vector databases & local inference*.
**Hours:** Theory **8** + Lab **12** = **20**.
