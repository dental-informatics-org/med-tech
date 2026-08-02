# Volume I · Chapter 2 — Foundations of Clinical Data (EHR; code sets; privacy) · Theory

> Source: split from `med-tech-curriculum-V1.md` (V1). From this split onward this chapter is maintained **independently** here. See `Volume-I-Chapter-2-context.md` for the AI interaction log.

**Prerequisites:** Ch 1 (Python/Pandas).

**Learning outcomes — the student can:**
- Describe **EHR structure** and its core data domains, and distinguish structured vs. unstructured data.
- Navigate and **map medical code sets** — ICD-10-CM/PCS, CPT/HCPCS, SNOMED CT, LOINC — to the right purpose.
- Explain **data privacy/regulation** (HIPAA, GDPR) and what makes clinical data identifiable.
- Apply basic **de-identification** and justify **synthetic-data** use for development.

**Topics (theory) — 10 h:**

| # | Topic | h |
|---|-------|---|
| 2.1 | The EHR: data domains (demographics, encounters, dx, procedures, meds, labs, vitals, notes); structured vs. unstructured | 2 |
| 2.2 | Diagnosis & procedure code sets: ICD-10-CM/PCS, CPT/HCPCS | 2 |
| 2.3 | Clinical terminologies: SNOMED CT (concepts/hierarchies), LOINC (labs) | 2 |
| 2.4 | Mapping, crosswalks & value sets between terminologies | 1 |
| 2.5 | Privacy & regulation: HIPAA (PHI, Safe Harbor / Expert Determination), GDPR (special-category data, lawful basis) | 2 |
| 2.6 | De-identification, synthetic data & data-governance basics | 1 |

**Datasets/tools:** synthetic EHR; public browsers (ICD-10, SNOMED CT browser, LOINC search); Pandas.

**Assessment:** quiz on code sets & privacy (**40%**); crosswalk deliverable (**30%**); de-identification lab rubric (**30%**).

**Key decisions:** which terminology fits which purpose; when data is/ isn't de-identified; **synthetic vs. real** data for development.

**References:** plan §13 → *Clinical data, code sets & privacy*.

**Hours:** Theory **10** + Lab **6** = **16**.
