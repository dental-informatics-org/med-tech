# Volume V · Chapter 24 — Perception for Clinical/Surgical Scenes · Theory

> Source: split from `med-tech-curriculum-V1.md` (V1). From this split onward this chapter is maintained **independently** here. See `Volume-V-Chapter-24-context.md` for the AI interaction log.

**Prerequisites:** Ch 23; Ch 6–7 (vision-capable models).

**Learning outcomes — the student can:** apply computer vision to surgical/clinical scenes; segment/track instruments & anatomy; estimate depth/pose; integrate perception into a robot loop (in simulation).

**Topics (theory) — 8 h:**

| # | Topic | h |
|---|-------|---|
| 24.1 | CV for surgical scenes: occlusion, lighting, deformation | 2 |
| 24.2 | Segmentation & instrument tracking | 2 |
| 24.3 | Depth & pose estimation | 2 |
| 24.4 | Integrating perception into control (perception→action) | 2 |

**Datasets/tools:** OpenCV, segmentation models; the simulator.
**Assessment:** perception pipeline (**60%**); tracking report (**20%**); quiz (**20%**).
**Key decisions:** model choice vs. latency; sim-to-real gap; **safety of perception errors**.
**References:** plan §7; §13 → *Robotics & embodied AI*; *Medical LLMs* (vision).
**Hours:** Theory **8** + Lab **14** = **22**.
