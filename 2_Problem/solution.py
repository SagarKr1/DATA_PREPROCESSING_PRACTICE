import pandas as pd
import numpy as np

# step 1 : Dataset import
superStore = pd.read_csv("SampleSuperstore.csv", encoding="latin1")

print(
    f"Show top 5 data : \n{superStore.head()}\n show last 5 data : \n {superStore.tail()}\n"
)

# step 2 : Identifing data columns

print(f"\nSample Data info : {superStore.info()}\n")

dataType = """  
    #   Column         Non-Null Count  Dtype
---  ------         --------------  -----
 0   Row ID         9994 non-null   int64   --------> Numerical: continous
 1   Order ID       9994 non-null   str     --------> string
 2   Order Date     9994 non-null   str     --------> Date 
 3   Ship Date      9994 non-null   str     --------> Date
 4   Ship Mode      9994 non-null   str     --------> Categorial 
 5   Customer ID    9994 non-null   str     --------> string
 6   Customer Name  9994 non-null   str     --------> string
 7   Segment        9994 non-null   str     --------> categorial
 8   Country        9994 non-null   str     --------> categorial
 9   City           9994 non-null   str     --------> categorical
 10  State          9994 non-null   str     --------> categorical
 11  Postal Code    9994 non-null   int64   --------> numerical : discrete
 12  Region         9994 non-null   str     --------> categorial
 13  Product ID     9994 non-null   str     --------> string
 14  Category       9994 non-null   str     --------> categorial
 15  Sub-Category   9994 non-null   str     --------> categorial
 16  Product Name   9994 non-null   str     --------> string
 17  Sales          9994 non-null   float64 --------> numerical : continous
 18  Quantity       9994 non-null   int64   --------> numerical : discrete
 19  Discount       9994 non-null   float64 --------> numerical : discrete
 20  Profit         9994 non-null   float64 --------> numerical : discrete
"""
print(f"Data columns : \n{dataType}\n")
# step 3 : Removing duplicate rows

superStore.drop_duplicates(ignore_index=True, inplace=True)

print(superStore.info())

# step 4 : cleaning data Numerical : continous
# 0   Row ID         9994 non-null   int64   --------> Numerical: continous
# 17  Sales          9994 non-null   float64 --------> numerical : continous

# 1. ROW ID valid range : Row ID > 0

superStore = superStore.loc[superStore["Row ID"] > 0]
# superStore["Row ID"].drop_duplicates( inplace=True, ignore_index=True)
# print(f"removed duplicate row id : \n{superStore.info()}\n")

# 2. Sales valid range : Sales > 0

superStore = superStore.loc[superStore["Sales"] > 0]
# superStore["Sales"].drop_duplicates(keep=False, inplace=True, ignore_index=True)
# print(f"removed duplicate sales: \n{superStore.info()}\n")

# step 5 : cleaning data Numerical : discrete
# 11  Postal Code    9994 non-null   int64   --------> numerical : discrete
# 18  Quantity       9994 non-null   int64   --------> numerical : discrete
#  19  Discount       9994 non-null   float64 --------> numerical : discrete
#  20  Profit         9994 non-null   float64 --------> numerical : discrete

# 1. Postal Code valid range : 10000 ≤ Postal Code ≤ 99999
superStore = superStore.loc[
    (superStore["Postal Code"] >= 10000) & (superStore["Postal Code"] <= 99999)
]
# superStore["Postal Code"].drop_duplicates(keep=False, inplace=True, ignore_index=True)
# print(f"removed duplicate postal code: \n{superStore.info()}\n")

# 2. Quantity valid range : 1 ≤ Quantity ≤ 20
superStore = superStore.loc[
    (superStore["Quantity"] >= 1) & (superStore["Quantity"] <= 20)
]
# superStore["Quantity"].drop_duplicates(keep=False, inplace=True, ignore_index=True)
# print(f"removed duplicate Quantity: \n{superStore.info()}\n")

# 3. Discount valid range : 0 ≤ Discount ≤ 1
superStore = superStore.loc[
    (superStore["Discount"] >= 0) & (superStore["Discount"] <= 1)
]
# superStore["Discount"].drop_duplicates(keep=False, inplace=True, ignore_index=True)
# print(f"removed duplicate Discont: \n{superStore.info()}\n")


# 4. Profit valid range : -10,000 ≤ Profit ≤ 10,000
superStore = superStore.loc[
    (superStore["Profit"] >= -10000) & (superStore["Profit"] <= 10000)
]
# superStore["Profit"].drop_duplicates(keep=False, inplace=True, ignore_index=True)
superStore.reset_index(drop=True, inplace=True)
# print(f"removed duplicate Profit: \n{superStore.info()}\n")


# step 6 : cleaning data Categorial
#  4   Ship Mode      9994 non-null   str     --------> Categorial
#  7   Segment        9994 non-null   str     --------> categorial
#  8   Country        9994 non-null   str     --------> categorial
#  9   City           9994 non-null   str     --------> categorical
#  10  State          9994 non-null   str     --------> categorical
#  12  Region         9994 non-null   str     --------> categorial
#  14  Category       9994 non-null   str     --------> categorial
#  15  Sub-Category   9994 non-null   str     --------> categorial

# 1. Ship Mode valid range : Standard Class,Second Class,First Class,Same Day
allowedShipMode = ["standard class", "second class", "first class", "same day"]
superStore["Ship Mode"] = superStore["Ship Mode"].str.strip().str.lower()
superStore = superStore.loc[superStore["Ship Mode"].isin(allowedShipMode)]

# 2. Segment valid range : Consumer,Corporate,Home Office
allowedSegmant = ["consumer", "corporate", "home office"]
superStore["Segment"] = superStore["Segment"].str.strip().str.lower()
superStore = superStore.loc[superStore["Segment"].isin(allowedSegmant)]

# 3. Country valid range : United States
allowedCountry = ["united states"]
superStore["Country"] = superStore["Country"].str.strip().str.lower()
superStore = superStore.loc[superStore["Country"].isin(allowedCountry)]

# 4. City valid range : New York,Los Angeles,Chicago,Houston,Philadelphia,San Francisco,Seattle,Boston,Dallas,Miami
allowedCity = [
    "new york",
    "los angeles",
    "chicago",
    "houston",
    "phoenix",
    "philadelphia",
    "san antonio",
    "san diego",
    "dallas",
    "san jose",
    "austin",
    "jacksonville",
    "san francisco",
    "seattle",
    "denver",
    "boston",
    "miami",
    "atlanta",
    "detroit",
    "orlando",
    "las vegas",
    "portland",
    "memphis",
    "baltimore",
    "milwaukee",
    "albuquerque",
    "tucson",
    "sacramento",
    "kansas city",
    "oakland",
    "cleveland",
    "tampa",
    "bakersfield",
    "honolulu",
    "anaheim",
    "riverside",
    "lexington",
    "stockton",
    "pittsburgh",
    "cincinnati",
    "anchorage",
    "plano",
    "newark",
    "lincoln",
    "irvine",
    "toledo",
    "durham",
    "fort wayne",
    "st. petersburg",
    "laredo",
    "madison",
    "buffalo",
    "reno",
    "norfolk",
    "chesapeake",
    "garland",
    "fremont",
    "boise",
    "richmond",
    "spokane",
    "des moines",
    "tacoma",
    "santa clarita",
    "birmingham",
    "rochester",
    "salt lake city",
    "grand rapids",
    "huntsville",
    "augusta",
    "tallahassee",
    "knoxville",
    "worcester",
    "vancouver",
    "fort lauderdale",
    "ontario",
    "chattanooga",
    "providence",
    "salem",
    "eugene",
    "springfield",
    "fort collins",
    "jackson",
    "hayward",
    "lakewood",
    "hollywood",
    "sunnyvale",
    "pomona",
    "naperville",
    "bellevue",
    "savannah",
    "bridgeport",
    "syracuse",
    "midland",
    "dayton",
    "fullerton",
    "orange",
    "thornton",
    "waco",
    "charleston",
    "columbia",
    "new haven",
    "concord",
    "elizabeth",
    "round rock",
    "athens",
    "topeka",
    "fargo",
    "wilmington",
    "hartford",
    "berkeley",
    "allentown",
]
superStore["City"] = superStore["City"].str.strip().str.lower()
superStore = superStore.loc[superStore["City"].isin(allowedCity)]

# 5. State valid range : California,Texas,New York,Washington,Florida,Illinois,Pennsylvania,Ohio,Michigan,North Carolina
allowedState = [
    "alabama",
    "alaska",
    "arizona",
    "arkansas",
    "california",
    "colorado",
    "connecticut",
    "delaware",
    "florida",
    "georgia",
    "hawaii",
    "idaho",
    "illinois",
    "indiana",
    "iowa",
    "kansas",
    "kentucky",
    "louisiana",
    "maine",
    "maryland",
    "massachusetts",
    "michigan",
    "minnesota",
    "mississippi",
    "missouri",
    "montana",
    "nebraska",
    "nevada",
    "new hampshire",
    "new jersey",
    "new mexico",
    "new york",
    "north carolina",
    "north dakota",
    "ohio",
    "oklahoma",
    "oregon",
    "pennsylvania",
    "rhode island",
    "south carolina",
    "south dakota",
    "tennessee",
    "texas",
    "utah",
    "vermont",
    "virginia",
    "washington",
    "west virginia",
    "wisconsin",
    "wyoming",
]
superStore["State"] = superStore["State"].str.strip().str.lower()
superStore = superStore.loc[superStore["State"].isin(allowedState)]

# 6. Region valid range : West,East,Central,South
allowedRegion = ["west", "east", "central", "south"]
superStore["Region"] = superStore["Region"].str.strip().str.lower()
superStore = superStore.loc[superStore["Region"].isin(allowedRegion)]

# 7. Category valid range : Furniture,Office Supplies,Technology
allowedCategory = ["furniture", "office supplies", "technology"]
superStore["Category"] = superStore["Category"].str.strip().str.lower()
superStore = superStore.loc[superStore["Category"].isin(allowedCategory)]

# 8. Sub-Category valid range : Chairs,Tables,Bookcases,Phones,Storage,Binders,Machines,Accessories,Copiers,Appliances,Paper,Furnishings,Art,Envelopes,Labels,Fasteners,Supplies
allowedSbuCategory = [
    "chairs",
    "tables",
    "bookcases",
    "phones",
    "storage",
    "binders",
    "machines",
    "accessories",
    "copiers",
    "appliances",
    "paper",
    "furnishings",
    "art",
    "envelopes",
    "labels",
    "fasteners",
    "supplies",
]
superStore["Sub-Category"] = superStore["Sub-Category"].str.strip().str.lower()
superStore = superStore.loc[superStore["Sub-Category"].isin(allowedSbuCategory)]

superStore.reset_index(drop=True, inplace=True)
# print(superStore.info())

# step 7 : correcting date formate
#  2   Order Date     9994 non-null   str     --------> Date
#  3   Ship Date      9994 non-null   str     --------> Date

# 1. Order Date
superStore["Order Date"] = pd.to_datetime(superStore["Order Date"])

# 2. Ship Date
superStore["Ship Date"] = pd.to_datetime(superStore["Ship Date"])

superStore = superStore[superStore["Ship Date"] >= superStore["Order Date"]]

# print(superStore.head())

# before moving to next part i will reset all indexies
superStore.reset_index(drop=True, inplace=True)

# step 8 : Descriptive Statistics: calculating mean , median , mode , min , max and quartiles(q1,q2,q3,q4)
# Calculate descriptive statistics for the following columns:
# Sales
# Quantity
# Discount
# Profit

# 1. Sales
SalesData = superStore["Sales"].describe()
# print(SalesData)

# 2. Quantity
QuantityData = superStore["Quantity"].describe()
# print(QuantityData)

# 3. Discount
DiscountData = superStore["Discount"].describe()
# print(DiscountData)

# 4. Profit
ProfitData = superStore["Profit"].describe()
# print(ProfitData)

# step 9 : Outlier Detection
# Detect outliers using the **IQR method (1.5 × IQR rule)**.
# Columns to analyze:
# Sales
# Profit
# Discount

salesIQR = SalesData["75%"] - SalesData["25%"]
profitIQR = ProfitData["75%"] - ProfitData["25%"]
discountIQR = DiscountData["75%"] - DiscountData["25%"]

# 1. Sales finding outliers
superStore = superStore.loc[
    (superStore["Sales"] >= (SalesData["25%"] - 1.5 * salesIQR))
    & (superStore["Sales"] <= (SalesData["75%"] + 1.5 * salesIQR))
]
# print(superStore.info())

# 2. Profit finding outliers
ProfitData = superStore["Profit"].describe()
profitIQR = ProfitData["75%"] - ProfitData["25%"]
superStore = superStore.loc[
    (superStore["Profit"] >= (ProfitData["25%"] - 1.5 * profitIQR))
    & (superStore["Profit"] <= (ProfitData["75%"] + 1.5 * profitIQR))
]
# print(superStore.info())

# 3. Discount finding outliers
DiscountData = superStore["Discount"].describe()
discountIQR = DiscountData["75%"] - DiscountData["25%"]
superStore = superStore.loc[
    (superStore["Discount"] >= (DiscountData["25%"] - 1.5 * discountIQR))
    & (superStore["Discount"] <= (DiscountData["75%"] + 1.5 * discountIQR))
]
# print(superStore.info())

superStore.reset_index(drop=True, inplace=True)
print(superStore.info())

# step 10 : Distribution Analysis
# Analyze the distribution of the following variables:
# Sales
# Profit
# Quantity
# Discount

# Create visualizations:
# - Histogram
# - Boxplot
# - KDE Distribution Plot

# currently not introduced by graph  skipping step 10

# step 11 : Exploratory Data Analysis (EDA)

# Answer the following business questions.

# 1. Which **category generates the highest total sales?**
salesCategory = superStore.groupby("Category")["Sales"].sum()
print(
    f"\nTotal sales according to category : \n{salesCategory}\n\n Max sales : {salesCategory.max()}\n"
)

# 2. Which **sub-category generates the highest profit?**
SubCategoryProfit = superStore.groupby("Sub-Category")["Profit"].sum()
print(
    f"\nTotal profit according to sub category : \n{SubCategoryProfit}\n\n Max profit : {SubCategoryProfit.max()}\n"
)

# 3. Which **region generates the highest revenue?**
RegionSales = superStore.groupby("Region")["Sales"].sum()
print(
    f"\nTotal sales according to region : \n{RegionSales}\n\n Max sales : {RegionSales.max()}\n"
)

# 4. Which **city has the most orders?**
CityOrders = superStore["City"].value_counts()
print(
    f"\nTotal orders according to city : \n{CityOrders.head()}\n\n Max orders : {CityOrders.max()}\n"
)

# 5. What is the **monthly sales trend?**
superStore["month"] = superStore["Order Date"].dt.month
monthlySales = superStore.groupby("month")["Sales"].sum()
print(f"\n{monthlySales}\n")

# 6. Which **segment contributes the most profit?**
SegmentProfit = superStore.groupby("Segment")["Profit"].sum()
print(
    f"\nTotal profit according to segment : \n{SegmentProfit}\n\n Max profit : {SegmentProfit.max()}\n"
)

# 7. Which **products have the highest sales?**
ProductSales = superStore.groupby("Sub-Category")["Sales"].sum()
print(
    f"\nTotal sales according to sub category : \n{ProductSales}\n\n Max profit : {ProductSales.max()}\n"
)

# 8. What is the relationship between **discount and profit?**


print(superStore.info())
