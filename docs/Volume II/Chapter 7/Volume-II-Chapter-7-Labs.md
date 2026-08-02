# Volume II · Chapter 7 — The Hugging Face Ecosystem · Labs

> Source: split from `med-tech-curriculum-V1.md` (V1). From this split onward this chapter is maintained **independently** here. See `Volume-II-Chapter-7-context.md` for the AI interaction log.

**Prerequisites:** Ch 6.

**Learning outcomes — the student can:** navigate the Hub; use `transformers` pipelines and `AutoModel`/`AutoTokenizer`; load and process data with `datasets`; run efficient inference; manage models and licenses locally.

**Labs (hands-on) — 12 h:**

| # | Lab | h |
|---|-----|---|
| 7a | Load a biomedical model via `pipeline`; run NER/classification | 3 |
| 7b | Load & preprocess a medical dataset with `datasets` (map/tokenize) | 3 |
| 7c | Batch inference over a clinical corpus; save outputs | 3 |
| 7d | Build a small reproducible inference script + pinned environment | 3 |

**Datasets/tools:** HF `transformers`, `datasets`, `evaluate`; PubMedBERT and similar.
**Assessment:** inference-pipeline deliverable (**50%**); dataset-processing lab (**30%**); quiz (**20%**).
**Key decisions:** model choice/license; precision vs. memory; streaming vs. in-memory datasets.
**References:** plan §13 → *Transformers & the Hugging Face ecosystem*.
**Hours:** Theory **8** + Lab **12** = **20**.
