# Med-Tech Curriculum — V1

> **Companion to [`med-tech-plan-V1.md`](med-tech-plan-V1.md).** The plan is the master/architecture document (vision, volumes, chapter map, hour budget, conventions). **This file holds the fully-expanded, formal chapter definitions** — each chapter filled out to the §2.5 template using the §2.6 worked example as the standard, with the real topic list and per-topic theory/lab hours.

- **Status:** V1 — **all 27 chapters expanded** (first pass). Pending pedagogical review of content and hours.
- **Source of structure:** `med-tech-plan-V1.md` §2.3 (Volume & Chapter map) and §2.5 (chapter template).
- **Hour figures:** theory (T) = lecture/seminar contact hours; lab (L) = supervised hands-on hours. Per-topic hours **sum to the chapter budget** in the plan's §2.3. Figures remain **provisional** until reviewed.
- **Progress:** **Complete — Volumes I–V, Chapters 1–27** (see per-volume summaries and the program grand total at the end). Core (I–IV) = 542 h; with elective Vol V = 646 h.

---

# Volume I — Foundations & Clinical Data Engineering *(Phase 0)*

Chapters 1–5. Volume budget: **T 58 h + L 66 h = 124 h**.

---

## Chapter 1 — Python for Data Science (NumPy, Pandas, Matplotlib) · [Volume I]

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

---

## Chapter 2 — Foundations of Clinical Data (EHR; code sets; privacy) · [Volume I]

**Prerequisites:** Ch 1 (Python/Pandas).

**Learning outcomes — the student can:**
- Describe **EHR structure** and its core data domains, and distinguish structured vs. unstructured data.
- Navigate and **map medical code sets** — ICD-10-CM/PCS, CPT/HCPCS, SNOMED CT, LOINC — to the right purpose.
- Explain **data privacy/regulation** (HIPAA, GDPR) and what makes clinical data identifiable.
- Apply basic **de-identification** and justify **synthetic-data** use for development.

**Topics (theory) — 10 h:**

| # | Topic | h |
|---|-------|---|
| 2.1 | The EHR: data domains (demographics, encounters, dx, procedures, meds, labs, vitals, notes); structured vs. unstructured | 2 |
| 2.2 | Diagnosis & procedure code sets: ICD-10-CM/PCS, CPT/HCPCS | 2 |
| 2.3 | Clinical terminologies: SNOMED CT (concepts/hierarchies), LOINC (labs) | 2 |
| 2.4 | Mapping, crosswalks & value sets between terminologies | 1 |
| 2.5 | Privacy & regulation: HIPAA (PHI, Safe Harbor / Expert Determination), GDPR (special-category data, lawful basis) | 2 |
| 2.6 | De-identification, synthetic data & data-governance basics | 1 |

**Labs (hands-on) — 6 h:**

| # | Lab | h |
|---|-----|---|
| 2a | Explore an EHR schema; classify fields into data domains; structured vs. unstructured | 2 |
| 2b | Code lookup & mapping: build a small ICD-10 ↔ SNOMED ↔ LOINC crosswalk in Pandas | 2 |
| 2c | De-identification: apply HIPAA Safe Harbor (18 identifiers) to a synthetic dataset; verify | 2 |

**Datasets/tools:** synthetic EHR; public browsers (ICD-10, SNOMED CT browser, LOINC search); Pandas.

**Assessment:** quiz on code sets & privacy (**40%**); crosswalk deliverable (**30%**); de-identification lab rubric (**30%**).

**Key decisions:** which terminology fits which purpose; when data is/ isn't de-identified; **synthetic vs. real** data for development.

**References:** plan §13 → *Clinical data, code sets & privacy*.

**Hours:** Theory **10** + Lab **6** = **16**.

---

## Chapter 3 — Healthcare Interoperability (HL7 v2, CDA/C-CDA, FHIR, SMART-on-FHIR) · [Volume I]

> Migrated from plan §2.6 (the template worked example).

**Prerequisites:** Ch 1 (Python/Pandas), Ch 2 (clinical data & code sets).

**Learning outcomes — the student can:**
- Explain how clinical data is **exchanged** (not just stored) and why it is the backbone of medical AI.
- **Read and parse** an HL7 v2 message and a C-CDA document into structured data.
- Model clinical data as **FHIR resources** and query a FHIR server via its **REST API** from Python.
- **Bind** data to standard terminologies (ICD/SNOMED/LOINC) and describe a **SMART-on-FHIR** integration.

**Topics (theory) — 12 h:**

| # | Topic | h |
|---|-------|---|
| 3.1 | Why interoperability matters; the data backbone of medical-AI products | 1 |
| 3.2 | HL7 v2.x messaging: segments, trigger events (ADT/ORM/ORU), pipe-delimited format | 2 |
| 3.3 | HL7 CDA & C-CDA: XML clinical documents, templates, sections | 2 |
| 3.4 | FHIR fundamentals: resources, references, bundles, data types | 3 |
| 3.5 | FHIR REST API: search, read, CRUD, versioning, pagination | 2 |
| 3.6 | Terminology binding in FHIR (ICD/SNOMED/LOINC); profiles & conformance | 1 |
| 3.7 | SMART-on-FHIR & app integration; OAuth scopes, security basics | 1 |

**Labs (hands-on) — 16 h:**

| # | Lab | h |
|---|-----|---|
| 3a | Parse an HL7 v2 message with `hl7apy` into structured fields | 3 |
| 3b | Read a C-CDA document; extract problems / medications / allergies | 3 |
| 3c | Stand up a HAPI FHIR server and load Synthea synthetic patients | 3 |
| 3d | Query the FHIR REST API from Python; Patient/Observation/Condition → Pandas | 4 |
| 3e | Build a patient-summary extractor over FHIR (mini SMART-on-FHIR read flow) | 3 |

**Datasets/tools:** Synthea synthetic patients; HAPI FHIR (public sandbox or local); Python `hl7apy`, `fhir.resources`/`fhirclient`, `requests`, Pandas; sample C-CDA XML.

**Assessment:** quiz on standards (**20%**); lab rubric on 3a–3e (**50%**); a "clinical data → tidy DataFrame" deliverable from a FHIR bundle (**30%**).

**Key decisions:** FHIR vs. HL7 v2 for a new integration; **document (CDA) vs. resource (FHIR)** models; how much to normalize/terminology-map before feeding an AI pipeline.

**References:** plan §13 → *Interoperability standards*.

**Hours:** Theory **12** + Lab **16** = **28**.

---

## Chapter 4 — Core Machine Learning for Medicine · [Volume I]

**Prerequisites:** Ch 1 (NumPy/Pandas), Ch 2 (clinical data).

**Learning outcomes — the student can:**
- Frame a clinical problem as **supervised or unsupervised** ML and build/train/evaluate models with **scikit-learn**.
- Apply a rigorous **workflow** (train/val/test, cross-validation) and avoid **data leakage**.
- Choose and **interpret clinically appropriate metrics** (sensitivity/specificity, PPV/NPV, ROC-AUC, PR-AUC, calibration).
- Use **unsupervised** methods (clustering, PCA) for **patient stratification**, and recognize imbalance/bias issues.

**Topics (theory) — 14 h:**

| # | Topic | h |
|---|-------|---|
| 4.1 | ML framing for medicine: supervised vs. unsupervised; clinical use cases | 1 |
| 4.2 | The ML workflow: train/validation/test, cross-validation, data leakage | 2 |
| 4.3 | Supervised I: logistic regression, linear models, regularization | 2 |
| 4.4 | Supervised II: decision trees, random forests, gradient boosting | 2 |
| 4.5 | Evaluation & metrics: confusion matrix, sensitivity/specificity/PPV/NPV, ROC-AUC, PR-AUC, calibration | 3 |
| 4.6 | Class imbalance, thresholds & clinical decision trade-offs | 1 |
| 4.7 | Unsupervised: clustering (k-means, hierarchical) + PCA for stratification | 2 |
| 4.8 | Overfitting, bias/variance & model selection | 1 |

**Labs (hands-on) — 16 h:**

| # | Lab | h |
|---|-----|---|
| 4a | Build a readmission classifier (logistic regression) with a proper train/test split | 3 |
| 4b | Random forest / gradient boosting on the same task; compare; feature importance | 3 |
| 4c | Evaluation deep-dive: ROC/PR curves, calibration, clinical threshold selection | 3 |
| 4d | Cross-validation & hyperparameter tuning; leakage checks | 3 |
| 4e | Unsupervised patient stratification: clustering + PCA visualization | 4 |

**Datasets/tools:** synthetic structured EHR; scikit-learn, Pandas, Matplotlib.

**Assessment:** modeling project — build + evaluate a classifier with written interpretation (**50%**); evaluation/metrics lab rubric (**30%**); quiz (**20%**).

**Key decisions:** metric choice for the clinical question; **sensitivity vs. specificity** trade-off; complexity vs. **interpretability**; handling imbalance; avoiding leakage.

**References:** plan §13 → *Programming & data science*; *Clinical datasets*.

**Hours:** Theory **14** + Lab **16** = **30**. *(Feeds plan Lab 2 — Simple Clinical Classifier.)*

---

## Chapter 5 — Medical NLP Basics (regex → embeddings) · [Volume I]

**Prerequisites:** Ch 1 (Python/Pandas).

**Learning outcomes — the student can:**
- Process clinical free text with **classical NLP** (tokenization, normalization, TF-IDF).
- Build **regex/rule-based extractors** for clinical concepts and detect **negation**.
- Use **word embeddings** (general and biomedical) and build a simple clinical **text classifier**.
- Articulate the **limits of classical NLP** (context, negation) that motivate transformers (bridge to Volume II).

**Topics (theory) — 10 h:**

| # | Topic | h |
|---|-------|---|
| 5.1 | Clinical text: characteristics & challenges (abbreviations, negation, jargon) | 1 |
| 5.2 | Preprocessing: tokenization, normalization, stopwords, stemming/lemmatization | 2 |
| 5.3 | Regular expressions for clinical information extraction | 2 |
| 5.4 | Representations: bag-of-words, TF-IDF | 1 |
| 5.5 | Word embeddings: word2vec/GloVe; biomedical embeddings | 2 |
| 5.6 | Simple text classification, basic NER & negation detection (e.g., NegEx) | 1 |
| 5.7 | Limits of classical NLP → why transformers (bridge to Volume II) | 1 |

**Labs (hands-on) — 10 h:**

| # | Lab | h |
|---|-----|---|
| 5a | Preprocess clinical notes: tokenize, normalize, build a clean corpus | 2 |
| 5b | Regex extractor: pull vitals / medications / dates from clinical text | 3 |
| 5c | TF-IDF + logistic regression: classify clinical note type/intent | 3 |
| 5d | Explore word embeddings: nearest neighbors on biomedical terms | 2 |

**Datasets/tools:** synthetic/de-identified clinical notes; Python `re`, scikit-learn, spaCy/NLTK, gensim or pretrained biomedical embeddings.

**Assessment:** regex extractor deliverable — rubric (**40%**); text-classification lab (**40%**); quiz (**20%**).

**Key decisions:** rule-based vs. statistical NLP; when regex suffices vs. needs ML; **general vs. biomedical** embeddings; handling **negation/context**.

**References:** plan §13 → *Transformers & the Hugging Face ecosystem* (bridge); *Programming & data science*.

**Hours:** Theory **10** + Lab **10** = **20**.

---

### Volume I — completion summary

| Ch | Title | T | L | Total |
|----|-------|---|---|-------|
| 1 | Python for Data Science | 12 | 18 | 30 |
| 2 | Foundations of Clinical Data | 10 | 6 | 16 |
| 3 | Healthcare Interoperability | 12 | 16 | 28 |
| 4 | Core Machine Learning for Medicine | 14 | 16 | 30 |
| 5 | Medical NLP Basics | 10 | 10 | 20 |
| | **Volume I total** | **58** | **66** | **124** |

*Matches the plan §2.3 budget.* ✔

---

# Volume II — The LLM Era *(Phase 1)*

Chapters 6–11. Volume budget: **T 56 h + L 62 h = 118 h**.

---

## Chapter 6 — Transformer Architecture & Self-Attention · [Volume II]

**Prerequisites:** Ch 4 (ML), Ch 5 (NLP basics).

**Learning outcomes — the student can:** explain self-attention and the transformer block; describe tokenization, embeddings and positional encoding; distinguish encoder/decoder/encoder-decoder families; read a model card and reason about parameters/context length.

**Topics (theory) — 12 h:**

| # | Topic | h |
|---|-------|---|
| 6.1 | From embeddings to context; limits of classical NLP | 1 |
| 6.2 | Tokenization & subwords (BPE, WordPiece) | 2 |
| 6.3 | Self-attention & multi-head attention | 3 |
| 6.4 | The transformer block: FFN, residuals, layer norm, positional encoding | 2 |
| 6.5 | Architectures: encoder (BERT), decoder (GPT), encoder-decoder (T5) | 2 |
| 6.6 | Pretraining objectives (MLM, causal LM) & scaling intuition | 1 |
| 6.7 | Reading model cards: parameters, context length, tokens | 1 |

**Labs (hands-on) — 6 h:**

| # | Lab | h |
|---|-----|---|
| 6a | Tokenization exploration: tokenize clinical text, inspect subwords & token counts | 2 |
| 6b | Visualize attention weights on a clinical sentence | 2 |
| 6c | Run inference with a small pretrained transformer; extract embeddings | 2 |

**Datasets/tools:** Hugging Face `transformers`; a small BERT/GPT; clinical text samples.
**Assessment:** architecture quiz (**50%**); attention-visualization writeup (**30%**); tokenization exercise (**20%**).
**Key decisions:** encoder vs. decoder for a task; context length vs. cost; tokenizer choice.
**References:** plan §13 → *Transformers & the Hugging Face ecosystem*.
**Hours:** Theory **12** + Lab **6** = **18**.

---

## Chapter 7 — The Hugging Face Ecosystem · [Volume II]

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

---

## Chapter 8 — Prompt Engineering for Medicine · [Volume II]

**Prerequisites:** Ch 7.

**Learning outcomes — the student can:** design effective prompts (zero/few-shot, chain-of-thought); produce structured outputs; assess reliability and hallucination; apply basic safety/injection awareness in clinical apps.

**Topics (theory) — 8 h:**

| # | Topic | h |
|---|-------|---|
| 8.1 | Prompting fundamentals: zero/few-shot, roles, instructions | 2 |
| 8.2 | Chain-of-thought & reasoning prompts | 1 |
| 8.3 | Structured outputs (JSON, schemas), constrained generation | 1 |
| 8.4 | Retrieval-grounded prompting (intro to the RAG idea) | 1 |
| 8.5 | Reliability, hallucination & self-consistency; when NOT to trust | 2 |
| 8.6 | Safety & prompt-injection awareness in clinical apps | 1 |

**Labs (hands-on) — 10 h:**

| # | Lab | h |
|---|-----|---|
| 8a | Prompt iteration on a clinical QA task; zero- vs. few-shot | 3 |
| 8b | Chain-of-thought vs. direct on clinical reasoning; measure | 2 |
| 8c | Structured extraction: prompt an LLM to output a JSON clinical summary | 3 |
| 8d | Hallucination probe: design tests, log failures | 2 |

**Datasets/tools:** local LLM via Ollama (MedGemma) or HF; Python.
**Assessment:** prompt-portfolio deliverable (**50%**); structured-extraction lab (**30%**); quiz (**20%**).
**Key decisions:** prompting vs. fine-tuning vs. RAG; how to measure reliability; guardrails.
**References:** plan §13 → *Medical LLMs*.
**Hours:** Theory **8** + Lab **10** = **18**.

---

## Chapter 9 — Medical Domain Adaptation · [Volume II]

**Prerequisites:** Ch 7, Ch 8.

**Learning outcomes — the student can:** distinguish continued pretraining vs. fine-tuning vs. instruction tuning; explain how Meditron/Clinical-Camel/MedGemma were adapted; choose an adaptation strategy; reason about data requirements and licensing.

**Topics (theory) — 10 h:**

| # | Topic | h |
|---|-------|---|
| 9.1 | Why adapt general LLMs to medicine; gaps & risks | 1 |
| 9.2 | Continued pretraining on biomedical corpora | 2 |
| 9.3 | Supervised fine-tuning & instruction tuning | 2 |
| 9.4 | Case studies: Meditron, Clinical-Camel, MedGemma, PubMedBERT | 2 |
| 9.5 | Data: sources, curation, quality, licensing for medical corpora | 2 |
| 9.6 | Choosing an adaptation strategy vs. RAG (decision framework) | 1 |

**Labs (hands-on) — 6 h:**

| # | Lab | h |
|---|-----|---|
| 9a | Compare a general vs. domain-adapted model on medical prompts | 2 |
| 9b | Prepare a small biomedical instruction dataset (format, clean) | 2 |
| 9c | Design an adaptation plan for a chosen clinical use case | 2 |

**Datasets/tools:** HF models (Meditron/MedGemma/PubMedBERT), `datasets`.
**Assessment:** adaptation-plan deliverable (**50%**); comparison lab (**30%**); quiz (**20%**).
**Key decisions:** pretrain vs. fine-tune vs. RAG; data licensing; base-model choice.
**References:** plan §13 → *Medical LLMs*; *Fine-tuning, alignment & benchmarks*.
**Hours:** Theory **10** + Lab **6** = **16**.

---

## Chapter 10 — Benchmarking & Hallucination · [Volume II]

**Prerequisites:** Ch 8, Ch 9.

**Learning outcomes — the student can:** evaluate LLMs on medical benchmarks (MedQA/PubMedQA/MedMCQA); interpret results; measure hallucination; build an eval harness; explain why benchmark ≠ clinical safety.

**Topics (theory) — 8 h:**

| # | Topic | h |
|---|-------|---|
| 10.1 | Benchmark landscape: MedQA (USMLE), PubMedQA, MedMCQA | 2 |
| 10.2 | Metrics: accuracy, exact-match & their limits | 1 |
| 10.3 | Hallucination: definitions, causes, measurement | 2 |
| 10.4 | Faithfulness & grounding metrics | 1 |
| 10.5 | Benchmark ≠ clinical safety; distribution shift | 2 |

**Labs (hands-on) — 8 h:**

| # | Lab | h |
|---|-----|---|
| 10a | Run a model on a MedQA-style set; compute accuracy | 3 |
| 10b | Build a small eval harness with the `evaluate` library | 2 |
| 10c | Hallucination test: craft adversarial clinical prompts, score | 3 |

**Datasets/tools:** HF `datasets`/`evaluate`; local LLM.
**Assessment:** eval-harness deliverable (**50%**); hallucination report (**30%**); quiz (**20%**).
**Key decisions:** which benchmark supports which claim; honest reporting of limitations.
**References:** plan §13 → *Fine-tuning, alignment & benchmarks*; *Medical LLMs*.
**Hours:** Theory **8** + Lab **8** = **16**.

---

## Chapter 11 — First Fine-Tunes (PubMedBERT, QLoRA, local MedGemma/Ollama) · [Volume II]

**Prerequisites:** Ch 7–10.

**Learning outcomes — the student can:** fine-tune a biomedical BERT for classification; apply QLoRA to fine-tune a small generative LLM on medical QA; run models locally via Ollama; evaluate a fine-tune and write a model card.

**Topics (theory) — 10 h:**

| # | Topic | h |
|---|-------|---|
| 11.1 | Fine-tuning mechanics: heads, learning rate, epochs, overfitting | 2 |
| 11.2 | Parameter-efficient fine-tuning: LoRA & QLoRA (quantization) | 3 |
| 11.3 | Datasets for fine-tuning: formatting, splits, tokenization | 1 |
| 11.4 | Local deployment: Ollama, GGUF, quantization levels | 2 |
| 11.5 | Evaluating a fine-tuned medical model; avoiding leakage | 1 |
| 11.6 | Compute & memory budgeting on consumer GPUs | 1 |

**Labs (hands-on) — 20 h:**

| # | Lab | h |
|---|-----|---|
| 11a | Fine-tune PubMedBERT for clinical-question intent classification | 5 |
| 11b | Prepare a medical QA dataset for generative fine-tuning | 3 |
| 11c | QLoRA fine-tune a small Llama/GPT-2 on medical QA | 6 |
| 11d | Run MedGemma locally via Ollama; compare base vs. fine-tuned | 3 |
| 11e | Evaluate the fine-tune (quant + qual) & write a model card | 3 |

**Datasets/tools:** HF `transformers`/`peft`/`bitsandbytes`, QLoRA, Ollama, MedGemma; GPU workstation.
**Assessment:** fine-tuned model + model card (**60%**); eval report (**20%**); quiz (**20%**).
**Key decisions:** full vs. PEFT fine-tuning; quantization level vs. quality; base model/size vs. hardware.
**References:** plan §13 → *Fine-tuning…*; *Medical LLMs*; *…local inference*.
**Hours:** Theory **10** + Lab **20** = **30**.

---

### Volume II — completion summary

| Ch | Title | T | L | Total |
|----|-------|---|---|-------|
| 6 | Transformer Architecture & Self-Attention | 12 | 6 | 18 |
| 7 | The Hugging Face Ecosystem | 8 | 12 | 20 |
| 8 | Prompt Engineering for Medicine | 8 | 10 | 18 |
| 9 | Medical Domain Adaptation | 10 | 6 | 16 |
| 10 | Benchmarking & Hallucination | 8 | 8 | 16 |
| 11 | First Fine-Tunes | 10 | 20 | 30 |
| | **Volume II total** | **56** | **62** | **118** |

*Matches the plan §2.3 budget.* ✔

---

# Volume III — Autonomous Medical AI Systems *(Phase 2)*

Chapters 12–17. Volume budget: **T 64 h + L 136 h = 200 h**.

---

## Chapter 12 — Retrieval-Augmented Generation (RAG) · [Volume III]

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

---

## Chapter 13 — Vector Databases & Knowledge Storage · [Volume III]

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

---

## Chapter 14 — Training Pipeline: Pre-training → Fine-tuning → Alignment (DPO) · [Volume III]

**Prerequisites:** Ch 11, Ch 12.

**Learning outcomes — the student can:** describe the full three-stage pipeline; reason about data/compute for pretraining; run domain fine-tuning; build preference data and apply DPO; compare RLHF vs. DPO; manage training runs with tracking.

**Topics (theory) — 16 h:**

| # | Topic | h |
|---|-------|---|
| 14.1 | The three-stage pipeline overview (pretrain→SFT→align) | 1 |
| 14.2 | Pretraining: data scale, objectives, tokenization, compute | 2 |
| 14.3 | Domain fine-tuning on medical corpora (e.g., MedFineWeb) | 2 |
| 14.4 | Instruction/supervised fine-tuning data design | 2 |
| 14.5 | Preference alignment: RLHF overview | 2 |
| 14.6 | Direct Preference Optimization (DPO): theory & practice | 3 |
| 14.7 | Safety alignment for medical outputs | 2 |
| 14.8 | Training infra: checkpoints, mixed precision, distributed basics, experiment tracking | 2 |

**Labs (hands-on) — 20 h:**

| # | Lab | h |
|---|-----|---|
| 14a | Continued pretraining (small) on a biomedical corpus | 5 |
| 14b | Build an SFT dataset & run supervised fine-tuning | 5 |
| 14c | Create a preference dataset (chosen/rejected) for a clinical behavior | 3 |
| 14d | Run DPO on the SFT model | 5 |
| 14e | Track experiments & compare stages (metrics, safety checks) | 2 |

**Datasets/tools:** HF `transformers`/`trl`/`peft`, DPO; experiment tracking (W&B or MLflow); GPU.
**Assessment:** aligned model across stages (**60%**); training report (**20%**); quiz (**20%**).
**Key decisions:** pretrain vs. fine-tune vs. align scope; DPO vs. RLHF; data quality vs. quantity; compute budget.
**References:** plan §13 → *Fine-tuning, alignment & benchmarks*; *Medical LLMs*; *Clinical datasets*.
**Hours:** Theory **16** + Lab **20** = **36**.

---

## Chapter 15 — Evaluation, Bias, Fairness & Clinical Safety · [Volume III]

**Prerequisites:** Ch 10, Ch 14.

**Learning outcomes — the student can:** design rigorous clinical evaluation; measure subgroup bias/fairness; assess calibration and safety (red-teaming); explain the benchmark-to-clinic gap; run clinician-in-the-loop evaluation.

**Topics (theory) — 12 h:**

| # | Topic | h |
|---|-------|---|
| 15.1 | Evaluation beyond accuracy: task-appropriate metrics | 2 |
| 15.2 | Bias & fairness: subgroup analysis, disparate performance | 2 |
| 15.3 | Calibration & uncertainty in clinical models | 2 |
| 15.4 | Safety: harmful outputs, refusal, red-teaming | 2 |
| 15.5 | Benchmark vs. clinical validity; prospective vs. retrospective | 2 |
| 15.6 | Human evaluation & clinician-in-the-loop protocols | 2 |

**Labs (hands-on) — 10 h:**

| # | Lab | h |
|---|-----|---|
| 15a | Subgroup fairness analysis on a clinical model | 3 |
| 15b | Calibration curves & reliability diagrams | 2 |
| 15c | Red-team a medical LLM; catalog failure modes | 3 |
| 15d | Design a human-eval rubric & run a mini study | 2 |

**Datasets/tools:** `evaluate`, fairness libraries; local LLM.
**Assessment:** safety/fairness eval report (**60%**); red-team catalog (**20%**); quiz (**20%**).
**Key decisions:** which subgroups & metrics; acceptable risk thresholds; when a model is **not** safe to deploy.
**References:** plan §13 → *Medical LLMs*; *Fine-tuning, alignment & benchmarks*.
**Hours:** Theory **12** + Lab **10** = **22**.

---

## Chapter 16 — Deployment, FHIR Integration & Compliance · [Volume III]

**Prerequisites:** Ch 12, Ch 15, Ch 3.

**Learning outcomes — the student can:** deploy models locally (Ollama/Open WebUI); build an inference API; integrate via FHIR (read/write, SMART-on-FHIR); monitor performance/drift; navigate the regulatory/compliance landscape.

**Topics (theory) — 10 h:**

| # | Topic | h |
|---|-------|---|
| 16.1 | Deployment options: local serving, Ollama, Open WebUI, APIs | 2 |
| 16.2 | Inference serving: latency, batching, quantization, scaling | 2 |
| 16.3 | FHIR integration & SMART-on-FHIR app model (read/write) | 2 |
| 16.4 | Monitoring, logging, drift & feedback loops | 2 |
| 16.5 | Regulatory & compliance landscape (SaMD, FDA/CE, HIPAA/GDPR at deployment) | 2 |

**Labs (hands-on) — 16 h:**

| # | Lab | h |
|---|-----|---|
| 16a | Deploy a model with Ollama + Open WebUI | 3 |
| 16b | Wrap the model in a REST inference API (FastAPI) | 4 |
| 16c | FHIR integration: read patient context, write results back | 5 |
| 16d | Add monitoring/logging & a drift check | 4 |

**Datasets/tools:** Ollama, Open WebUI, FastAPI, HAPI FHIR/Synthea; monitoring tools.
**Assessment:** deployed FHIR-integrated service (**60%**); monitoring setup (**20%**); quiz (**20%**).
**Key decisions:** local vs. cloud; API design; regulatory pathway; PHI handling at inference.
**References:** plan §13 → *…local inference*; *Interoperability standards*; *Clinical data, code sets & privacy*.
**Hours:** Theory **10** + Lab **16** = **26**.

---

## Chapter 17 — Capstone Project · [Volume III]

**Prerequisites:** all of Volumes I–III.

**Learning outcomes — the student can:** independently design, build, evaluate, and deploy an end-to-end medical-AI system for a real clinical problem; document decisions and safety; present with evidence to clinical stakeholders.

**Topics (theory) — 6 h:**

| # | Topic | h |
|---|-------|---|
| 17.1 | Scoping a clinical AI problem; requirements & success metrics | 2 |
| 17.2 | Project planning, data & licensing, risk/safety plan | 2 |
| 17.3 | Documentation, model cards & presenting to clinical stakeholders | 2 |

**Project (hands-on) — 60 h:**

| # | Milestone | h |
|---|-----------|---|
| 17a | Problem definition & data/knowledge sourcing | 8 |
| 17b | Build knowledge base / RAG pipeline | 12 |
| 17c | Train/adapt the model (QLoRA/DPO as needed) | 14 |
| 17d | Evaluation & safety/fairness assessment | 10 |
| 17e | Deploy locally with FHIR-style I/O (inference server) | 10 |
| 17f | Documentation, model card & final presentation | 6 |

**Example project:** "Clinical Trial Matching Assistant" (plan §5.2).
**Datasets/tools:** the full stack from Volumes I–III.
**Assessment:** end-to-end system (**50%**); evaluation & safety documentation (**25%**); presentation/defense (**25%**).
**Key decisions:** the full stack of trade-offs — RAG vs. fine-tune, hardware, scope vs. safety.
**References:** plan §5.2; §13 (all).
**Hours:** Theory **6** + Project **60** = **66**.

---

### Volume III — completion summary

| Ch | Title | T | L | Total |
|----|-------|---|---|-------|
| 12 | Retrieval-Augmented Generation (RAG) | 12 | 18 | 30 |
| 13 | Vector Databases & Knowledge Storage | 8 | 12 | 20 |
| 14 | Training Pipeline (pretrain→finetune→DPO) | 16 | 20 | 36 |
| 15 | Evaluation, Bias, Fairness & Clinical Safety | 12 | 10 | 22 |
| 16 | Deployment, FHIR Integration & Compliance | 10 | 16 | 26 |
| 17 | Capstone Project | 6 | 60 | 66 |
| | **Volume III total** | **64** | **136** | **200** |

*Matches the plan §2.3 budget.* ✔

---

# Volume IV — From Books to LLM *(Strategic §6)*

Chapters 18–22. Volume budget: **T 38 h + L 62 h = 100 h**.

---

## Chapter 18 — Ingestion, OCR & Document Understanding · [Volume IV]

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

---

## Chapter 19 — Figures & Multimodal Understanding · [Volume IV]

**Prerequisites:** Ch 18, Ch 7.

**Learning outcomes — the student can:** detect/extract figures; generate & curate captions with multimodal models; link images to text; make images retrievable; describe the SOTA and limits of medical image understanding.

**Topics (theory) — 8 h:**

| # | Topic | h |
|---|-------|---|
| 19.1 | Medical figures: radiology, histology, ECG, diagrams, charts | 1 |
| 19.2 | Figure detection & extraction from documents | 1 |
| 19.3 | Multimodal models (captioning, VQA): LLaVA-Med, MedGemma-multimodal | 2 |
| 19.4 | Image embeddings & multimodal retrieval | 2 |
| 19.5 | Linking figures to surrounding text & captions | 1 |
| 19.6 | SOTA & limits: reliability of medical image understanding | 1 |

**Labs (hands-on) — 14 h:**

| # | Lab | h |
|---|-----|---|
| 19a | Extract figures + captions from a medical document | 3 |
| 19b | Generate captions with a multimodal model; compare to originals | 4 |
| 19c | Multimodal retrieval: query text → return relevant figures | 4 |
| 19d | Link figures to text chunks; evaluate linkage quality | 3 |

**Datasets/tools:** multimodal HF models (LLaVA-Med/MedGemma), CLIP-style embeddings; vector DB.
**Assessment:** multimodal ingest+retrieval (**60%**); caption-quality report (**20%**); quiz (**20%**).
**Key decisions:** which multimodal model; how much to trust captions; image vs. caption embeddings.
**References:** plan §6; §13 → *Medical LLMs*.
**Hours:** Theory **8** + Lab **14** = **22**.

---

## Chapter 20 — Structuring, Provenance & Building the Corpus · [Volume IV]

**Prerequisites:** Ch 18, Ch 19.

**Learning outcomes — the student can:** semantically chunk book content; attach citations/provenance; build a versioned, updatable knowledge base; manage licensing/governance of sources.

**Topics (theory) — 6 h:**

| # | Topic | h |
|---|-------|---|
| 20.1 | Semantic chunking for books/atlases | 1 |
| 20.2 | Provenance model: book/edition/page/figure citations | 2 |
| 20.3 | Versioning & updatability of medical knowledge | 1 |
| 20.4 | Licensing, ownership & governance of source content | 2 |

**Labs (hands-on) — 12 h:**

| # | Lab | h |
|---|-----|---|
| 20a | Build a semantic chunker with citation metadata | 4 |
| 20b | Assemble a versioned knowledge base (text + figures) | 4 |
| 20c | Implement citation-traceable retrieval (answer → source page) | 4 |

**Datasets/tools:** vector DB; chunking libraries; a metadata store.
**Assessment:** cited knowledge base (**60%**); provenance audit (**20%**); quiz (**20%**).
**Key decisions:** chunk granularity; provenance schema; licensing compliance; update strategy.
**References:** plan §6; §13 → *RAG…*.
**Hours:** Theory **6** + Lab **12** = **18**.

---

## Chapter 21 — RAG-vs-Fine-tune Paths & Synthetic Data · [Volume IV]

**Prerequisites:** Ch 11, Ch 12, Ch 20.

**Learning outcomes — the student can:** decide between RAG and fine-tuning for book knowledge; generate quality-controlled synthetic Q&A/instruction data from sources; build image-text pairs; compare accuracy/hallucination of both paths.

**Topics (theory) — 8 h:**

| # | Topic | h |
|---|-------|---|
| 21.1 | Decision framework: RAG vs. fine-tune vs. both for book knowledge | 2 |
| 21.2 | Synthetic Q&A generation from source text (quality control) | 2 |
| 21.3 | Image-text pair construction for multimodal training | 1 |
| 21.4 | Risks: hallucinated synthetic data, contamination, licensing | 2 |
| 21.5 | Comparing paths: accuracy, faithfulness, cost | 1 |

**Labs (hands-on) — 16 h:**

| # | Lab | h |
|---|-----|---|
| 21a | Generate synthetic Q&A from a book chapter; QC filter | 4 |
| 21b | Fine-tune a small model on the synthetic set (QLoRA) | 5 |
| 21c | Build a RAG baseline over the same content | 3 |
| 21d | Head-to-head: accuracy & hallucination, RAG vs. fine-tune | 4 |

**Datasets/tools:** local LLM; HF `peft`/QLoRA; vector DB; eval harness.
**Assessment:** comparative study (**60%**); synthetic-data QC report (**20%**); quiz (**20%**).
**Key decisions:** RAG vs. fine-tune vs. both; synthetic-data quality gates; licensing of derived data.
**References:** plan §6; §13 → *Fine-tuning…*; *RAG…*.
**Hours:** Theory **8** + Lab **16** = **24**.

---

## Chapter 22 — State of the Art & Evaluation (text/image/video) · [Volume IV]

**Prerequisites:** Ch 10, Ch 15, Ch 19.

**Learning outcomes — the student can:** survey current medical LLM/multimodal/video SOTA honestly; design evaluation for book-derived models; assess source-fidelity and citation correctness; articulate maturity gaps.

**Topics (theory) — 8 h:**

| # | Topic | h |
|---|-------|---|
| 22.1 | Text medical LLMs today: Med-PaLM 2, Meditron, MedGemma; capabilities | 2 |
| 22.2 | Multimodal (image+text): Med-PaLM M, LLaVA-Med; the reliability gap | 2 |
| 22.3 | Video understanding: surgical/echo/endoscopy — early state | 2 |
| 22.4 | Evaluating book-derived models: source-fidelity & citation correctness | 2 |

**Labs (hands-on) — 6 h:**

| # | Lab | h |
|---|-----|---|
| 22a | Fidelity eval: does the model's answer match the source book? | 3 |
| 22b | Citation-correctness scoring on RAG answers | 3 |

**Datasets/tools:** eval harness; the RAG/fine-tuned models built in Volume IV.
**Assessment:** SOTA briefing + fidelity eval (**60%**); citation-accuracy report (**20%**); quiz (**20%**).
**Key decisions:** honest capability claims; which modality is production-ready; how to report limits.
**References:** plan §6.3; §13 → *Medical LLMs*.
**Hours:** Theory **8** + Lab **6** = **14**.

---

### Volume IV — completion summary

| Ch | Title | T | L | Total |
|----|-------|---|---|-------|
| 18 | Ingestion, OCR & Document Understanding | 8 | 14 | 22 |
| 19 | Figures & Multimodal Understanding | 8 | 14 | 22 |
| 20 | Structuring, Provenance & Building the Corpus | 6 | 12 | 18 |
| 21 | RAG-vs-Fine-tune Paths & Synthetic Data | 8 | 16 | 24 |
| 22 | State of the Art & Evaluation (text/image/video) | 8 | 6 | 14 |
| | **Volume IV total** | **38** | **62** | **100** |

*Matches the plan §2.3 budget.* ✔

---

# Volume V — AI for Medical Robots *(Strategic §7 — elective/frontier)*

Chapters 23–27. Volume budget: **T 44 h + L 60 h = 104 h**.

---

## Chapter 23 — Robotics Fundamentals & Simulation (ROS 2, Isaac Sim) · [Volume V]

**Prerequisites:** Ch 4; general programming maturity.

**Learning outcomes — the student can:** explain robot kinematics/control basics; use ROS 2 concepts (nodes, topics, services, actions); run Gazebo/Isaac Sim; command a simulated arm.

**Topics (theory) — 10 h:**

| # | Topic | h |
|---|-------|---|
| 23.1 | Robotics basics: kinematics, DoF, coordinate frames | 2 |
| 23.2 | Control loops & real-time constraints | 2 |
| 23.3 | ROS 2 architecture: nodes, topics, services, actions | 3 |
| 23.4 | Simulation: Gazebo & NVIDIA Isaac Sim | 2 |
| 23.5 | Medical robotics landscape (surgical, assistive, lab automation) | 1 |

**Labs (hands-on) — 16 h:**

| # | Lab | h |
|---|-----|---|
| 23a | Set up ROS 2 + a simulator; run a demo | 4 |
| 23b | Publish/subscribe: command a simulated arm via topics | 4 |
| 23c | Bring up a simulated robot arm in Isaac Sim; basic motion | 4 |
| 23d | Scripted pick task in simulation | 4 |

**Datasets/tools:** ROS 2, Gazebo, Isaac Sim; GPU workstation.
**Assessment:** simulation task deliverable (**60%**); ROS 2 quiz (**20%**); writeup (**20%**).
**Key decisions:** simulator choice; **sim vs. hardware**; real-time constraints.
**References:** plan §7; §13 → *Robotics & embodied AI*.
**Hours:** Theory **10** + Lab **16** = **26**.

---

## Chapter 24 — Perception for Clinical/Surgical Scenes · [Volume V]

**Prerequisites:** Ch 23; Ch 6–7 (vision-capable models).

**Learning outcomes — the student can:** apply computer vision to surgical/clinical scenes; segment/track instruments & anatomy; estimate depth/pose; integrate perception into a robot loop (in simulation).

**Topics (theory) — 8 h:**

| # | Topic | h |
|---|-------|---|
| 24.1 | CV for surgical scenes: occlusion, lighting, deformation | 2 |
| 24.2 | Segmentation & instrument tracking | 2 |
| 24.3 | Depth & pose estimation | 2 |
| 24.4 | Integrating perception into control (perception→action) | 2 |

**Labs (hands-on) — 14 h:**

| # | Lab | h |
|---|-----|---|
| 24a | Segment instruments/targets in a simulated surgical scene | 4 |
| 24b | Track an instrument across frames | 4 |
| 24c | Depth/pose estimation on sim data | 3 |
| 24d | Close a simple perception→action loop in sim | 3 |

**Datasets/tools:** OpenCV, segmentation models; the simulator.
**Assessment:** perception pipeline (**60%**); tracking report (**20%**); quiz (**20%**).
**Key decisions:** model choice vs. latency; sim-to-real gap; **safety of perception errors**.
**References:** plan §7; §13 → *Robotics & embodied AI*; *Medical LLMs* (vision).
**Hours:** Theory **8** + Lab **14** = **22**.

---

## Chapter 25 — Learning for Control (Imitation/RL, sim-to-real) · [Volume V]

**Prerequisites:** Ch 23, Ch 24.

**Learning outcomes — the student can:** explain imitation learning & RL for control; train a policy in simulation; reason about sim-to-real transfer and its risks; apply safety constraints/shields.

**Topics (theory) — 10 h:**

| # | Topic | h |
|---|-------|---|
| 25.1 | Control paradigms: classical vs. learned | 1 |
| 25.2 | Imitation learning (behavioral cloning) | 2 |
| 25.3 | Reinforcement learning basics for control | 3 |
| 25.4 | Sim-to-real transfer: domain randomization, gaps | 2 |
| 25.5 | Safety constraints & constrained policies | 2 |

**Labs (hands-on) — 14 h:**

| # | Lab | h |
|---|-----|---|
| 25a | Behavioral cloning on a sim manipulation task | 4 |
| 25b | Train an RL policy in sim (reach/grasp) | 5 |
| 25c | Domain-randomization experiment | 3 |
| 25d | Add a safety constraint / shield to the policy | 2 |

**Datasets/tools:** RL libraries (Stable-Baselines3 / Isaac Gym); the simulator.
**Assessment:** trained policy (**60%**); sim-to-real analysis (**20%**); quiz (**20%**).
**Key decisions:** IL vs. RL; reward design; safety shielding; when sim is insufficient.
**References:** plan §7; §13 → *Robotics & embodied AI*.
**Hours:** Theory **10** + Lab **14** = **24**.

---

## Chapter 26 — LLMs/VLA as Planners & Human-in-the-Loop Safety · [Volume V]

**Prerequisites:** Ch 11, Ch 25.

**Learning outcomes — the student can:** use LLMs/VLA models as high-level planners; translate NL tasks into verified action sequences; design human-in-the-loop approval; describe VLA SOTA and its limits in medicine.

**Topics (theory) — 8 h:**

| # | Topic | h |
|---|-------|---|
| 26.1 | LLMs as planners/reasoners for robots | 2 |
| 26.2 | Vision-Language-Action (VLA) models: concepts & SOTA (e.g., RT-2) | 2 |
| 26.3 | Grounding language to actions & verification | 2 |
| 26.4 | Human-in-the-loop: approval gates, oversight, fail-safes | 2 |

**Labs (hands-on) — 12 h:**

| # | Lab | h |
|---|-----|---|
| 26a | LLM task planner: NL instruction → action plan in sim | 4 |
| 26b | Add verification/validation of generated plans | 4 |
| 26c | Human-approval gate before execution; log & audit | 4 |

**Datasets/tools:** local LLM; the simulator; a planning framework.
**Assessment:** LLM-planner-in-sim with approval gate (**60%**); safety analysis (**20%**); quiz (**20%**).
**Key decisions:** autonomy level; verification strategy; **when human approval is mandatory**.
**References:** plan §7; §13 → *Robotics & embodied AI*; *Medical LLMs*.
**Hours:** Theory **8** + Lab **12** = **20**.

---

## Chapter 27 — Regulation, Ethics & Liability · [Volume V]

**Prerequisites:** Ch 15, Ch 26.

**Learning outcomes — the student can:** navigate device regulation for autonomous medical systems; analyze liability/accountability; apply an ethics framework; draft a safety/validation case.

**Topics (theory) — 8 h:**

| # | Topic | h |
|---|-------|---|
| 27.1 | Medical device regulation: SaMD, FDA/CE for AI & robotics | 2 |
| 27.2 | Autonomy levels & regulatory implications | 1 |
| 27.3 | Liability & accountability for autonomous action | 2 |
| 27.4 | Ethics: consent, equity, transparency, human oversight | 2 |
| 27.5 | Building a safety/validation case | 1 |

**Labs (hands-on) — 4 h:**

| # | Lab | h |
|---|-----|---|
| 27a | Draft a regulatory/safety case for a proposed medical-robot feature | 2 |
| 27b | Ethics & liability analysis of an autonomy scenario | 2 |

**Datasets/tools:** regulatory guidance documents; case templates.
**Assessment:** safety/regulatory case (**60%**); ethics analysis (**20%**); quiz (**20%**).
**Key decisions:** autonomy vs. oversight; regulatory pathway; acceptable risk & accountability.
**References:** plan §7; §13 → *Robotics & embodied AI*.
**Hours:** Theory **8** + Lab **4** = **12**.

---

### Volume V — completion summary

| Ch | Title | T | L | Total |
|----|-------|---|---|-------|
| 23 | Robotics Fundamentals & Simulation | 10 | 16 | 26 |
| 24 | Perception for Clinical/Surgical Scenes | 8 | 14 | 22 |
| 25 | Learning for Control (Imitation/RL, sim-to-real) | 10 | 14 | 24 |
| 26 | LLMs/VLA as Planners & HITL Safety | 8 | 12 | 20 |
| 27 | Regulation, Ethics & Liability | 8 | 4 | 12 |
| | **Volume V total** | **44** | **60** | **104** |

*Matches the plan §2.3 budget.* ✔

---

## Program grand total

| Volume | Title | T | L | Total |
|--------|-------|---|---|-------|
| I | Foundations & Clinical Data Engineering | 58 | 66 | 124 |
| II | The LLM Era | 56 | 62 | 118 |
| III | Autonomous Medical AI Systems | 64 | 136 | 200 |
| IV | From Books to LLM | 38 | 62 | 100 |
| | **Core (I–IV)** | **216** | **326** | **542** |
| V | AI for Medical Robots *(elective)* | 44 | 60 | 104 |
| | **With elective (I–V)** | **260** | **386** | **646** |

**All 27 chapters expanded.** Hours match the plan §2.3 budget. Figures remain provisional pending pedagogical review.
