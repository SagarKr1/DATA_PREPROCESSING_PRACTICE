# 📊 Domain Knowledge & Valid Value Ranges

(Customer Behaviour Dataset)

This document provides realistic business constraints and valid ranges for each feature.

These ranges help in:

* Detecting inappropriate values
* Identifying logical outliers
* Choosing correct imputation strategy
* Making meaningful statistical decisions

---

## 🧍 Age

* Minimum Valid Age → **18**
* Maximum Valid Age → **70**

Notes:

* Customers below 18 are not eligible.
* Age above 70 is considered highly unlikely for active retail engagement.

---

## 💰 Monthly Income (INR)

* Minimum Valid Income → **₹8,000**
* Typical Range → **₹15,000 – ₹1,20,000**
* Extreme but Possible → **₹2,50,000**

Notes:

* Income below ₹8,000 may indicate data entry error.
* Income above ₹2,50,000 should be carefully validated.

---

## 🎯 Spending Score

Represents customer engagement level.

* Valid Range → **1 to 100**

Notes:

* Values outside this range are invalid.
* Higher score → Higher engagement / loyalty.

---

## 🏙️ City Tier

Categorical Feature.

Valid Values:

* Tier1 → Metro Cities
* Tier2 → Developing Cities
* Tier3 → Small Cities

Notes:

* No other category should exist.

---

## 🚗 Owns Car

Binary Feature.

Valid Values:

* 0 → Does NOT own car
* 1 → Owns car

Notes:

* Any other value is invalid.

---

## 🛒 Online Purchases per Month

Represents number of purchases.

* Minimum → **0**
* Typical Range → **0 to 20**
* Rare Extreme → **30**

Notes:

* Negative values are invalid.
* Very high values should be validated.

---

## 🆔 Customer ID

* Must be unique
* Must not contain missing values

---

## 🎯 Purpose of Domain Constraints

These ranges are NOT strict filtering rules.

They are **guidelines to support analytical thinking** during:

* Data Cleaning
* Outlier Detection
* Hypothesis Testing

Final decisions should be supported by:

* Statistical Evidence
* Business Logic
* EDA Observations
