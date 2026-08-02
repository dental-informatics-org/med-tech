# Volume I · Chapter 4 — Core Machine Learning for Medicine · Labs

> Source: split from `med-tech-curriculum-V1.md` (V1). From this split onward this chapter is maintained **independently** here. See `Volume-I-Chapter-4-context.md` for the AI interaction log.

**Prerequisites:** Ch 1 (NumPy/Pandas), Ch 2 (clinical data).

**Learning outcomes — the student can:**
- Frame a clinical problem as **supervised or unsupervised** ML and build/train/evaluate models with **scikit-learn**.
- Apply a rigorous **workflow** (train/val/test, cross-validation) and avoid **data leakage**.
- Choose and **interpret clinically appropriate metrics** (sensitivity/specificity, PPV/NPV, ROC-AUC, PR-AUC, calibration).
- Use **unsupervised** methods (clustering, PCA) for **patient stratification**, and recognize imbalance/bias issues.

**Labs (hands-on) — 16 h:**

| # | Lab | h |
|---|-----|---|
| 4a | Build a readmission classifier (logistic regression) with a proper train/test split | 3 |
| 4b | Random forest / gradient boosting on the same task; compare; feature importance | 3 |
| 4c | Evaluation deep-dive: ROC/PR curves, calibration, clinical threshold selection | 3 |
| 4d | Cross-validation & hyperparameter tuning; leakage checks | 3 |
| 4e | Unsupervised patient stratification: clustering + PCA visualization | 4 |

**Datasets/tools:** synthetic structured EHR; scikit-learn, Pandas, Matplotlib.

**Assessment:** modeling project — build + evaluate a classifier with written interpretation (**50%**); evaluation/metrics lab rubric (**30%**); quiz (**20%**).

**Key decisions:** metric choice for the clinical question; **sensitivity vs. specificity** trade-off; complexity vs. **interpretability**; handling imbalance; avoiding leakage.

**References:** plan §13 → *Programming & data science*; *Clinical datasets*.

**Hours:** Theory **14** + Lab **16** = **30**. *(Feeds plan Lab 2 — Simple Clinical Classifier.)*
