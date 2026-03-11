# 🍔 Food Delivery Data Preprocessing + EDA Challenge

## 📊 Scenario

You are hired as a **Junior Data Analyst at a Food Delivery Company.**

The company has exported raw order transaction data which is:

* messy
* inconsistent
* contains outliers
* contains invalid categorical values

Before building dashboards and reports, your job is to:

> **Clean the dataset and perform Exploratory Data Analysis (EDA).**

---

## 📂 Dataset

File Name:

```
food_delivery_orders.csv
```

Approx Rows:

```
~12,000
```

---

## 📌 Columns Description

| Column               | Description              |
| -------------------- | ------------------------ |
| order_id             | Unique order ID          |
| customer_id          | Customer identifier      |
| restaurant_name      | Restaurant name          |
| city                 | Delivery city            |
| order_amount         | Total order value        |
| delivery_time        | Delivery time (minutes)  |
| rating               | Customer rating          |
| payment_method       | Payment mode             |
| order_date           | Order date               |
| delivery_partner_age | Age of delivery partner  |
| distance_km          | Distance from restaurant |

---

## 🎯 Task 1 — Dataset Inspection

You must:

* Show first few rows
* Show dataset shape
* Check data types
* Check missing values
* Check duplicate rows

---

## 🎯 Task 2 — Domain Validation

Apply the following validation rules:

### Order Amount

```
order_amount > 0
```

### Delivery Time

```
5 ≤ delivery_time ≤ 120
```

### Rating

```
1 ≤ rating ≤ 5
```

### Delivery Partner Age

```
18 ≤ delivery_partner_age ≤ 60
```

### Distance

```
0 < distance_km ≤ 50
```

---

## 🎯 Task 3 — Categorical Cleaning

Clean the following columns:

* city
* payment_method
* restaurant_name

Tasks:

* convert to lowercase
* remove extra spaces
* fix inconsistent naming

---

## 🎯 Task 4 — Date Processing

Convert:

```
order_date → datetime
```

Extract:

```
order_month
order_day
```

---

## 🎯 Task 5 — Descriptive Statistics

For these columns:

* order_amount
* delivery_time
* rating
* distance_km

Calculate:

* mean
* median
* mode
* standard deviation
* quartiles
* IQR

---

## 🎯 Task 6 — Outlier Detection

Using **IQR Method**, detect outliers in:

* order_amount
* delivery_time
* distance_km

Decide whether to remove or keep.

---

## 🎯 Task 7 — Exploratory Data Analysis (EDA)

Answer the following:

1. Which **city has the highest number of orders**
2. Which **restaurant generates highest revenue**
3. Average **delivery time per city**
4. Monthly **order trend**
5. Most used **payment method**
6. Relationship between **distance and delivery_time**
7. Average **rating per restaurant**

---

## 🎯 Task 8 — Final Insights

Provide **at least 5 business insights.**

---

## 📦 Deliverables

Your submission must include:

* Python code / Notebook
* Cleaned dataset summary
* EDA results
* Business insights

---

## 🚀 Goal

This challenge simulates **real-world data preprocessing and EDA tasks** performed by junior data analysts.
