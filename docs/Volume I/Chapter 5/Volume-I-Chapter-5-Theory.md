# Volume I · Chapter 5 — Medical NLP Basics (regex → embeddings) · Theory

> Source: split from `med-tech-curriculum-V1.md` (V1). From this split onward this chapter is maintained **independently** here. See `Volume-I-Chapter-5-context.md` for the AI interaction log.

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

**Datasets/tools:** synthetic/de-identified clinical notes; Python `re`, scikit-learn, spaCy/NLTK, gensim or pretrained biomedical embeddings.

**Assessment:** regex extractor deliverable — rubric (**40%**); text-classification lab (**40%**); quiz (**20%**).

**Key decisions:** rule-based vs. statistical NLP; when regex suffices vs. needs ML; **general vs. biomedical** embeddings; handling **negation/context**.

**References:** plan §13 → *Transformers & the Hugging Face ecosystem* (bridge); *Programming & data science*.

**Hours:** Theory **10** + Lab **10** = **20**.
