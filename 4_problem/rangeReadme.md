## 📏 Feature Valid Domain Ranges

To simulate real-world retail customer data constraints, the following valid ranges and category rules must be considered during preprocessing.

### 👤 Age

Valid Range:

18 → 65 years

Business Logic:

- Customers below 18 are not eligible buyers.
- Customers above 65 are extremely rare in premium retail purchase datasets.

---

### 💰 Salary

Valid Range:

10,000 → 2,00,000

Business Logic:

- Values below minimum threshold may indicate missing / incorrect entries.
- Extremely high salary values may indicate outliers or data entry issues.

---

### 🧑‍💻 Experience

Valid Range:

0 → (Age − 18)

Recommended Cap:

Maximum realistic experience ≈ 40 years.

Business Logic:

- Professional experience generally starts after age 18.
- Experience greater than age constraint indicates data inconsistency.

---

### 🏙 City

Valid Categories:

- Delhi  
- Mumbai  
- Chennai  
- Kolkata  
- Bangalore  

Business Logic:

- Any other category should be treated as inconsistent data.

---

### 🎓 Education (Ordinal Feature)

Correct Ranking Order:

School < Graduate < PostGraduate

Business Logic:

- This feature must preserve ordinal relationship during encoding.

---

### 🎯 Purchased (Target Variable)

Valid Values:

0 → Customer did not purchase  
1 → Customer purchased  

Business Logic:

- No missing values are allowed in target variable.
- Must remain binary.