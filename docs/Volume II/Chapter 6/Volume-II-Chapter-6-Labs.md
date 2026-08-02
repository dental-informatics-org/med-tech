# Volume II · Chapter 6 — Transformer Architecture & Self-Attention · Labs

> Source: split from `med-tech-curriculum-V1.md` (V1). From this split onward this chapter is maintained **independently** here. See `Volume-II-Chapter-6-context.md` for the AI interaction log.

**Prerequisites:** Ch 4 (ML), Ch 5 (NLP basics).

**Learning outcomes — the student can:** explain self-attention and the transformer block; describe tokenization, embeddings and positional encoding; distinguish encoder/decoder/encoder-decoder families; read a model card and reason about parameters/context length.

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
