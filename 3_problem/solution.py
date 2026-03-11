import pandas as pd
import numpy as np

# Import csv dataset
foodDelivery = pd.read_csv("food_delivery_orders.csv", encoding="latin1")
print(foodDelivery.head())
print(foodDelivery.info())

# step 1. Identifying Data Columns
#   Column                Non-Null Count  Dtype
# ---  ------                --------------  -----
#  0   order_id              12000 non-null  int64 ----------> Numerical : continous
#  1   customer_id           12000 non-null  int64 ----------> Numerical : continous
#  2   restaurant_name       12000 non-null  str   ----------> string
#  3   city                  12000 non-null  str   ----------> Categorial
#  4   order_amount          12000 non-null  float64 --------> Numerical : continous
#  5   delivery_time         12000 non-null  int64   --------> Numerical : discrete
#  6   rating                12000 non-null  float64 --------> Numerical : discrete
#  7   payment_method        12000 non-null  str     --------> Categorial
#  8   order_date            12000 non-null  str     --------> Date Time
#  9   delivery_partner_age  12000 non-null  int64   --------> Numerical : discrete
#  10  distance_km           12000 non-null  float64 --------> Numerical : discrete


# dataColumns = """
#    Column                Non-Null Count  Dtype
#  ---  ------                --------------  -----
#   0   order_id              12000 non-null  int64 ----------> Numerical : continous
#   1   customer_id           12000 non-null  int64 ----------> Numerical : continous
#   2   restaurant_name       12000 non-null  str   ----------> string
#   3   city                  12000 non-null  str   ----------> Categorial
#   4   order_amount          12000 non-null  float64 --------> Numerical : continous
#   5   delivery_time         12000 non-null  int64   --------> Numerical : discrete
#   6   rating                12000 non-null  float64 --------> Numerical : discrete
#   7   payment_method        12000 non-null  str     --------> Categorial
#   8   order_date            12000 non-null  str     --------> Date Time
#   9   delivery_partner_age  12000 non-null  int64   --------> Numerical : discrete
#   10  distance_km           12000 non-null  float64 --------> Numerical : discrete
# """

# print(dataColumns)

# step 2 : Remove Duplicate Values
foodDelivery.drop_duplicates(ignore_index=True, inplace=True)

# print(foodDelivery.info())

# step 3 : cleaning numerical : continous data
# 0   order_id              12000 non-null  int64 ----------> Numerical : continous
# 1   customer_id           12000 non-null  int64 ----------> Numerical : continous
# 4   order_amount          12000 non-null  float64 --------> Numerical : continous

# 1. order_id valid range : order_id > 0

foodDelivery = foodDelivery.loc[foodDelivery["order_id"] > 0]

foodDelivery["order_id"].drop_duplicates(ignore_index=True, inplace=True)
# print(foodDelivery.info())

# 2. customer_id valid range : customer_id > 0
foodDelivery = foodDelivery.loc[foodDelivery["customer_id"] > 0]
foodDelivery["customer_id"].drop_duplicates(ignore_index=True, inplace=True)
# print(foodDelivery.info())

# 3. order_amount valid range : order_amount > 0
foodDelivery["order_amount"].loc[foodDelivery["order_amount"] < 0] = np.nan
print(foodDelivery.info())


# step 4 : cleaning numerical : discrete data
#   5   delivery_time         12000 non-null  int64   --------> Numerical : discrete
#   6   rating                12000 non-null  float64 --------> Numerical : discrete
#   9   delivery_partner_age  12000 non-null  int64   --------> Numerical : discrete
#   10  distance_km           12000 non-null  float64 --------> Numerical : discrete

# 1. delivery_time valid range : 5 ≤ delivery_time ≤ 120
foodDelivery["delivery_time"].loc[
    (foodDelivery["delivery_time"] < 5) | (foodDelivery["delivery_time"] > 120)
] = np.nan

# 2. rating valid range : 1 ≤ rating ≤ 5

foodDelivery["rating"].loc[
    (foodDelivery["rating"] < 1) | (foodDelivery["rating"] > 5)
] = np.nan

# 3. delivery_partner_age valid range : 18 ≤ delivery_partner_age ≤ 60
foodDelivery["delivery_partner_age"].loc[
    (foodDelivery["delivery_partner_age"] < 18)
    | (foodDelivery["delivery_partner_age"] > 60)
] = np.nan

# 4 distance_km valid range : 0 < distance_km ≤ 50
foodDelivery["distance_km"].loc[
    (foodDelivery["distance_km"] < 0) | (foodDelivery["distance_km"] > 50)
] = np.nan

# step 5: cleaning categorial data
#   3   city                  12000 non-null  str   ----------> Categorial
#   7   payment_method        12000 non-null  str     --------> Categorial

# 1. city valid range : delhi,mumbai,bangalore,hyderabad,chennai,kolkata,pune
allowedCity = [
    "delhi",
    "mumbai",
    "bangalore",
    "hyderabad",
    "chennai",
    "kolkata",
    "pune",
]
foodDelivery["city"] = foodDelivery["city"].str.strip().str.lower()
foodDelivery = foodDelivery.loc[foodDelivery["city"].isin(allowedCity)]
# print(foodDelivery.info())

# 2. payment_method valid range : cash,upi,card

allowedPayment = ["cash", "upi", "card"]
foodDelivery['payment_method'] = foodDelivery['payment_method'].str.strip().str.lower()
foodDelivery = foodDelivery.loc[foodDelivery['payment_method'].isin(allowedPayment)]
# print(foodDelivery.info())

# step 6 : fixing date and time
#   8   order_date            12000 non-null  str     --------> Date Time
foodDelivery['order_date'] = pd.to_datetime(foodDelivery['order_date'])
# print(foodDelivery.info())

# step 7 : cleaning string data
#   2   restaurant_name       12000 non-null  str   ----------> string

foodDelivery['restaurant_name'] = foodDelivery['restaurant_name'].str.strip().str.lower()
print(foodDelivery.info())

# step 8 : Descriptive Statistics
# For these columns:

# * order_amount
# * delivery_time
# * rating
# * distance_km



