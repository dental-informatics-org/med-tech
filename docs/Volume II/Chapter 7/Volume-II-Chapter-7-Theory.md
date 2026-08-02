# Volume II · Chapter 7 — The Hugging Face Ecosystem · Theory

> Source: split from `med-tech-curriculum-V1.md` (V1). From this split onward this chapter is maintained **independently** here. See `Volume-II-Chapter-7-context.md` for the AI interaction log.

**Prerequisites:** Ch 6.

**Learning outcomes — the student can:** navigate the Hub; use `transformers` pipelines and `AutoModel`/`AutoTokenizer`; load and process data with `datasets`; run efficient inference; manage models and licenses locally.

**Topics (theory) — 8 h:**

| # | Topic | h |
|---|-------|---|
| 7.1 | The Hub: models, datasets, spaces; model cards & licenses | 1 |
| 7.2 | `transformers`: pipelines, `AutoModel`/`AutoTokenizer`, config | 2 |
| 7.3 | `datasets`: loading, `map`, streaming | 2 |
| 7.4 | Tokenizers, batching, padding/truncation | 1 |
| 7.5 | Inference: CPU/GPU, half precision, device management | 1 |
| 7.6 | The `evaluate` library & metrics basics | 1 |

**Datasets/tools:** HF `transformers`, `datasets`, `evaluate`; PubMedBERT and similar.
**Assessment:** inference-pipeline deliverable (**50%**); dataset-processing lab (**30%**); quiz (**20%**).
**Key decisions:** model choice/license; precision vs. memory; streaming vs. in-memory datasets.
**References:** plan §13 → *Transformers & the Hugging Face ecosystem*.
**Hours:** Theory **8** + Lab **12** = **20**.
