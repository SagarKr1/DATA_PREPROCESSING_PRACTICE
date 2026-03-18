import pandas as pd
import numpy as np
import seaborn as sns
from scipy import stats
import matplotlib.pyplot as plt

df = pd.read_csv("dataset.csv")
# print(df.info(),end="\n\n")

# step 1: identify types of data columns
typeCol = """
#   Column                     Non-Null Count  Dtype  
---  ------                     --------------  -----  
 0   customer_id                10000 non-null  int64     -------------> Numberical Continous
 1   age                        9500 non-null   float64   -------------> Numberical Discrete (18 - 70)
 2   monthly_income             9500 non-null   float64   -------------> Numberical Continous (salary >0)
 3   spending_score             9500 non-null   float64   -------------> Numberical discrete (1 - 100)
 4   city_tier                  10000 non-null  str       -------------> Ordinal
 5   owns_car                   10000 non-null  int64     -------------> Ordinal
 6   online_purchase_per_month  10000 non-null  int64     -------------> Numberical Continous
"""

print(typeCol)

# step 2 : remove duplicate rows

df.drop_duplicates(ignore_index=True, inplace=True)
# print(df.info(),end="\n\n")

# step 3 : Numerical Data columns cleaning
# 0   customer_id                10000 non-null  int64     -------------> Numberical Continous
# 1   age                        9500 non-null   float64   -------------> Numberical Discrete (18 - 70)
# 2   monthly_income             9500 non-null   float64   -------------> Numberical Continous (salary >0)
# 3   spending_score             9500 non-null   float64   -------------> Numberical discrete (1 - 100)
# 6   online_purchase_per_month  10000 non-null  int64     -------------> Numberical Continous (pur>0)


# customer_id : unique values only
checkNull = df["customer_id"].isnull().sum()
print(checkNull)

# df["customer_id"] = df["customer_id"].unique()
# df.reset_index(drop=True, inplace=True)
# print(df.info(),end="\n\n")

# age : (18 - 70) if missing value fill it with median
df.loc[(df["age"] <= 17) | (df["age"] >= 71),"age"] = np.nan
checkNull = df["age"].isna().sum()
print(checkNull)
ageMed = round(df["age"].median())
print(ageMed)
df["age"] = df["age"].fillna(ageMed)
# print(df.info(),end="\n\n")

# monthly_income : (salary >0) if missing value replace it with mean value
df.loc[df["monthly_income"] < 0,"monthly_income"] = np.nan
checkNull = df["monthly_income"].isna().sum()
print(checkNull)
salaryMean = df["monthly_income"].mean()
df["monthly_income"] = df["monthly_income"].fillna(salaryMean)
# print(df.info(),end="\n\n")


# online_purchase_per_month : (pur>0)
df.loc[df["online_purchase_per_month"] < 0,"online_purchase_per_month"] = np.nan
checkNull = df["online_purchase_per_month"].isna().sum()
print(checkNull)
# Null = 0
purMean = round(df["online_purchase_per_month"].mean())
print(purMean)
df["online_purchase_per_month"] = df["online_purchase_per_month"].fillna(purMean)
# print(df.info(),end="\n\n")

# spending_score : (1 - 100)
df.loc[(df["spending_score"] < 0) | (df["spending_score"] > 100),"spending_score"] = np.nan
checkNull = df["spending_score"].isna().sum()
print(checkNull)
spendingMedian = round(df["spending_score"].median())
print(spendingMedian)
df["spending_score"] = df["spending_score"].fillna(spendingMedian)
# print(df.info(), end="\n\n")


# step 4 : cleaning ordinal data columns
#  4   city_tier                  10000 non-null  str       -------------> Ordinal
#  5   owns_car                   10000 non-null  int64     -------------> Ordinal

# city_tier : (Tier1 → Metro Cities,Tier2 → Developing Cities,Tier3 → Small Cities)
allowedCityTiers = ["tier1", "tier2", "tier3"]
df["city_tier"] = df["city_tier"].str.strip().str.lower()
# cityTierMode = df["city_tier"].mode()[0]
# print(cityTierMode)
df = df.loc[df["city_tier"].isin(allowedCityTiers)]
df.reset_index(drop=True, inplace=True)
# print(df.head())
# print(df.info(), end="\n\n")

# owns_car : ( 0 → Does NOT own car, 1 → Owns car)
allowedCar = [0, 1]
df = df.loc[df["owns_car"].isin(allowedCar)]
# print(df.info(), end="\n\n")

# step 5 : Exploratory Data Analysis (EDA)
# 1. Displot
# monthly_income
# sns.displot(data=df["monthly_income"],kind="kde")
# plt.show()
# # normal distribution or bell curve

# # spending_score
# sns.displot(data=df["spending_score"],kind="kde")
# plt.show()
# # normal distribution or bell curve

# # age
# sns.displot(data=df['age'],kind="kde")
# plt.show()
# # normal distribution or bell curve

# 2. Box Plot
# owns_car and monthly_income
# sns.boxplot(data=df,x="owns_car",y="monthly_income")
# plt.show()

# # city_tier and monthly_income
# sns.boxplot(data=df,x='city_tier',y="monthly_income")
# plt.show()

# 3 scatter plot
# sns.scatterplot(data=df,x="age",y="monthly_income")
# plt.show()
# # random distribution

# sns.scatterplot(data=df,x="spending_score",y="monthly_income")
# plt.show()
# # random distribution

# sns.scatterplot(
#     x='spending_score',
#     y='monthly_income',
#     data=df[df['monthly_income'] < 100000]
# )
# plt.show()


# step 6 : Outlier Detection
# monthly_income
# salStats = df["monthly_income"].describe()
# print(salStats)

# salIQR = salStats["75%"] - salStats["25%"]
# lbSal = salStats["25%"] - 1.5 * salIQR
# upSal = salStats["75%"] + 1.5 * salIQR

# # remove outliers
# df = df.loc[(df["monthly_income"] >= lbSal) & (df["monthly_income"] <= upSal)]
# df.reset_index(drop=True, inplace=True)

# we will use Z-Score method to detect outlier because disploat is a normal graph
df["salZ"] = stats.zscore(df["monthly_income"])
df = df.loc[(df["salZ"] >= -3) & (df["salZ"] <= 3)]

# print(df.info(), end="\n\n")

# step 7 : Correlation Test using Hypothesis Testing Method
# check co-relation

SL = 0.05
corr, pvalue = stats.pearsonr(df["age"], df["monthly_income"])
if pvalue <= SL:
    print("Alt Hypothesis (ha) ----> age and monthly income has linear relationship")
else:
    print("Null Hypothesis (H0) ---> age and monthly income has NO linear relationship")

if corr >= 0.75:
    print(f"age and monthly income has Strong +ve corr : {corr}")
elif corr >= 0.45:
    print(f"age and monthly income has weak +ve corr : {corr}")
elif corr < 0.45 or corr < -0.45:
    print(f"age and monthly income has no corr : {corr}")
elif corr <= -0.75:
    print(f"age and monthly income has Strong -ve corr : {corr}")
elif corr <= -0.45:
    print(f"age and monthly income has weak -ve corr : {corr}")



corr, pvalue = stats.pearsonr(df["spending_score"], df["monthly_income"])


if pvalue <= SL:
    print("Alt Hypothesis (ha) ----> age and monthly income has linear relationship")
else:
    print("Null Hypothesis (H0) ---> age and monthly income has NO linear relationship")

if corr >= 0.75:
    print(f"age and monthly income has Strong +ve corr : {corr}")
elif corr >= 0.45:
    print(f"age and monthly income has weak +ve corr : {corr}")
elif corr < 0.45 or corr < -0.45:
    print(f"age and monthly income has no corr : {corr}")
elif corr <= -0.75:
    print(f"age and monthly income has Strong -ve corr : {corr}")
elif corr <= -0.45:
    print(f"age and monthly income has weak -ve corr : {corr}")



# print(df.info(), end="\n\n")
