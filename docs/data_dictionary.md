# Data Dictionary: Behavioral Health & Obesity Dataset

This document details the variables, definitions, measurement units, domain constraints, and encoding strategies used across the Behavioral Health Analytics pipeline.

---

## 1. Biometric & Demographic Features (Non-Predictors)

These features represent physical measurements and demographic identifiers. To prevent **data leakage** during behavioral clustering, biometric metrics (`Height`, `Weight`) and target labels (`NObeyesdad`) were isolated from the training feature matrix.

| Variable | Type | Description | Unit / Range | Pipeline Treatment |
| :--- | :--- | :--- | :--- | :--- |
| **Gender** | Categorical | Biological sex of the participant | `Male`, `Female` | Binary Encoded (`0`/`1`) |
| **Age** | Continuous | Age of the individual | 14–61 years | Scaled (`StandardScaler`) |
| **Height** | Continuous | Height in meters | 1.45–1.98 m | Biometric label (Isolated) |
| **Weight** | Continuous | Body mass in kilograms | 39.0–173.0 kg | Biometric label (Isolated) |
| **NObeyesdad**| Categorical | Official WHO Obesity Category | 7 ordinal levels | Isolated Target Class |

---

## 2. Eating Habits & Dietary Behaviors (Predictors)

Variables capturing nutritional choices, eating frequency, and caloric intake behaviors.

| Feature Acronym | Full Feature Name | Description | Measurement / Scale | Technical Constraints |
| :--- | :--- | :--- | :--- | :--- |
| **FAVC** | High Caloric Food Consumption | Frequent consumption of high caloric food | Binary (`Yes` / `No`) | Encoded as `1` / `0` |
| **FCVC** | Frequency of Vegetable Consumption | Daily frequency of vegetable intake | 1 (Rarely) to 3 (Always) | Clipped $[1, 3]$, Scaled |
| **NCP** | Number of Main Meals | Daily main meal count | 1 to 3 meals | Clipped $[1, 3]$, Scaled |
| **CAEC** | Food Between Meals | Consumption of food between main meals | `no`, `Sometimes`, `Frequently`, `Always` | Ordinal Mapping (`0`–`3`) |
| **CH2O** | Daily Water Intake | Daily water consumption | 1 (<1L), 2 (1–2L), 3 (>2L) | Clipped $[1, 3]$, Scaled |
| **CALC** | Alcohol Consumption | Frequency of alcohol intake | `no`, `Sometimes`, `Frequently`, `Always` | Ordinal Mapping (`0`–`3`) |

---

## 3. Physical Activity & Lifestyle Behaviors (Predictors)

Variables describing energy expenditure, sedentary screen time, habits, and transportation.

| Feature Acronym | Full Feature Name | Description | Measurement / Scale | Technical Constraints |
| :--- | :--- | :--- | :--- | :--- |
| **FAF** | Physical Activity Frequency | Weekly physical activity frequency | 0 (None) to 3 (4+ days) | Clipped $[0, 3]$, Scaled |
| **TUE** | Time Using Technology Devices | Daily screen time / sedentary tech use | 0 (0–2 hrs), 1 (3–5 hrs), 2 (>5 hrs) | Clipped $[0, 2]$, Scaled |
| **SMOKE** | Smoking Habit | Whether the participant smokes | Binary (`Yes` / `No`) | Encoded as `1` / `0` |
| **SCC** | Calories Monitoring | Tracks daily caloric intake | Binary (`Yes` / `No`) | Encoded as `1` / `0` |
| **family_history_with_overweight** | Family History | Overweight history in immediate family | Binary (`Yes` / `No`) | Encoded as `1` / `0` |
| **MTRANS** | Transportation Mode | Primary mode of transport used | `Automobile`, `Motorbike`, `Bike`, `Public_Transportation`, `Walking` | One-Hot Encoded (`MTRANS_*`) |
