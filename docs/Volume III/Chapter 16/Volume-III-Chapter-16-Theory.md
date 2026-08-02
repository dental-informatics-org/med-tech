# Volume III · Chapter 16 — Deployment, FHIR Integration & Compliance · Theory

> Source: split from `med-tech-curriculum-V1.md` (V1). From this split onward this chapter is maintained **independently** here. See `Volume-III-Chapter-16-context.md` for the AI interaction log.

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

**Datasets/tools:** Ollama, Open WebUI, FastAPI, HAPI FHIR/Synthea; monitoring tools.
**Assessment:** deployed FHIR-integrated service (**60%**); monitoring setup (**20%**); quiz (**20%**).
**Key decisions:** local vs. cloud; API design; regulatory pathway; PHI handling at inference.
**References:** plan §13 → *…local inference*; *Interoperability standards*; *Clinical data, code sets & privacy*.
**Hours:** Theory **10** + Lab **16** = **26**.
