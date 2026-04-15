# 💀 Employee Risk Dataset — Domain Ranges

## Dataset Size

- Rows → 10,000
- Columns → 17

---

## Column Domain Expectations

### age

- Expected → 18 — 60
- Dirty → negative / >100 / text / missing

### salary

- Expected → 10,000 — 200,000
- Dirty → currency symbols / commas / k format / negative / extreme outlier

### experience_years

- Expected → 0 — 40
- Logical Rule → experience ≤ age − 18

### performance_score

- Range → 1 — 5
- Heavy Missing (~30%)

### work_hours_per_week

- Expected → 30 — 60
- Dirty → 10 / 120

### remote_work_ratio

- Range → 0 — 100 %

### job_satisfaction

- Range → 1 — 10
- Heavy Missing (~40%)

### bonus

- Expected → 0 — 50% of salary
- Very High Missing (~70%)

### joining_date

Formats Mixed:

- DD-MM-YYYY
- YYYY/MM/DD
- Month DD YYYY
- Invalid Dates
- NULL

### department

Standard Expected:

- IT
- HR
- Finance
- Sales
- Operations

Dirty:

- lowercase
- abbreviations
- synonyms
- missing

### manager_rating

- Range → 1 — 5

### training_hours

- Range → 0 — 200

### loan_default_history

- Yes / No

### left_company (Target)

- Imbalanced:
  - Yes → ~9%
  - No → ~91%

---

## Objective

- Full preprocessing
- EDA
- Hypothesis testing
- Attrition risk modelling
- Business insight extraction

---

## Difficulty

IMPOSSIBLE++

```

```
