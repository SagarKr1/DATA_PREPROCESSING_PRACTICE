# 🧠 Data Preprocessing Challenge (50K Dataset)

## 📌 Domain

This dataset belongs to **Retail Customer Purchase Prediction Domain.**

A retail company wants to understand customer behaviour before building a Machine Learning model to predict whether a customer will purchase a premium product or not.

You are hired as a **Junior Data Scientist** to perform full Data Cleaning and Exploratory Data Analysis.

---

## 🎯 Problem Statement

The dataset contains **raw customer demographic and financial data** collected from multiple sources.

The data is:

- Incomplete
- Noisy
- Contains outliers
- Contains categorical and ordinal features
- Not ready for ML usage

Your task is to:

> Convert this raw dataset into a **clean, structured, ML-ready dataset.**

---

## 📊 Dataset Description

Total Rows → 50,000  
Total Columns → 6  

### Features

| Column | Description | Type |
|-------|------------|------|
| age | Age of customer | Numerical |
| salary | Annual salary | Numerical |
| experience | Work experience in years | Numerical |
| city | Customer city | Categorical |
| education | Education level | Ordinal |
| purchased | Target variable (0 = No, 1 = Yes) | Binary |

---

## ⚠️ Real World Issues Present in Dataset

The dataset intentionally contains:

- Missing values
- Extreme salary values
- Distribution imbalance
- Categorical inconsistencies
- Ordinal ranking requirement

---

## 🧩 Your Responsibilities

You must:

### ✅ Perform EDA

- Understand distribution of numerical features
- Identify skewness
- Identify relationships (if any)

### ✅ Handle Missing Values

- Choose appropriate strategy
- Justify WHY you chose that method

### ✅ Handle Outliers

- Detect properly
- Decide whether to remove / cap / transform

### ✅ Handle Categorical Data

- Convert into numerical representation

### ✅ Handle Ordinal Data

- Apply proper ranking based on domain understanding

### ✅ Prepare Final Dataset

Final dataset must:

- Have no missing values
- Have controlled outliers
- Be fully numerical
- Be ready for ML model training

---

## 📤 Submission Requirements

Submit:

1. EDA Observations
2. Missing Value Handling Strategy (with reasoning)
3. Outlier Handling Strategy (with reasoning)
4. Encoding Method Used
5. Final Dataset Shape
6. Python Code

---

## 🚫 Restrictions

- Do not assume data is clean
- Do not randomly drop rows
- Every decision must be justified
- Work like a real Data Scientist

---

## ⭐ Goal

This assignment is designed to test:

- Data understanding
- Preprocessing decision making
- Statistical thinking
- Domain reasoning
- Coding implementation