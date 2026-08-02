# Volume I · Chapter 1 — Python for Data Science (NumPy, Pandas, Matplotlib) · Theory

> Source: split from `med-tech-curriculum-V1.md` (V1). From this split onward this chapter is maintained **independently** here. See `Volume-I-Chapter-1-context.md` for the AI interaction log.

**Prerequisites:** basic Python (entry skill for the program — variables, control flow, functions, lists/dicts).

**Learning outcomes — the student can:**
- Manipulate numerical data efficiently with **NumPy** (vectorization, broadcasting, indexing, aggregation).
- Load, clean, transform, and join tabular **clinical data** with **Pandas** (missing values, types, dates, categoricals, merges, groupby).
- Perform basic **feature engineering** to build a modeling-ready table from raw EHR-style data.
- Produce clear exploratory **visualizations** with Matplotlib (distributions, cohort comparisons, missingness).
- Work in **reproducible, well-structured notebooks** with sound data hygiene.

**Topics (theory) — 12 h:**

| # | Topic | h |
|---|-------|---|
| 1.1 | Python for data work: environment (Anaconda/conda), Jupyter, reproducibility | 1 |
| 1.2 | NumPy: `ndarray`, vectorization, broadcasting, indexing/slicing, aggregation | 3 |
| 1.3 | Pandas I: `Series`/`DataFrame`, I/O (CSV/Parquet), indexing & selection | 2 |
| 1.4 | Pandas II: cleaning — missing data, dtypes, dates, categoricals, merges/joins, `groupby` | 3 |
| 1.5 | Feature engineering for clinical/tabular data | 1 |
| 1.6 | Matplotlib (and pandas plotting): distributions, correlations, time series | 1 |
| 1.7 | Reproducible, well-structured notebooks & data hygiene | 1 |

**Datasets/tools:** synthetic EHR CSVs (or a Synthea export); NumPy, Pandas, Matplotlib, Jupyter; conda/Anaconda environment.

**Assessment:** notebook deliverable — a cleaned dataset + short EDA report (rubric, **60%**); quiz on NumPy/Pandas idioms (**20%**); feature-engineering task producing a modeling table (**20%**).

**Key decisions taught here:**
- NumPy vs. Pandas for a given operation (raw arrays vs. labeled tables).
- **Wide vs. long** data format for clinical time series.
- Handling missing clinical data — **impute vs. drop** — and its **clinical implications** (bias, leakage).
- Reproducibility choices (environment pinning, deterministic notebooks).

**References:** plan §13 → *Programming & data science*.

**Hours:** Theory **12** + Lab **18** = **30**. *(Feeds plan Lab 1 — EHR Data Wrangling.)*
