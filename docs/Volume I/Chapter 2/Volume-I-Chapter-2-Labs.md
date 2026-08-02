# Volume I · Chapter 2 — Foundations of Clinical Data (EHR; code sets; privacy) · Labs

> Source: split from `med-tech-curriculum-V1.md` (V1). From this split onward this chapter is maintained **independently** here. See `Volume-I-Chapter-2-context.md` for the AI interaction log.

**Prerequisites:** Ch 1 (Python/Pandas).

**Learning outcomes — the student can:**
- Describe **EHR structure** and its core data domains, and distinguish structured vs. unstructured data.
- Navigate and **map medical code sets** — ICD-10-CM/PCS, CPT/HCPCS, SNOMED CT, LOINC — to the right purpose.
- Explain **data privacy/regulation** (HIPAA, GDPR) and what makes clinical data identifiable.
- Apply basic **de-identification** and justify **synthetic-data** use for development.

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
