# Volume II · Chapter 6 — Transformer Architecture & Self-Attention · Theory

> Source: split from `med-tech-curriculum-V1.md` (V1). From this split onward this chapter is maintained **independently** here. See `Volume-II-Chapter-6-context.md` for the AI interaction log.

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

**Datasets/tools:** Hugging Face `transformers`; a small BERT/GPT; clinical text samples.
**Assessment:** architecture quiz (**50%**); attention-visualization writeup (**30%**); tokenization exercise (**20%**).
**Key decisions:** encoder vs. decoder for a task; context length vs. cost; tokenizer choice.
**References:** plan §13 → *Transformers & the Hugging Face ecosystem*.
**Hours:** Theory **12** + Lab **6** = **18**.
