# Volume V · Chapter 24 — Perception for Clinical/Surgical Scenes · Labs

> Source: split from `med-tech-curriculum-V1.md` (V1). From this split onward this chapter is maintained **independently** here. See `Volume-V-Chapter-24-context.md` for the AI interaction log.

**Prerequisites:** Ch 23; Ch 6–7 (vision-capable models).

**Learning outcomes — the student can:** apply computer vision to surgical/clinical scenes; segment/track instruments & anatomy; estimate depth/pose; integrate perception into a robot loop (in simulation).

**Labs (hands-on) — 14 h:**

| # | Lab | h |
|---|-----|---|
| 24a | Segment instruments/targets in a simulated surgical scene | 4 |
| 24b | Track an instrument across frames | 4 |
| 24c | Depth/pose estimation on sim data | 3 |
| 24d | Close a simple perception→action loop in sim | 3 |

**Datasets/tools:** OpenCV, segmentation models; the simulator.
**Assessment:** perception pipeline (**60%**); tracking report (**20%**); quiz (**20%**).
**Key decisions:** model choice vs. latency; sim-to-real gap; **safety of perception errors**.
**References:** plan §7; §13 → *Robotics & embodied AI*; *Medical LLMs* (vision).
**Hours:** Theory **8** + Lab **14** = **22**.
