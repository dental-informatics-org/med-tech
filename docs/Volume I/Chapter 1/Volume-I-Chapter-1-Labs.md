# Volume I · Chapter 1 — Python for Data Science (NumPy, Pandas, Matplotlib) · Labs

> Source: split from `med-tech-curriculum-V1.md` (V1). From this split onward this chapter is maintained **independently** here. See `Volume-I-Chapter-1-context.md` for the AI interaction log.

**Prerequisites:** basic Python (entry skill for the program — variables, control flow, functions, lists/dicts).

**Learning outcomes — the student can:**
- Manipulate numerical data efficiently with **NumPy** (vectorization, broadcasting, indexing, aggregation).
- Load, clean, transform, and join tabular **clinical data** with **Pandas** (missing values, types, dates, categoricals, merges, groupby).
- Perform basic **feature engineering** to build a modeling-ready table from raw EHR-style data.
- Produce clear exploratory **visualizations** with Matplotlib (distributions, cohort comparisons, missingness).
- Work in **reproducible, well-structured notebooks** with sound data hygiene.

**Labs (hands-on) — 18 h:**

| # | Lab | h |
|---|-----|---|
| 1a | NumPy warm-up: vitals array computations, vectorized normalization/z-scores | 3 |
| 1b | Load & explore a synthetic EHR CSV in Pandas; basic profiling/EDA | 3 |
| 1c | Data cleaning: missing values, dtype fixes, date parsing, deduplication | 4 |
| 1d | Merge multi-table EHR (patients / encounters / labs); `groupby` aggregations | 3 |
| 1e | Feature engineering: build a per-patient modeling table | 3 |
| 1f | Visualization: distributions, cohort comparison, missingness heatmap | 2 |

**Datasets/tools:** synthetic EHR CSVs (or a Synthea export); NumPy, Pandas, Matplotlib, Jupyter; conda/Anaconda environment.

**Assessment:** notebook deliverable — a cleaned dataset + short EDA report (rubric, **60%**); quiz on NumPy/Pandas idioms (**20%**); feature-engineering task producing a modeling table (**20%**).

**Key decisions taught here:**
- NumPy vs. Pandas for a given operation (raw arrays vs. labeled tables).
- **Wide vs. long** data format for clinical time series.
- Handling missing clinical data — **impute vs. drop** — and its **clinical implications** (bias, leakage).
- Reproducibility choices (environment pinning, deterministic notebooks).

**References:** plan §13 → *Programming & data science*.

**Hours:** Theory **12** + Lab **18** = **30**. *(Feeds plan Lab 1 — EHR Data Wrangling.)*
