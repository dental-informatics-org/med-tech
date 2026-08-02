# Volume I · Chapter 3 — Healthcare Interoperability (HL7 v2, CDA/C-CDA, FHIR, SMART-on-FHIR) · Theory

> Source: split from `med-tech-curriculum-V1.md` (V1). From this split onward this chapter is maintained **independently** here. See `Volume-I-Chapter-3-context.md` for the AI interaction log.

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

**Datasets/tools:** Synthea synthetic patients; HAPI FHIR (public sandbox or local); Python `hl7apy`, `fhir.resources`/`fhirclient`, `requests`, Pandas; sample C-CDA XML.

**Assessment:** quiz on standards (**20%**); lab rubric on 3a–3e (**50%**); a "clinical data → tidy DataFrame" deliverable from a FHIR bundle (**30%**).

**Key decisions:** FHIR vs. HL7 v2 for a new integration; **document (CDA) vs. resource (FHIR)** models; how much to normalize/terminology-map before feeding an AI pipeline.

**References:** plan §13 → *Interoperability standards*.

**Hours:** Theory **12** + Lab **16** = **28**.
