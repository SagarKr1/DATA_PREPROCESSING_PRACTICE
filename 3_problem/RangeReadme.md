# 📏 Full Domain Validation Ranges

Dataset: **food_delivery_orders.csv**

Total Rows: ~12,000
Total Columns: 11

Before performing **data preprocessing and EDA**, the dataset must satisfy the following **domain validation constraints.**

---

## 🆔 order_id

Description: Unique identifier of each order.

Validation Rules:

* Must be **positive integer**
* Must be **unique**
* Cannot be null

Valid Range:

```
order_id > 0
```

---

## 👤 customer_id

Description: Identifier of customer placing the order.

Validation Rules:

* Must be **positive integer**
* One customer may place multiple orders
* Cannot be null

Valid Range:

```
customer_id > 0
```

---

## 🍽 restaurant_name

Description: Name of restaurant fulfilling the order.

Validation Rules:

* Must be **non-null string**
* Must not contain numeric corruption
* Must be consistently formatted (case and spacing)

---

## 🌆 city

Description: Delivery location city.

Validation Rules:

* Must be **non-null string**
* Must represent a valid city name
* Must not contain numeric corruption or invalid symbols

```
delhi
mumbai
bangalore
hyderabad
chennai
kolkata
pune
```
---

## 💰 order_amount

Description: Total value of the order.

Validation Rules:

```
order_amount > 0
```

Typical Business Range:

```
50 ≤ order_amount ≤ 3000
```

Outlier Consideration:

* Extremely high values should be investigated

---

## ⏱ delivery_time (minutes)

Description: Time taken to deliver the order.

Validation Rules:

```
5 ≤ delivery_time ≤ 120
```

Business Logic:

* Delivery cannot realistically take less than 5 minutes
* Deliveries exceeding 2 hours are considered abnormal

---

## ⭐ rating

Description: Customer rating for the order.

Validation Rules:

```
1 ≤ rating ≤ 5
```

Business Logic:

* Must follow standard 5-point rating scale

---

## 💳 payment_method

Expected Clean Categories:

```
cash
upi
card
```

Validation Rules:

* Must belong to one of the allowed categories
* Must be consistently formatted

---

## 📅 order_date

Description: Date when the order was placed.

Validation Rules:

* Must be valid datetime
* Cannot be null

Typical Dataset Range:

```
Within operational business period (example: Jan–Jun 2024)
```

---

## 🧑‍🦱 delivery_partner_age

Description: Age of delivery partner.

Validation Rules:

```
18 ≤ delivery_partner_age ≤ 60
```

Business Logic:

* Legal working age minimum is 18
* Extremely high ages are unrealistic for delivery operations

---

## 📍 distance_km

Description: Distance between restaurant and customer.

Validation Rules:

```
0 < distance_km ≤ 50
```

Business Logic:

* Distance cannot be zero or negative
* Food delivery rarely exceeds 50 km radius

---

## 🎯 Purpose of Domain Validation

Applying these constraints ensures:

* Removal of corrupted records
* Reliable statistical summaries
* Accurate EDA insights
* Better business decision making
