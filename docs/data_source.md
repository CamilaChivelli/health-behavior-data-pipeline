# Dataset Provenance & Survey Methodology

This document details the original data source, problem domain, collection methodology, hybrid generation mechanics, and survey structure used to build the dataset for this project.

---

## 1. Problem Domain & Context

The dataset focuses on estimating obesity levels among individuals from **Mexico, Peru, and Colombia**, three Latin American nations with diverse nutritional and socioeconomic profiles. 

Unlike traditional clinical diagnostics that rely solely on physical measurements, this domain integrates standard biometric data with detailed behavioral indicators. This behavioral dimension captures key lifestyle factors, including:
* Family genetic history.
* Consumption of high-caloric food.
* Eating frequency and hydration habits.
* Modern sedentary markers, such as technology usage and screen time.

---

## 2. Source & Data Provenance

* **Original Research Paper**: Palechor, F. M., & de la Hoz Manotas, A. (2019). *Dataset for estimation of obesity levels based on eating habits and physical condition in individuals from Mexico, Peru and Colombia*. **Data in Brief**, 25, 104080.
* **Public Repository**: [UCI Machine Learning Repository - Estimation of Obesity Levels Based On Eating Habits and Physical Condition](https://archive.ics.uci.edu/ml/datasets/Estimation+of+obesity+levels+based+on+eating+habits+and+physical+condition+)

---

## 3. Data Collection & Synthetic Augmentation

The original dataset was collected via a 30-day open online survey platform. To address sample size constraints for machine learning model training, a **hybrid sampling strategy** was implemented by the original researchers:

* **Real Data (23%)**: 485 empirical records gathered from anonymous web platform respondents.
* **Synthetic Data (77%)**: 1,626 additional records generated using the **Weka** framework and the **SMOTE** (Synthetic Minority Over-sampling Technique) filter to balance target class distributions.
* **Total Dataset Size**: 2,111 instances with 17 attributes.

> **Methodological Note on Duplicates**: Synthetic data generation via SMOTE can result in near-identical feature vectors for continuous attributes. Rather than discarding these as invalid duplicate observations, they represent valid synthetic feature combinations and are intentionally preserved in the data cleaning pipeline (`scripts/data_cleaning.py`).

---

## 4. Survey Questions & Measurement Scale

The underlying survey instrument consisted of 16 structured questions designed to capture demographic, dietary, physical activity, and technological habits.

| Feature Name | Original Survey Question | Possible Answer Options |
| :--- | :--- | :--- |
| **Gender** | *What is your gender?* | Female, Male |
| **Age** | *What is your age?* | Numeric value (Years) |
| **Height** | *What is your height?* | Numeric value (Meters) |
| **Weight** | *What is your weight?* | Numeric value (Kilograms) |
| **family_history_with_overweight** | *Has a family member suffered or suffers from overweight?* | Yes, No |
| **FAVC** | *Do you eat high caloric food frequently?* | Yes, No |
| **FCVC** | *Do you usually eat vegetables in your meals?* | Never, Sometimes, Always |
| **NCP** | *How many main meals do you have daily?* | Between 1 and 2, 3, More than three |
| **CAEC** | *Do you eat any food between meals?* | No, Sometimes, Frequently, Always |
| **SMOKE** | *Do you smoke?* | Yes, No |
| **CH2O** | *How much water do you drink daily?* | Less than a liter, Between 1 and 2 L, More than 2 L |
| **SCC** | *Do you monitor the calories you eat daily?* | Yes, No |
| **FAF** | *How often do you have physical activity?* | I do not have, 1 or 2 days, 2 or 4 days, 4 or 5 days |
| **TUE** | *How much time do you use technological devices such as cell phone, videogames, television, computer and others?* | 0–2 hours, 3–5 hours, More than 5 hours |
| **CALC** | *How often do you drink alcohol?* | I do not drink, Sometimes, Frequently, Always |
| **MTRANS** | *Which transportation do you usually use?* | Automobile, Motorbike, Bike, Public Transportation, Walking |

---

## 5. Target Classification Standards

Target labels (`NObeyesdad`) were calculated based on the Body Mass Index ($\text{BMI} = \text{Weight} / \text{Height}^2$) and categorized according to standards set by the **World Health Organization (WHO)** and **Mexican Health Norms**:

* **Insufficient Weight**: $\text{BMI} < 18.5$
* **Normal Weight**: $18.5 \le \text{BMI} < 25.0$
* **Overweight Level I**: $25.0 \le \text{BMI} < 27.0$
* **Overweight Level II**: $27.0 \le \text{BMI} < 30.0$
* **Obesity Type I**: $30.0 \le \text{BMI} < 35.0$
* **Obesity Type II**: $35.0 \le \text{BMI} < 40.0$
* **Obesity Type III**: $\text{BMI} \ge 40.0$
