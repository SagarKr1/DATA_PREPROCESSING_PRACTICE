# 💀 IMPOSSIBLE HR ATTRITION DATASET

## 📂 Dataset File

```bash
employee_risk_dataset.csv
```

---

## 📊 Dataset Size

* Total Rows → **10,000**
* Total Columns → **17**

---

## 📌 Column Ranges / Domain Rules

### 👤 age

* Expected Range → **18 to 60**
* Possible Dirty Values:

  * Negative values
  * Values > 100
  * Text values ("thirty")
  * Missing values

---

### 💰 salary

* Expected Range → **10,000 to 200,000**
* Possible Dirty Values:

  * "45k"
  * "₹60000"
  * "70,000"
  * Negative salary
  * Extreme outlier → 9999999

---

### 🧑‍💻 experience_years

* Expected Range → **0 to 40**
* Logical Rule:

  * experience_years ≤ age − 18
* Possible Dirty Values:

  * "ten"
  * 50
  * Missing

---

### ⭐ performance_score

* Range → **1 to 5**
* 32% Missing

---

### ⏱ work_hours_per_week

* Expected Range → **30 to 60**
* Dirty Values:

  * 10
  * 120

---

### 🏠 remote_work_ratio

* Range → **0 to 100 (%)**

---

### 😊 job_satisfaction

* Range → **1 to 10**
* 41% Missing

---

### 🎁 bonus

* Expected Range → **0 to 50% of salary**
* 70% Missing
* Some values → 0 even for high salary

---

### 📅 joining_date

Formats Present:

```
12-05-2018
2017/07/01
March 3 2019
32/01/2020
NULL
```

---

### 🏢 department (Standard Expected)

* IT
* HR
* Finance
* Sales
* Operations

Dirty Values:

```
it
Information Technology
Human Resource
FIN
NULL
```

---

### 📍 city

Possible Values:

* Mumbai
* Delhi
* Bangalore
* Pune
* Kolkata
* Chennai
* NULL

---

### 🧠 manager_rating

* Range → **1 to 5**

---

### 🎓 training_hours

* Range → **0 to 200**

---

### 💳 loan_default_history

* Yes / No

---

### 🎯 left_company (Target)

* Yes → ~9%
* No → ~91%

---

## 🎯 Your Mission

You must:

* Clean this dataset logically
* Perform full EDA
* Detect attrition patterns
* Do hypothesis testing
* Design risk score

---

## ⚠️ IMPORTANT

This dataset is intentionally:

* Noisy
* Biased
* Inconsistent
* Logically conflicting
* Statistically dangerous

You must justify every decision.

---

## 🔥 Difficulty

```
IMPOSSIBLE++
```
