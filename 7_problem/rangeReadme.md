# 📘 Domain Knowledge & Range Validation Guide

## 🎯 Objective

Use this guide to validate and clean the dataset using **domain knowledge and valid ranges** before performing EDA and hypothesis testing.

---

## 🔹 1. customer_id

**Description:** Unique identifier for each customer

### ✅ Valid Rules:

* Must be **unique**
* Must be **positive integer**
* No duplicates allowed

### ⚠️ Invalid:

* Duplicate IDs
* Negative values
* Null values

---

## 🔹 2. age

**Description:** Age of customer

### ✅ Valid Range:

* **18 – 65** (dataset-specific)
* Acceptable real-world range: **0 – 100**

### ⚠️ Invalid:

* age < 0
* age > 100

---

## 🔹 3. gender

**Description:** Gender of customer

### ✅ Valid Values:

* Male
* Female

### ⚠️ Invalid:

* Any other category
* Null / empty values

---

## 🔹 4. income

**Description:** Annual income of customer

### ✅ Valid Range:

* **20,000 – 150,000** (dataset-specific)
* Must be **non-negative**

### ⚠️ Invalid:

* income < 0
* Extremely high unrealistic values (e.g., > 1,000,000)

---

## 🔹 5. spending_score

**Description:** Customer spending score

### ✅ Valid Range:

* **1 – 100**

### ⚠️ Invalid:

* spending_score < 1
* spending_score > 100

---

## 🔹 6. region

**Description:** Customer region

### ✅ Valid Values:

* North
* South
* East
* West

### ⚠️ Invalid:

* Any other category
* Null values

---

## 🔹 7. purchase_frequency

**Description:** Number of purchases

### ✅ Valid Range:

* **1 – 50** (dataset-specific)
* Must be **positive integer**

### ⚠️ Invalid:

* purchase_frequency ≤ 0
* Extremely high unrealistic values

---

## 🔹 8. churn

**Description:** Customer churn status

### ✅ Valid Values:

* Yes
* No

### ⚠️ Invalid:

* Any other value
* Null values

---

## 🔥 Validation Checklist

* [ ] Remove duplicates (customer_id)
* [ ] Check numeric ranges (age, income, spending_score, purchase_frequency)
* [ ] Validate categorical values (gender, region, churn)
* [ ] Handle missing values
* [ ] Detect unrealistic values using domain knowledge

---

## 🚀 Rule

> Always apply **Domain Knowledge + Statistical Methods (Hybrid Approach)** for best results.
