# Volume III · Chapter 16 — Deployment, FHIR Integration & Compliance · Labs

> Source: split from `med-tech-curriculum-V1.md` (V1). From this split onward this chapter is maintained **independently** here. See `Volume-III-Chapter-16-context.md` for the AI interaction log.

**Prerequisites:** Ch 12, Ch 15, Ch 3.

**Learning outcomes — the student can:** deploy models locally (Ollama/Open WebUI); build an inference API; integrate via FHIR (read/write, SMART-on-FHIR); monitor performance/drift; navigate the regulatory/compliance landscape.

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
