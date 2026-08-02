# Volume II · Chapter 11 — First Fine-Tunes (PubMedBERT, QLoRA, local MedGemma/Ollama) · Theory

> Source: split from `med-tech-curriculum-V1.md` (V1). From this split onward this chapter is maintained **independently** here. See `Volume-II-Chapter-11-context.md` for the AI interaction log.

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

**Datasets/tools:** HF `transformers`/`peft`/`bitsandbytes`, QLoRA, Ollama, MedGemma; GPU workstation.
**Assessment:** fine-tuned model + model card (**60%**); eval report (**20%**); quiz (**20%**).
**Key decisions:** full vs. PEFT fine-tuning; quantization level vs. quality; base model/size vs. hardware.
**References:** plan §13 → *Fine-tuning…*; *Medical LLMs*; *…local inference*.
**Hours:** Theory **10** + Lab **20** = **30**.
