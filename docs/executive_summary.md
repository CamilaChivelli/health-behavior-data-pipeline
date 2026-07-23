# Executive Summary: Behavioral Health Analytics & Unsupervised Clustering

**Domain:** Health Data Analytics / Machine Learning Engineering  

---

## 🎯 Executive Overview

Obesity management typically relies on isolated biometric indicators like Body Mass Index (BMI). However, BMI alone fails to capture the underlying lifestyle and behavioral drivers that dictate patient outcomes.

This project implements an **unsupervised $K$-Means clustering architecture** ($K=4$) to segment individuals based strictly on **behavioral, dietary, and physical activity patterns** (isolating biometric metrics to avoid data leakage). By identifying distinct behavioral archetypes, healthcare providers and digital health platforms can deploy targeted, personalized interventions rather than one-size-fits-all clinical recommendations.

---

## 🔑 Key Strategic Findings: The 4 Behavioral Archetypes

Through silhouette score optimization and elbow analysis, four distinct behavioral profiles were identified:

### 1. Archetype 0: "Active & Balanced Conscious"
* **Behavioral Profile**: High physical activity frequency (`FAF`), high daily water intake (`CH2O`), consistent calorie tracking (`SCC`), and high vegetable consumption (`FCVC`).
* **Clinical Risk**: Low risk of obesity; strong metabolic baseline.
* **Target Intervention**: Maintenance programs, optimization of athletic performance, and preventive wellness tracking.

### 2. Archetype 1: "Sedentary Digital Lifestyle"
* **Behavioral Profile**: Elevated screen time (`TUE`), low physical activity (`FAF`), reliance on motorized transportation (`MTRANS`), and moderate-to-high snacking between meals (`CAEC`).
* **Clinical Risk**: Moderate-to-high risk of developing metabolic syndrome and gradual BMI increase.
* **Target Intervention**: Micro-activity integration (breaks during screen time), active commuting encouragement, and digital nudge notifications.

### 3. Archetype 2: "High-Caloric / Unstructured Eating"
* **Behavioral Profile**: Frequent consumption of high-calorie foods (`FAVC`), irregular main meal counts (`NCP`), frequent snacking, and low-to-moderate physical activity.
* **Clinical Risk**: High risk of severe obesity and associated cardiovascular comorbidities.
* **Target Intervention**: Nutritional restructuring, satiety-focused meal planning, and behavioral therapy for impulse eating.

### 4. Archetype 3: "Moderate Routine with Family Risk"
* **Behavioral Profile**: Average behavioral metrics with strong genetic predisposition (`family_history_with_overweight`) and moderate alcohol/snacking habits.
* **Clinical Risk**: Moderate baseline risk heavily influenced by environmental and family factors.
* **Target Intervention**: Family-centered lifestyle modifications, early screening, and habit-stacking routines.

---

## 🚀 Business & Clinical Impact

1. **Personalized Digital Health**: Enables healthtech platforms to automate user onboarding segmentation and deliver personalized habit-building recommendations.
2. **Resource Allocation**: Allows healthcare providers to stratify patient risk based on habits before biometric complications arise.
3. **Reproducible Pipeline**: All data transformations, domain constraint enforcement, and model inference steps are fully automated via an end-to-end Python pipeline (`main.py`).



# Executive Summary: Behavioral Health Analytics & Unsupervised Clustering

**Project:** Unsupervised Machine Learning for Behavioral Health Archetyping  
**Author:** Camila Chivelli  
**Domain:** Health Data Analytics / Machine Learning Engineering  

---

## 🎯 Executive Overview

Obesity management typically relies on isolated biometric indicators like Body Mass Index (BMI). However, BMI alone fails to capture the underlying lifestyle and behavioral drivers that dictate patient outcomes.

This project implements an **unsupervised K-Means clustering architecture** (K=4) to segment individuals based strictly on **behavioral, dietary, and physical activity patterns** (isolating biometric metrics to avoid data leakage). By identifying distinct behavioral archetypes, healthcare providers and digital health platforms can deploy targeted, personalized interventions rather than one-stop clinical recommendations.

---

## 🔑 Key Strategic Findings: The 4 Real Behavioral Archetypes

Through silhouette score optimization and elbow analysis, four distinct behavioral profiles were identified from the feature matrix:

### 1. Cluster 0: "Young, Low-Vegetable & Screen-Centric Profile"
* **Behavioral Markers**: Characterized by below-average vegetable consumption, younger age, and high daily technology/screen time.
* **Physical & Risk Profile**: Broad BMI distribution centered around ~27 kg/m². Spans mild-to-moderate categories (`Overweight I/II` and `Obesity Type I`), containing **0% Obesity Type III** cases.
* **Target Intervention**: Digital nudges for screen-time breaks, gamified physical activity, and nutritional education focusing on micronutrient/vegetable intake.

### 2. Cluster 1: "Older / Adult Population with High Metabolic Risk"
* **Behavioral Markers**: Strongly dominated by older individuals, lower physical activity, and significantly lower screen time.
* **Physical & Risk Profile**: Concentrates high BMI levels (median ~31 kg/m²). Over **80%** of its members belong to `Overweight Level II`, `Obesity Type I`, or `Obesity Type II`.
* **Target Intervention**: Low-impact mobility routines, cardiovascular risk monitoring, and age-adapted metabolic health management.

### 3. Cluster 2: "Low Main-Meal Frequency (Irregular Diet) Profile"
* **Behavioral Markers**: Defined by an extreme negative outlier in main meals per day, combined with lower physical activity.
* **Physical & Risk Profile**: Maintains lower-to-moderate BMI values (median ~26.5 kg/m²). Heavily populated by `Overweight Level I` (25.1%), `Normal Weight` (16.3%), and `Insufficient Weight` (13.8%).
* **Target Intervention**: Meal-timing stabilization, metabolic consistency programs, and addressing irregular eating/skipping meals.

### 4. Cluster 3: "Severe Obesity Profile (High Food & Vegetable Volume)"
* **Behavioral Markers**: Highest intake of vegetables, high meal frequency, and positive water consumption.
* **Physical & Risk Profile**: Exhibits the highest BMI distribution (median ~36 kg/m², up to >50 kg/m²). Captures **100% of all Obesity Type III cases** in the dataset (44.1% of this cluster).
* **Target Intervention**: Caloric density reduction, portion control, and comprehensive clinical intervention (high volume/portion intake drives outcomes despite high reported vegetable intake).

---

## 🚀 Business & Clinical Impact

1. **Personalized Digital Health**: Enables healthtech platforms to automate user onboarding segmentation and deliver personalized habit-building recommendations.
2. **Resource Allocation**: Allows healthcare providers to stratify patient risk based on behavioral habits before biometric complications arise.
3. **Reproducible Pipeline**: All data transformations, domain constraint enforcement, and model inference steps are fully automated via an end-to-end Python pipeline (`main.py`).