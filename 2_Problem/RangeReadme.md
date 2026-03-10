# 📊 Data Validation Rules (Domain Constraints)

## Dataset

**Sample - Superstore.csv**

Before performing **data preprocessing and exploratory data analysis (EDA)**, the dataset must satisfy the following **domain validation rules** based on retail business logic.

---

# 1. Identifier Columns

## Row ID

Description: Unique identifier for each row.

Validation Rules:

- Must be a **positive integer**
- Must be **unique**
- Cannot be **null**

Valid Range:

```
Row ID > 0
```

---

## Order ID

Description: Unique order identifier.

Validation Rules:

- Must be **non-null**
- Should follow a **consistent format**
- Multiple rows may share the same Order ID (because one order may contain multiple products)

---

## Customer ID

Description: Unique identifier for a customer.

Validation Rules:

- Must be **non-null**
- Must follow a **consistent ID format**
- One customer may place multiple orders

---

## Product ID

Description: Unique identifier for a product.

Validation Rules:

- Must be **non-null**
- Must follow a **consistent ID format**

---

# 2. Date Columns

## Order Date

Description: Date when the order was placed.

Validation Rules:

- Must be a **valid date**
- Cannot be **null**

---

## Ship Date

Description: Date when the order was shipped.

Validation Rules:

- Must be a **valid date**
- Must be **greater than or equal to Order Date**

Constraint:

```
Ship Date ≥ Order Date
```

---

# 3. Categorical Columns

## Ship Mode

Valid Categories:

```
Standard Class
Second Class
First Class
Same Day
```

Rules:

- Values must belong to the valid categories
- No spelling inconsistencies
- No extra spaces

---

## Segment

Valid Categories:

```
Consumer
Corporate
Home Office
```

Rules:

- Must match one of the allowed categories

---

## Country

Expected Value:

```
United States
```

Rules:

- Must be non-null
- Must contain valid country name

---

## City

Description
Represents the city where the customer is located.

Validation Rules

* Must be a **valid city name**
* Cannot be **null or empty**
* Must not contain **numbers or special characters**
* Must belong to a **valid U.S. city**

Expected Domain

Cities should belong to the **United States**.

Examples of Valid Values

```
New York
Los Angeles
Chicago
Houston
Philadelphia
San Francisco
Seattle
Boston
Dallas
Miami
```

General Constraints

```
City must be a valid U.S. city name
```

---

## State

Description
Represents the U.S. state where the order was placed.

Validation Rules

* Must be a **valid U.S. state name**
* Cannot be **null**
* Must match one of the official **U.S. states**

Expected Range

```
Total valid states: 50
```

Examples of Valid Values

```
California
Texas
New York
Washington
Florida
Illinois
Pennsylvania
Ohio
Michigan
North Carolina
```

General Constraints

```
State must be a valid U.S. state
```

---

## Postal Code

Description
Represents the ZIP code of the customer location.

Validation Rules

* Must be a **positive integer**
* Must represent a **valid U.S. ZIP code**
* Cannot be negative
* Cannot be null

Expected Range

```
10000 ≤ Postal Code ≤ 99999
```

Examples

```
10024
30318
60601
94122
98103
```

General Constraints

```
Postal Code must be a valid 5-digit U.S. ZIP code
```

---


## Region

Valid Categories:

```
West
East
Central
South
```

Rules:

- Must match one of the allowed regions

---

## Category

Valid Categories:

```
Furniture
Office Supplies
Technology
```

Rules:

- Must match one of the allowed categories

---

## Sub-Category

Valid Categories:

```
Chairs
Tables
Bookcases
Phones
Storage
Binders
Machines
Accessories
Copiers
Appliances
Paper
Furnishings
Art
Envelopes
Labels
Fasteners
Supplies
```

Rules:

- Must match valid sub-categories

---

# 4. Numerical Columns

## Sales

Description: Total revenue generated from the order line.

Validation Rules:

- Must be **positive**
- Cannot be **zero or negative**

Valid Range:

```
Sales > 0
```

---

## Quantity

Description: Number of units sold.

Validation Rules:

- Must be a **positive integer**

Valid Range:

```
1 ≤ Quantity ≤ 20
```

---

## Discount

Description: Discount applied to the product.

Validation Rules:

- Must be between **0 and 1**

Valid Range:

```
0 ≤ Discount ≤ 1
```

Interpretation:

- 0.10 → 10% discount
- 0.50 → 50% discount

---

## Profit

Description: Profit generated from the order.

Validation Rules:

- Profit may be **positive or negative**
- Negative profit represents **loss**

Typical Range:

```
-10,000 ≤ Profit ≤ 10,000
```

---

## Postal Code

Description: Geographic postal code.

Validation Rules:

- Must be a **positive integer**
- Must represent a valid postal code

Typical Range:

```
10000 ≤ Postal Code ≤ 99999
```

---

# 5. General Data Quality Rules

The dataset must also satisfy the following quality checks:

- No duplicate rows
- No null values in critical identifier columns
- No invalid categorical values
- No invalid numerical values outside domain ranges
- Dates must follow logical order (Ship Date ≥ Order Date)

---

# Goal

Applying these validation rules ensures that the dataset is **clean, reliable, and ready for Exploratory Data Analysis (EDA) and business insights.**