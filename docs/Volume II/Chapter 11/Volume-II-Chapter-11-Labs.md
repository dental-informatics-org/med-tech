# Volume II · Chapter 11 — First Fine-Tunes (PubMedBERT, QLoRA, local MedGemma/Ollama) · Labs

> Source: split from `med-tech-curriculum-V1.md` (V1). From this split onward this chapter is maintained **independently** here. See `Volume-II-Chapter-11-context.md` for the AI interaction log.

**Prerequisites:** Ch 7–10.

**Learning outcomes — the student can:** fine-tune a biomedical BERT for classification; apply QLoRA to fine-tune a small generative LLM on medical QA; run models locally via Ollama; evaluate a fine-tune and write a model card.

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
