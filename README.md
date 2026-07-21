# End-to-End Data Pipeline: Lifestyle & Obesity Risk Analysis

[![Python](https://img.shields.io/badge/Python-3.10+-0A2947?style=flat-square&logo=python&logoColor=F3E4C9)](#)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-K--Means-0A2947?style=flat-square&logo=scikit-learn&logoColor=F3E4C9)](#)
[![Pandas](https://img.shields.io/badge/Pandas-Data_Preparation-0A2947?style=flat-square&logo=pandas&logoColor=F3E4C9)](#)
[![Seaborn](https://img.shields.io/badge/Seaborn-Data_Visualization-0A2947?style=flat-square&logo=python&logoColor=F3E4C9)](#)

A comprehensive data mining and machine learning pipeline applied to the **"Estimation of Obesity Levels Based on Eating Habits and Physical Condition"** dataset. This project processes sociodemographic, eating, and physical metrics to investigate obesity risk factors and segment population profiles using unsupervised learning.

---

## 📌 Executive Summary

Obesity is a complex, multifactorial health issue driven by genetic predispositions, nutritional habits, and sedentary behaviors. This project establishes an end-to-end analytical workflow—from raw data curation to hypothesis-driven Exploratory Data Analysis (EDA) and K-Means Clustering—to identify distinct risk profiles and evaluate the interplay between behavioral and inherited factors.

* **Dataset Source:** [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/544/estimation+of+obesity+levels+based+on+eating+habits+and+physical+condition) (Palechor & Manotas, 2019)
* **Sample Size:** 2,111 instances, 17 multidimensional attributes
* **Dataset Composition:** 23% real surveys (485 records) and 77% synthetic data generated via SMOTE (1,626 records)

---

## ⚙️ Data Cleaning & Pipeline Engineering

To ensure statistical integrity before modeling, specific data curation protocols were applied to address synthetic generation artifacts ("SMOTE fingerprint"):

1. **Precision Restoration & Type Casting:**
   * Synthetic sampling created floating-point numbers with up to six decimal places for inherently discrete variables (`Age`, `FCVC`, `NCP`, `CH2O`, `FAF`, `TUE`). These were rounded to the nearest integer and converted to `int64`.
   * Biometric attributes were standardized to realistic continuous precision (`Height` to 2 decimals, `Weight` to 1 decimal).

2. **Domain Clamping (Boundary Enforcement):**
   * Applied clamping on `NCP` (Number of Main Meals) to re-align values exceeding the original survey bounds (`NCP > 3` re-assigned to `3`).

3. **Feature Encoding & Normalization:**
   * Binary attributes (`FAVC`, `SMOKE`, `family_history_with_overweight`) converted via Label Encoding (0/1).
   * Ordinal variables (`CAEC`, `CALC`) mapped to intensity scales.
   * `StandardScaler` (Z-Score) applied across all continuous/discrete features to prevent feature scale dominance during distance-based calculations in clustering.

---

## 🔍 Exploratory Data Analysis & Hypothesis Testing

### 📊 Exploratory Insights
* **Demographics:** Highly skewed young population ($\mu = 24.32$ years, $M = 23.00$ years) with symmetric height distribution across genders ($\mu_{\text{women}} = 1.64\text{m}$, $\mu_{\text{men}} = 1.76\text{m}$).
* **Weight Variance:** Female weight showed higher dispersion ($SD = 29.72\text{kg}$) and positive skewness compared to males ($SD = 21.41\text{kg}$), indicating a higher polarization toward extreme obesity classes in females.

### 🧪 Hypothesis Validation

* **Hypothesis 1 (Genetic Predisposition):**
  * *Verdict:* **Validated.** Family history operates as a vertical shift factor on BMI. Individuals with positive family history start at higher metabolic risk levels across all age groups compared to those without inherited predisposition.
* **Hypothesis 2 (High-Caloric Diet / FAVC):**
  * *Verdict:* **Validated.** Frequent consumption of high-caloric food is the primary driver displacing BMI distributions into overweight/obese ranges. The effect intensifies significantly in the 26–40 age bracket.
* **Hypothesis 3 (Physical Activity / FAF as a Moderator):**
  * *Verdict:* **Partially Validated.** Higher weekly physical activity moderates age-related BMI growth, but exercise alone does not fully offset strong genetic or dietary risk factors.

---

## 🤖 Unsupervised Learning: K-Means Clustering

To uncover underlying risk segments without relying on target labels (`NObeyesdad`), K-Means clustering was executed on behavioral, demographic, and genetic features (excluding direct `Height` and `Weight` measurements to avoid target leakage).

### Optimal Cluster Selection
Evaluated using the **Silhouette Score** across $K \in [2, 10]$, determining **$K = 4$** as the optimal balance between mathematical cohesion/separation and clinical interpretability.

```text
Silhouette Index Evaluation:
  K=2 : 0.172
  K=3 : 0.139
  K=4 : 0.104  <-- Optimal for multidimensional profile segmentation
  K=5 : 0.121
