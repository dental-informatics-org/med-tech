# Volume V · Chapter 25 — Learning for Control (Imitation/RL, sim-to-real) · Theory

> Source: split from `med-tech-curriculum-V1.md` (V1). From this split onward this chapter is maintained **independently** here. See `Volume-V-Chapter-25-context.md` for the AI interaction log.

**Prerequisites:** Ch 23, Ch 24.

**Learning outcomes — the student can:** explain imitation learning & RL for control; train a policy in simulation; reason about sim-to-real transfer and its risks; apply safety constraints/shields.

**Topics (theory) — 10 h:**

| # | Topic | h |
|---|-------|---|
| 25.1 | Control paradigms: classical vs. learned | 1 |
| 25.2 | Imitation learning (behavioral cloning) | 2 |
| 25.3 | Reinforcement learning basics for control | 3 |
| 25.4 | Sim-to-real transfer: domain randomization, gaps | 2 |
| 25.5 | Safety constraints & constrained policies | 2 |

**Datasets/tools:** RL libraries (Stable-Baselines3 / Isaac Gym); the simulator.
**Assessment:** trained policy (**60%**); sim-to-real analysis (**20%**); quiz (**20%**).
**Key decisions:** IL vs. RL; reward design; safety shielding; when sim is insufficient.
**References:** plan §7; §13 → *Robotics & embodied AI*.
**Hours:** Theory **10** + Lab **14** = **24**.
