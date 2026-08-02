# Volume V · Chapter 26 — LLMs/VLA as Planners & Human-in-the-Loop Safety · Labs

> Source: split from `med-tech-curriculum-V1.md` (V1). From this split onward this chapter is maintained **independently** here. See `Volume-V-Chapter-26-context.md` for the AI interaction log.

**Prerequisites:** Ch 11, Ch 25.

**Learning outcomes — the student can:** use LLMs/VLA models as high-level planners; translate NL tasks into verified action sequences; design human-in-the-loop approval; describe VLA SOTA and its limits in medicine.

**Labs (hands-on) — 12 h:**

| # | Lab | h |
|---|-----|---|
| 26a | LLM task planner: NL instruction → action plan in sim | 4 |
| 26b | Add verification/validation of generated plans | 4 |
| 26c | Human-approval gate before execution; log & audit | 4 |

**Datasets/tools:** local LLM; the simulator; a planning framework.
**Assessment:** LLM-planner-in-sim with approval gate (**60%**); safety analysis (**20%**); quiz (**20%**).
**Key decisions:** autonomy level; verification strategy; **when human approval is mandatory**.
**References:** plan §7; §13 → *Robotics & embodied AI*; *Medical LLMs*.
**Hours:** Theory **8** + Lab **12** = **20**.
