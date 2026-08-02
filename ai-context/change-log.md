# AI Change Log — Med-Tech Project

> **Purpose.** A single, compact, append-only record of **what each AI iteration changed and why**, committed to the repository. Its job is to let a future AI assistant get up to speed by reading **this one file** instead of replaying the full git history or re-reading every document — saving tokens and preserving intent/context that a raw `git diff` does not capture.

## How to use this file (for AI assistants)
- **Read this file first** at the start of a session, together with the current `docs/med-tech-plan-V1.md`. Do not re-derive project intent from scratch or crawl the whole git history.
- **Append a new entry** at the **top** of the log (reverse-chronological) after making any change to project content.
- Keep each entry **concise**: date, a one-line summary, the *why*, and the files touched. Capture the **reasoning/context**, not the full diff (git already has the diff).
- Use absolute dates (YYYY-MM-DD). Do not rewrite past entries; only add new ones. Correct mistakes with a new entry that references the old one.
- Bump the plan version (`-V2`, `-V3`, …) for major revisions and note it here.

---

## Log (newest first)

### 2026-08-02 — Iteration 14: House style for all docx/pdf (Arial 12 / 1.5 / justified)
- **Summary:** Added `scripts/make-reference-docx.py` → builds `scripts/reference.docx`, a pandoc reference enforcing **Arial 12 pt, 1.5 line spacing, justified body text, left-aligned headings** (via docDefaults + Normal style + theme fonts; headings overridden to left). Wired `--reference-doc` into `export-docs.sh` and `export-chapters.sh`. **Regenerated every docx and pdf** (59 docx / 59 pdf, incl. a new plan docx/pdf). Documented the house style in plan §12.
- **Why:** Owner wants all Word docs in Arial 12, 1.5 spacing, justified, with PDFs redone.
- **Verified:** styles.xml of generated files shows Arial + `w:line="360"` (1.5) + `jc=both` on body, `jc=left` on Heading1–6; PDF spot-checked visually.
- **Files:** `scripts/make-reference-docx.py`, `scripts/reference.docx` (new); `scripts/export-docs.sh`, `scripts/export-chapters.sh`; all `docs/**/*.docx` + `*.pdf`; `docs/med-tech-plan-V1.md` (§12).

### 2026-08-02 — Iteration 13: Chapter 0 — Python & GitHub Fundamentals (new onboarding chapter)
- **Summary:** Added a new **Chapter 0** (Python + Git/GitHub from scratch) as an onboarding prerequisite, under `docs/Volume I/Chapter 0/`. Introduces a **third component, Homework**, on the owner's **Theory : Labs : Homework = 1 : 2 : 4** model — **10 h theory / 20 h labs / 40 h homework = 70 h**. Files: Theory (11 topics), Labs (0a–0j), Homework (HW 0.1–0.7, submitted via the student's GitHub repo + a merged PR), context log, and `.docx`/`.pdf` for all three content files.
- **Why:** Owner asked for a fundamentals chapter using the supplied references (W3Schools Python/Git, Python.org tutorial, GitHub Hello World + learning resources, Class Central) and curated Python GitHub repos.
- **Notes:** Hand-authored (not from the frozen curriculum), so `split-chapters.py` won't touch it. Updated `scripts/export-chapters.sh` to also export `*-Homework.md`. Registered in plan §2.3 as an onboarding row, kept **separate from the core hour totals** (different model). Owner-supplied `lnkd.in` links resolved to canonical repo paths where confident and flagged for verification.
- **Files:** `docs/Volume I/Chapter 0/*` (new); `docs/med-tech-plan-V1.md` (§2.3); `scripts/export-chapters.sh`.

### 2026-08-02 — Iteration 12: Change-log relocated; attribution kept out of git identity
- **Summary:** Moved the change-log to `ai-context/change-log.md` and reworded entries to use generic wording. Updated plan references (header + §12) to the new path. The `.claude/` tool-config folder **is committed** to the repo (owner is fine with the name in files); the only hard requirement is that the AI tool never appear as a GitHub **contributor** or in **commit messages** — handled by using the owner's own git identity (`Igor Alves`) and adding no co-author/"generated with" trailer.
- **Why:** Owner wants no AI-tool attribution in the contributor list or commit messages (folder/file name is acceptable).
- **Files:** `ai-context/change-log.md` (new location), `docs/med-tech-plan-V1.md` (header + §12).

### 2026-08-02 — Iteration 11: Per-chapter Theory/Labs tree + per-chapter context logs
- **Summary:** Split the curriculum into an independent per-chapter tree under `docs/Volume <ROMAN>/Chapter <N>/`. For all 27 chapters: `…-Theory.md`, `…-Labs.md`, `…-context.md`, plus **`.docx` + `.pdf`** for Theory and Labs (54 docx, 54 pdf). Added `scripts/split-chapters.py` (parses master curriculum, splits theory vs labs, seeds context; non-overwriting by default, `FORCE=1` to regenerate) and `scripts/export-chapters.sh` (batch docx/pdf). Documented the per-chapter workflow in plan §12.
- **Why:** Owner wants each volume/chapter to progress **independently** from here, with a per-chapter AI-context memory file; the Theory files will later feed **PowerPoint slides + video explanations** built by another AI run.
- **Key rule:** `docs/med-tech-curriculum-V1.md` is now the **frozen V1 baseline**; the per-chapter files are the working copies. Do NOT re-run `split-chapters.py` without `FORCE=1` once chapters diverge (it would clobber edits). Read/append each chapter's `…-context.md` when modifying it.
- **Files:** `scripts/split-chapters.py`, `scripts/export-chapters.sh` (new); `docs/Volume */Chapter */*` (new, 189 files); `docs/med-tech-plan-V1.md` (§12).

### 2026-08-02 — Iteration 10: DOCX/PDF export + standing export convention
- **Summary:** Exported `docs/med-tech-curriculum-V1.md` to **`.docx` (pandoc)** and **`.pdf` (LibreOffice `soffice`, 39 pp)**. Added reusable `scripts/export-docs.sh` (md→docx→pdf; default targets = plan + curriculum). Documented a **default behavior** in plan §12: on every new version of the plan/curriculum, regenerate matching docx + pdf.
- **Why:** Owner asked to convert the curriculum to docx/pdf and to make docx+pdf generation a default for each new version.
- **Standing convention:** finalize a new version → run `scripts/export-docs.sh` → commit the `.docx`/`.pdf` next to the `.md`.
- **Env note:** host has `pandoc` + LibreOffice `soffice`; **no LaTeX**, so PDF is produced via LibreOffice (docx→pdf), not `pandoc --pdf-engine=xelatex`.
- **Files:** `scripts/export-docs.sh` (new), `docs/med-tech-curriculum-V1.docx` (new), `docs/med-tech-curriculum-V1.pdf` (new), `docs/med-tech-plan-V1.md` (§12).

### 2026-08-02 — Iteration 9: Volumes II–V expanded — all 27 chapters complete
- **Summary:** Expanded **Volume II (Ch 6–11), Volume III (Ch 12–17), Volume IV (Ch 18–22), Volume V (Ch 23–27)** in `docs/med-tech-curriculum-V1.md`, each chapter to the full template (prereqs, outcomes, per-topic theory table, per-lab table, datasets/tools, weighted assessment, key decisions, references, hours). Added per-volume completion tables and a **program grand-total table**.
- **Verification:** every chapter's per-topic hours sum to its §2.3 budget; volume subtotals match (I 124, II 118, III 200, IV 100, V 104). **Core (I–IV) = T216/L326 = 542 h; with elective V = 646 h.**
- **Why:** Owner said "continue without stop or ask" — finish expanding the whole curriculum.
- **Status/next:** First full pass done. Remaining work is **pedagogical review** and optionally trimming plan §2.6 (duplicate Ch3) to a pointer.
- **Files:** `docs/med-tech-curriculum-V1.md`.

### 2026-08-02 — Iteration 8: Volume I fully expanded (Chapters 2–5 + Ch3 migrated)
- **Summary:** Completed **Volume I**. Expanded **Ch 2** (Foundations of Clinical Data, T10/L6), **Ch 4** (Core ML for Medicine, T14/L16), **Ch 5** (Medical NLP Basics, T10/L10); **migrated Ch 3** (Interoperability) from plan §2.6 into the curriculum. Volume I subtotals **T58/L66 = 124 h**, matching plan §2.3.
- **Why:** Owner said "do it" — continue expanding Volume I.
- **Note:** Ch 3 now exists in both plan §2.6 (template example) and the curriculum; keep in sync or later trim §2.6 to a pointer.
- **Files:** `docs/med-tech-curriculum-V1.md`.

### 2026-08-02 — Iteration 7: Curriculum file started; Chapter 1 expanded
- **Summary:** Created `docs/med-tech-curriculum-V1.md` as the home for **fully-expanded formal chapter definitions**. Expanded **Chapter 1 — Python for Data Science** to the §2.6 standard (7 theory topics = 12 h, 6 labs = 18 h).
- **Why:** Owner said "yes" to expanding the next chapter to the worked-example standard.
- **Decision:** expanded chapters live in the companion curriculum file, not inline in the plan.
- **Files:** `docs/med-tech-curriculum-V1.md` (new).

### 2026-08-02 — Iteration 6: Book/university-course academic format
- **Summary:** Recast the plan as a **multi-volume textbook & formal university course**. Rewrote §2 into "Program Structure & Academic Format": Volume/Chapter/Topic/Lab hierarchy, a **Volume & Chapter map (5 volumes / 27 chapters) with a provisional contact-hour budget** (core 542 h, +104 h elective), hour/credit conventions, a **chapter-definition template** (§2.5), and a **worked example — Chapter 3** (§2.6).
- **Why:** Owner wants this to become a real Med-Tech university course/book.
- **Files:** `docs/med-tech-plan-V1.md` (header + §2 rewrite).

### 2026-08-02 — Iteration 5: Change-log mechanism + references
- **Summary:** Added this AI change-log; added a §12 instruction that future iterations must log changes here and read it first; added a **Sources & References** section to the plan.
- **Why:** Owner wants one compact file that carries per-iteration change *context* so future AI runs don't burn tokens reconstructing history from git.
- **Files:** the change-log (new), `docs/med-tech-plan-V1.md` (§12 + new §13 Sources & References).

### 2026-08-02 — Iteration 4: Strategic chapters added
- **Summary:** Added **§6 "From Books to LLM"** and **§7 "AI for Medical Robots"** (frontier elective). Wired both into the overview and milestones; renumbered later sections.
- **Why:** Owner requested these as strategic training chapters.
- **Files:** `docs/med-tech-plan-V1.md`.

### 2026-08-02 — Iteration 3: Interoperability standards
- **Summary:** Added **HL7 v2.x, HL7 CDA/C-CDA, and FHIR** (plus LOINC) across the plan: new Phase-0 topic, new **Lab 2b**, cross-cutting bullet, software-spec row, and FHIR integration in Phase-2 deployment.
- **Why:** Owner asked to include HL7/CDA/FHIR development.
- **Files:** `docs/med-tech-plan-V1.md`.

### 2026-08-02 — Iteration 2: Attribution policy
- **Summary:** Verified the repo contains **no AI-tool attribution** (working files, commit messages, author metadata all clean).
- **Why & standing decision:** Owner does not want the GitHub repo to reveal it was generated by an AI assistant. **Policy:** do **not** add any AI-tool "Co-Authored-By" or "Generated with" trailer to commits or files in this repo, and keep AI-tool names out of the tracked tree.
- **Files:** none changed (verification + standing policy).

### 2026-08-02 — Iteration 1: Initial plan created
- **Summary:** Created `docs/med-tech-plan-V1.md` — the reference plan turning healthcare students (with basic Python) into autonomous medical-AI developers. Captured vision/thesis, 3-phase structure, topics, labs, software/hardware specs, milestones.
- **Why:** Owner wanted a persistent plan the AI retrieves and iterates on. Curriculum is the planned next artifact.
- **Files:** `docs/med-tech-plan-V1.md` (new).
