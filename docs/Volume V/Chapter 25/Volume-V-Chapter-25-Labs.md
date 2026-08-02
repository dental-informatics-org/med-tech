# Volume V · Chapter 25 — Learning for Control (Imitation/RL, sim-to-real) · Labs

> Source: split from `med-tech-curriculum-V1.md` (V1). From this split onward this chapter is maintained **independently** here. See `Volume-V-Chapter-25-context.md` for the AI interaction log.

**Prerequisites:** Ch 23, Ch 24.

**Learning outcomes — the student can:** explain imitation learning & RL for control; train a policy in simulation; reason about sim-to-real transfer and its risks; apply safety constraints/shields.

**Labs (hands-on) — 14 h:**

| # | Lab | h |
|---|-----|---|
| 25a | Behavioral cloning on a sim manipulation task | 4 |
| 25b | Train an RL policy in sim (reach/grasp) | 5 |
| 25c | Domain-randomization experiment | 3 |
| 25d | Add a safety constraint / shield to the policy | 2 |

**Datasets/tools:** RL libraries (Stable-Baselines3 / Isaac Gym); the simulator.
**Assessment:** trained policy (**60%**); sim-to-real analysis (**20%**); quiz (**20%**).
**Key decisions:** IL vs. RL; reward design; safety shielding; when sim is insufficient.
**References:** plan §7; §13 → *Robotics & embodied AI*.
**Hours:** Theory **10** + Lab **14** = **24**.
