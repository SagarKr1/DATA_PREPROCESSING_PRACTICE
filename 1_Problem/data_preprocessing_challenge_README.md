
# 🧠 Data Preprocessing Challenge (Hard Level)

## Overview

You are hired as a **Data Analyst for a multinational company**.

The HR department exported an **employee dataset**, but the data is **dirty, inconsistent, and unreliable**.

Your task is to **clean and preprocess the dataset** using **data preprocessing techniques** before any analysis or machine learning.

Dataset size:

- 5000 rows
- 9 columns

---

# 📂 Dataset

File:

hard_employee_dataset.csv

Columns:

| Column | Description |
|------|-------------|
| emp_id | Employee ID |
| name | Employee name |
| age | Age of employee |
| gender | Gender |
| department | Department |
| salary | Monthly salary |
| experience | Years of experience |
| city | City of office |
| join_date | Employee joining date |

---

# 🎯 Challenge Objective

Prepare a **clean dataset** that follows the **company's data validation rules**.

You must implement **data preprocessing techniques** including:

- Data validation
- Duplicate detection
- Data cleaning
- Categorical normalization
- Data type handling

---

# 🧠 Company Data Rules

## Age

Employees must satisfy:

18 ≤ age ≤ 60

---

## Salary

Salary must be:

salary > 0

---

## Experience

Experience must be:

experience ≥ 0

---

## Valid Gender Categories

Male  
Female

---

## Valid Departments

IT  
HR  
Finance  
Sales  
Marketing

---

## Valid Cities

Delhi  
Mumbai  
Chennai  
Bangalore  
Kolkata

---

# 🧩 Tasks

## Task 1 — Identify Column Types

Classify each column as:

- Numerical
- Categorical
- Ordinal
- Pure String
- Date

---

## Task 2 — Detect and Remove Duplicates

Identify and remove:

- Duplicate rows
- Duplicate employee IDs

---

## Task 3 — Validate Numerical Columns

Check the following columns:

age  
salary  
experience  

Remove rows that violate the company rules.

---

## Task 4 — Clean Categorical Columns

Clean the following columns:

gender  
department  
city  

Fix:

- Case inconsistencies
- Spelling mistakes
- Extra spaces
- Invalid categories

---

## Task 5 — Domain Validation

Ensure categorical columns contain **only valid domain values**.

Invalid values must be corrected or removed.

---

## Task 6 — Date Processing

Convert:

join_date

into **datetime format**.

Extract:

joining_year  
joining_month

---

## Task 7 — Final Analysis

After cleaning the dataset, perform the following analysis:

1. Average salary per department
2. Number of employees per city
3. Average experience per department
4. Top 3 highest paying departments

---

# ⚠️ Challenge Rules

You must:

- Use Python (preferably **Pandas**)
- Show **data before and after cleaning**
- Explain what was removed and why

---

# 🧪 Deliverables

Your submission should include:

- Python preprocessing code
- Clean dataset summary
- Final analysis results

---

# 🧠 Difficulty Level

Dataset size: 5000 rows  
Difficulty: HARD  
Type: Real-world messy dataset

---

# 🚀 Goal

This challenge simulates **real-world data preprocessing tasks** performed by data analysts and data scientists before applying machine learning models.
