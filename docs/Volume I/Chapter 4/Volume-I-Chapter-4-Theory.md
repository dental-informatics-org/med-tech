# Volume I · Chapter 4 — Core Machine Learning for Medicine · Theory

> Source: split from `med-tech-curriculum-V1.md` (V1). From this split onward this chapter is maintained **independently** here. See `Volume-I-Chapter-4-context.md` for the AI interaction log.

**Prerequisites:** Ch 1 (NumPy/Pandas), Ch 2 (clinical data).

**Learning outcomes — the student can:**
- Frame a clinical problem as **supervised or unsupervised** ML and build/train/evaluate models with **scikit-learn**.
- Apply a rigorous **workflow** (train/val/test, cross-validation) and avoid **data leakage**.
- Choose and **interpret clinically appropriate metrics** (sensitivity/specificity, PPV/NPV, ROC-AUC, PR-AUC, calibration).
- Use **unsupervised** methods (clustering, PCA) for **patient stratification**, and recognize imbalance/bias issues.

**Topics (theory) — 14 h:**

| # | Topic | h |
|---|-------|---|
| 4.1 | ML framing for medicine: supervised vs. unsupervised; clinical use cases | 1 |
| 4.2 | The ML workflow: train/validation/test, cross-validation, data leakage | 2 |
| 4.3 | Supervised I: logistic regression, linear models, regularization | 2 |
| 4.4 | Supervised II: decision trees, random forests, gradient boosting | 2 |
| 4.5 | Evaluation & metrics: confusion matrix, sensitivity/specificity/PPV/NPV, ROC-AUC, PR-AUC, calibration | 3 |
| 4.6 | Class imbalance, thresholds & clinical decision trade-offs | 1 |
| 4.7 | Unsupervised: clustering (k-means, hierarchical) + PCA for stratification | 2 |
| 4.8 | Overfitting, bias/variance & model selection | 1 |

**Datasets/tools:** synthetic structured EHR; scikit-learn, Pandas, Matplotlib.

**Assessment:** modeling project — build + evaluate a classifier with written interpretation (**50%**); evaluation/metrics lab rubric (**30%**); quiz (**20%**).

**Key decisions:** metric choice for the clinical question; **sensitivity vs. specificity** trade-off; complexity vs. **interpretability**; handling imbalance; avoiding leakage.

**References:** plan §13 → *Programming & data science*; *Clinical datasets*.

**Hours:** Theory **14** + Lab **16** = **30**. *(Feeds plan Lab 2 — Simple Clinical Classifier.)*
