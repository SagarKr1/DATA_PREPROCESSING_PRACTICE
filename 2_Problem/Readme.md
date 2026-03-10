# 🧠 Data Preprocessing + EDA Challenge (Superstore Dataset)

## Overview

You are hired as a **Data Analyst for a retail company**.

The company has provided a **sales dataset (Superstore)** containing information about orders, customers, products, and profits.

Your job is to **clean, preprocess, and analyze the dataset** before the business team uses it for decision making.

Dataset:

Sample - Superstore.csv

Dataset Size:

- ~10,000 rows
- ~20 columns

You must perform **data preprocessing, descriptive statistics, outlier detection, distribution analysis, and exploratory data analysis (EDA).**

---

# 📂 Dataset Columns

The dataset contains the following columns:

Order ID  
Order Date  
Ship Date  
Ship Mode  
Customer ID  
Customer Name  
Segment  
Country  
City  
State  
Region  
Product ID  
Category  
Sub-Category  
Product Name  
Sales  
Quantity  
Discount  
Profit  

---

# 🎯 Task 1 — Dataset Inspection

Perform initial inspection.

Tasks:

1. Display the first 10 rows of the dataset.
2. Identify the shape of the dataset.
3. List the data types of each column.
4. Check for missing values.
5. Check for duplicate rows.

Questions:

- How many rows and columns exist?
- Which columns contain missing values?
- Are duplicate records present?

---

# 🎯 Task 2 — Data Type Correction

Check whether the following columns have correct data types:

Order Date  
Ship Date  

Convert them into **datetime format**.

Create new features:

- order_year  
- order_month  
- order_day  

---

# 🎯 Task 3 — Data Cleaning

Perform the following preprocessing steps:

1. Remove duplicate rows.
2. Remove or fix rows where:
   - Sales ≤ 0
   - Quantity ≤ 0
3. Ensure categorical columns do not contain extra spaces.

Columns to clean:

Segment  
Region  
Category  
Sub-Category  
Ship Mode  

---

# 🎯 Task 4 — Descriptive Statistics

Calculate descriptive statistics for the following columns:

Sales  
Quantity  
Discount  
Profit  

Compute:

- Mean
- Median
- Mode
- Standard Deviation
- Minimum
- Maximum
- Quartiles (Q1, Q2, Q3)
- Interquartile Range (IQR)

---

# 🎯 Task 5 — Outlier Detection

Detect outliers using the **IQR method (1.5 × IQR rule)**.

Columns to analyze:

Sales  
Profit  
Discount  

Tasks:

- Identify outliers.
- Decide whether to keep or remove them.
- Justify your decision.

---

# 🎯 Task 6 — Distribution Analysis

Analyze the distribution of the following variables:

Sales  
Profit  
Quantity  
Discount  

Create visualizations:

- Histogram
- Boxplot
- KDE Distribution Plot

Explain whether the distributions are:

- Normal
- Right-skewed
- Left-skewed

---

# 🎯 Task 7 — Exploratory Data Analysis (EDA)

Answer the following business questions.

1. Which **category generates the highest total sales?**
2. Which **sub-category generates the highest profit?**
3. Which **region generates the highest revenue?**
4. Which **city has the most orders?**
5. What is the **monthly sales trend?**
6. Which **segment contributes the most profit?**
7. Which **products have the highest sales?**
8. What is the relationship between **discount and profit?**

---

# 🎯 Task 8 — Correlation Analysis

Analyze correlations between numerical columns.

Columns:

Sales  
Quantity  
Discount  
Profit  

Create a **correlation heatmap**.

Explain:

- Positive correlation
- Negative correlation
- Weak correlation

---

# 🎯 Task 9 — Final Insights

Provide **at least 5 business insights** based on your EDA.

Examples:

- Most profitable category
- Most profitable region
- Impact of discounts on profit
- Seasonal sales patterns

---

# 📦 Deliverables

Your submission must include:

1. Python code
2. Cleaned dataset summary
3. Visualizations
4. Business insights

Recommended Libraries:

- pandas
- numpy
- matplotlib
- seaborn

---

# 🚀 Goal

This challenge simulates **real-world tasks performed by data analysts and data scientists when working with retail sales datasets.**