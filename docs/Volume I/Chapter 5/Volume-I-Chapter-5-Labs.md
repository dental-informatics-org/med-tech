# Volume I · Chapter 5 — Medical NLP Basics (regex → embeddings) · Labs

> Source: split from `med-tech-curriculum-V1.md` (V1). From this split onward this chapter is maintained **independently** here. See `Volume-I-Chapter-5-context.md` for the AI interaction log.

**Prerequisites:** Ch 1 (Python/Pandas).

**Learning outcomes — the student can:**
- Process clinical free text with **classical NLP** (tokenization, normalization, TF-IDF).
- Build **regex/rule-based extractors** for clinical concepts and detect **negation**.
- Use **word embeddings** (general and biomedical) and build a simple clinical **text classifier**.
- Articulate the **limits of classical NLP** (context, negation) that motivate transformers (bridge to Volume II).

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
