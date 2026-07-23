# Behavioral Health Analytics: Unsupervised Clustering & Patient Archetyping

**Author:** Camila Chivelli  
**Role:** Data Analyst / Machine Learning Engineer  
**Project Repository:** Health Behavioral Data Pipeline

[![Python](https://img.shields.io/badge/Python-3.9+-0A2947?style=flat-square&logo=python&logoColor=F3E4C9)](#)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-K--Means-0A2947?style=flat-square&logo=scikit-learn&logoColor=F3E4C9)](#)
[![Pandas](https://img.shields.io/badge/Pandas-Data_Preparation-0A2947?style=flat-square&logo=pandas&logoColor=F3E4C9)](#)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Plotting-0A2947?style=flat-square&logo=python&logoColor=F3E4C9)](#)
[![Seaborn](https://img.shields.io/badge/Seaborn-Data_Visualization-0A2947?style=flat-square&logo=python&logoColor=F3E4C9)](#)


A comprehensive data mining and machine learning pipeline applied to the **"Estimation of Obesity Levels Based on Eating Habits and Physical Condition"** dataset. This project processes sociodemographic, eating, and physical metrics to investigate obesity risk factors and segment population profiles using unsupervised learning.

---

## 📌 Executive Summary

Obesity is a complex, multifactorial health issue driven by genetic predispositions, nutritional habits, and sedentary behaviors. This project establishes an end-to-end analytical workflow—from raw data curation to hypothesis-driven Exploratory Data Analysis (EDA) and K-Means Clustering—to identify distinct risk profiles and evaluate the interplay between behavioral and inherited factors.

* **Dataset Source:** [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/544/estimation+of+obesity+levels+based+on+eating+habits+and+physical+condition) (Palechor & Manotas, 2019)
* **Sample Size:** 2,111 instances, 17 multidimensional attributes
* **Dataset Composition:** 23% real surveys (485 records) and 77% synthetic data generated via SMOTE (1,626 records)

---

## 🏗️ Repository Architecture
```text
behavioral-health-analytics/
├── docs/                             # Executive documentation & clinical insights
│   ├── executive_summary.md          # Business & clinical analysis of the 4 archetypes
│   ├── data_dictionary.md           # Variable definitions, scales, and constraints
│   └── dataset_provenance.md         # Survey specification & hybrid sampling methodology
├── notebooks/                        # Research, EDA & statistical validation
│   ├── 01_exploratory_data_analysis.ipynb
│   ├── 02_data_cleaning_and_preprocessing.ipynb
│   └── ...
├── scripts/                          # Production-ready Python modules
│   ├── data_cleaning.py
│   ├── data_processing.py
│   └── ...
├── models/                           # Serialized trained models & scalers
├── visuals/                          # Exported plots, cluster charts & pipeline diagrams
├── data/                             # Raw and processed datasets
├── main.py                           # Single-command pipeline entry point
├── requirements.txt                  # Environment dependencies
└── README.md                         # Project documentation
```
---

## 🎯 Objectives

The primary goal of this project is to build an end-to-end, reproducible data mining and machine learning architecture to analyze obesity risk factors through behavioral profiling.

Specifically, the project aims to:
* **Isolate Behavioral Signals:** Evaluate dietary habits, physical activity, and technology-driven sedentarism while isolating direct biometric variables to prevent target leakage.
* **Validate Analytical Hypotheses:** Perform statistical testing to quantify the impact of genetic predisposition, high-caloric intake, and physical exercise across different age groups.
* **Uncover Unsupervised Patient Archetypes:** Apply K-Means clustering to discover non-obvious population segments, enabling personalized lifestyle recommendations over generic clinical treatments.
* **Deliver Production-Ready Code:** Transition exploratory analysis into a modular, command-line operable Python pipeline (`main.py`).

---

## 🛠️ Project Scope & Tools

### Scope
* **In-Scope:** Data ingestion, domain constraint enforcement (clamping), scaling, categorical encodings, exploratory data analysis, hypothesis testing, K-Means model evaluation, and cluster profiling.
* **Out-of-Scope:** Supervised classification for direct obesity diagnosis or live REST API deployment (focus remains on behavioral clustering and data pipeline architecture).

### Tech Stack & Tools
* **Core Language:** Python 3.9+
* **Data Manipulation & Analysis:** `pandas`, `numpy`
* **Machine Learning & Preprocessing:** `scikit-learn` (`KMeans`, `StandardScaler`, `OneHotEncoder`)
* **Visualization & Reporting:** `matplotlib`, `seaborn`
* **Environment & Tools:** Jupyter Notebooks, Git, Markdown

---

## 🔄 Data Workflow

The execution sequence follows a strict, modular pipeline design to guarantee reproducibility:

[Raw Data] ➔ [Data Cleaning & Clipping] ➔ [Feature Isolation & Encoding] ➔ [Scaling] ➔ [K-Means (K=4)] ➔ [Cluster Export & Insights]

1. **Ingestion & Validation:** Ingests raw data from Palechor & Manotas (2019) and validates synthetic SMOTE structure.
2. **Domain Boundary Enforcement:** Applies .clip() on continuous survey features (FCVC, NCP, CH2O, FAF, TUE) to retain interpolation resolution while enforcing survey limits.
3. **Leakage Prevention & Encoding:** Isolates biometric target variables (Height, Weight, NObeyesdad). Applies binary mapping, ordinal encodings, and One-Hot Encoding (MTRANS).
4. **Feature Scaling:** Normalizes continuous predictors using StandardScaler to ensure balanced distance calculation in K-Means.

---

## 🔬 Methods Used

* **Data Curation & Preprocessing:** Domain clamping, duplicate validation, target variable isolation, and categorical mapping.
* **Exploratory Data Analysis (EDA):** Multivariate distribution analysis, correlation matrix inspection, and conditional demographic breakdowns.
* **Hypothesis Testing:** Non-parametric evaluation of behavioral drivers (dietary intake, genetic markers) across age brackets.
* **Unsupervised Clustering:** K-Means algorithm optimized via Euclidean distance.
* **Cluster Validation Metrics:** Inertia / Elbow Method and Silhouette Coefficient evaluation for optimal K selection (K=4).

---

## 💡 Key Insights

* **Genetics as a Baseline Shift:** Family history of overweight acts as a constant upward baseline shift in BMI across all age groups, compounding behavioral risk factors.
* **Screen Time & Physical Activity Gap:** Higher technology usage (TUE) strongly correlates with younger demographics, serving as a key driver for low weekly physical activity (FAF).
* **Caloric Volume Drives Extreme Outcomes:** High vegetable intake alone does not protect against severe obesity if paired with elevated meal frequency and total food volume (as observed in Cluster 3, which contains 100% of Obesity Type III cases).
* **Meal Skipping Dynamics:** Severe meal irregularity (NCP reduction) leads to unstable dietary patterns rather than significant weight loss, often yielding normal-to-mild overweight distributions rather than healthy baselines.

---

## 🚀 How to Use / Getting Started

Follow these steps to set up the environment, run the automated pipeline, or explore the research notebooks.

### 1. Prerequisites & Installation

Ensure you have Python 3.9+ installed on your system.

1. Clone the repository:
   ```text
   git clone https://github.com/your-username/behavioral-health-analytics.git
   cd behavioral-health-analytics
   ```
3. Create and activate a virtual environment:
   * Linux / macOS:
   ```text
   python3 -m venv venv
   source venv/bin/activate
   ```
   * Windows:
   ```text
   python -m venv venv
   .\venv\Scripts\activate
   ```

4. Install dependencies:
   ```text
   pip install -r requirements.txt
   ```
   
---

### 2. Running the Production Pipeline (main.py)

The entire workflow—including data loading, domain-constraint validation, scaling, feature engineering, and model execution—is fully automated via the main pipeline entry point.

Execute the following command from the project root:
 ```text
python main.py
```

What happens during execution?
1. Data Ingestion & Cleaning: Loads raw data and applies range clipping (.clip()) to maintain domain boundaries on synthetic records.
2. Feature Engineering: Isolates biometric leakage variables (BMI, Weight, Height) and applies proper binary, ordinal, and One-Hot encodings.
3. Scaling & Normalization: Applies StandardScaler to continuous behavioral features.
4. Clustering & Output Generation: Runs the optimized K-Means model (K=4), assigns cluster labels to observations, and exports processed datasets/metrics.

---

### 3. Interactive Research & Exploration

To inspect the exploratory data analysis (EDA) or review the mathematical validation behind K=4 (Elbow & Silhouette metrics):

1. Launch Jupyter Lab:
   jupyter lab

3. Open any notebook inside the /notebooks directory

---

## 📂 Project Documentation Quick Links

For detailed domain information and clinical insights, refer to the /docs directory:
* Executive Summary (docs/executive_summary.md) – Clinical archetypes and business value.
* Data Dictionary (docs/data_dictionary.md) – Complete variable definitions and constraints.
* Dataset Source (docs/dataset_source.md) – Methodology and survey background (Palechor & Manotas, 2019).
