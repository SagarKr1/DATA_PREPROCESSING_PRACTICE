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

# foodDelivery["order_id"].drop_duplicates(ignore_index=True, inplace=True)
# print(foodDelivery.info())

# 2. customer_id valid range : customer_id > 0
foodDelivery = foodDelivery.loc[foodDelivery["customer_id"] > 0]
# foodDelivery["customer_id"].drop_duplicates(ignore_index=True, inplace=True)
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
foodDelivery["payment_method"] = foodDelivery["payment_method"].str.strip().str.lower()
foodDelivery = foodDelivery.loc[foodDelivery["payment_method"].isin(allowedPayment)]
# print(foodDelivery.info())

# step 6 : fixing date and time
#   8   order_date            12000 non-null  str     --------> Date Time
foodDelivery["order_date"] = pd.to_datetime(foodDelivery["order_date"])
# print(foodDelivery.info())

# step 7 : cleaning string data
#   2   restaurant_name       12000 non-null  str   ----------> string

foodDelivery["restaurant_name"] = (
    foodDelivery["restaurant_name"].str.strip().str.lower()
)
print(foodDelivery.info())

# step 8 : Descriptive Statistics
# For these columns:

# * order_amount
# * delivery_time
# * rating
# * distance_km

orderStats = foodDelivery["order_amount"].describe()
orderIQR = orderStats["75%"] - orderStats["25%"]
print(f"{orderStats}\n{orderIQR}\n")

timeStats = foodDelivery["delivery_time"].describe()
timeIQR = timeStats["75%"] - timeStats["25%"]
print(f"{timeStats}\n{timeIQR}\n")

ratingStats = foodDelivery["rating"].describe()
ratingIQR = ratingStats["75%"] - ratingStats["25%"]
print(f"{ratingStats}\n{ratingIQR}\n")

kmStats = foodDelivery["distance_km"].describe()
kmIQR = kmStats["75%"] - kmStats["25%"]
print(f"{kmStats}\n{kmIQR}")

# step 9 : Outlier Detection

# Using **IQR Method**, detect outliers in:
# * order_amount
# * delivery_time
# * distance_km
# Decide whether to remove or keep.

# 1. order amount
foodDelivery = foodDelivery.loc[
    (foodDelivery["order_amount"] > (orderStats["25%"] - (1.5 * orderIQR)))
    & (foodDelivery["order_amount"] < (orderStats["75%"] + (1.5 * orderIQR)))
]
foodDelivery.reset_index(drop=True,inplace=True)
# print(foodDelivery.info())

# 2. delivery time
timeStats = foodDelivery["delivery_time"].describe()
timeIQR = timeStats["75%"] - timeStats["25%"]
# print(f"{timeStats}\n{timeIQR}\n")
foodDelivery = foodDelivery.loc[
    (foodDelivery["delivery_time"] > (timeStats["25%"] - (1.5 * timeIQR)))
    & (foodDelivery["delivery_time"] < (timeStats["75%"] + (1.5 * timeIQR)))
]
foodDelivery.reset_index(drop=True,inplace=True)
# print(foodDelivery.info())

# 3. distance km
kmStats = foodDelivery["distance_km"].describe()
kmIQR = kmStats["75%"] - kmStats["25%"]
# print(f"{kmStats}\n{kmIQR}")
foodDelivery = foodDelivery.loc[
    (foodDelivery["distance_km"] > (kmStats["25%"] - (1.5 * kmIQR)))
    & (foodDelivery["distance_km"] < (kmStats["75%"] + (1.5 * kmIQR)))
]
foodDelivery.reset_index(drop=True,inplace=True)
# print(foodDelivery.info())

# step 10 : Exploratory Data Analysis (EDA)

# 1. Which **city has the highest number of orders**
cityOrder = foodDelivery['city'].value_counts()
print(f"\nTotal city order : {cityOrder}\n highest order in city : {cityOrder.max()}\n\n")
# 2. Which **restaurant generates highest revenue**
restaurantRevenue = foodDelivery.groupby('restaurant_name')['order_amount'].sum()
print(f"\nHighest revenue generated by restaurants  : {restaurantRevenue}\n highest order in city : {restaurantRevenue.max()}\n\n")

# 3. Average **delivery time per city**
averageCityDelivery = foodDelivery.groupby('city')['delivery_time'].mean()
print(f"\nAverage delivery time  : {averageCityDelivery}\n average highest delivery time : {averageCityDelivery.max()}\n\n")

# 4. Monthly **order trend**
foodDelivery['month'] = foodDelivery['order_date'].dt.month
monthlyOrder = foodDelivery['month'].value_counts()
print(f"\nMonthly Order Trend  : {monthlyOrder}\n  highest monthly trend : {monthlyOrder.max()}\n\n")

# 5. Most used **payment method**
paymentMethod = foodDelivery['payment_method'].value_counts()
print(f"\nUsed Payment Method  : {paymentMethod}\n  highest payment method used : {paymentMethod.max()}\n\n")

# 6. Relationship between **distance and delivery_time**
distance_time = foodDelivery.groupby("distance_km")["delivery_time"].mean()
print(f"\nRelaction between distance and time : {distance_time}\n  highest : {distance_time.max()}\n\n")

# 7. Average **rating per restaurant**
rating = foodDelivery.groupby('restaurant_name')['rating'].mean()
print(f"\nAverage rating  : {rating}\n average highest rating : {rating.max()}\n\n")

