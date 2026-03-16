# importing required library
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# reading csv file
df = pd.read_csv("dataset.csv")

# Task 1 : Cleaning data according to domain range(pre-processing)

# step 1 : identifying data columns
print(f"info : \n{df.info()}\n\n Top 5 data : \n {df.head()}\n\n")

dataColumns = """ 
#   Column      Non-Null Count  Dtype  
---  ------      --------------  -----  
 0   age         46000 non-null  float64 ------> Numerical : continous (18 → 65 years)
 1   salary      46000 non-null  float64 ------> Numerical : discete (10,000 → 2,00,000)
 2   experience  46000 non-null  float64 ------> Numerical : continous (0 → (Age − 18))
 3   city        46000 non-null  str     ------> categorial (delhi,mumbai,chennai,kolkata,bangalore)
 4   education   46000 non-null  str     ------> categorical (school, graduate, postgraduate)
 5   purchased   50000 non-null  int64   ------> Ordinal (0 → Customer did not purchase, 1 → Customer purchased)
dtypes: float64(3), int64(1), str(2)
"""
print(f"Data columns : \n{dataColumns}\n\n")

# step: 2 : remove duplicate rows
df.drop_duplicates(ignore_index=True, inplace=True)

print(df.info())

# step 3 : Pre-Processing and handling missing Numerical continous columns values

#  0   age         46000 non-null  float64 ------> Numerical : continous  replace with mean
#  2   experience  46000 non-null  float64 ------> Numerical : continous (0 → (Age − 18)), missing value = replace according to age

# age 
# df['age']=df['age'].astype(dtype="Int64")
df['age'].loc[df['age']<0] = np.nan
ageMedian = round(df['age'].mean())
print(f"Age mean : {ageMedian}\n")
# df['age'].fillna(ageMedian,inplace=True) not working in vscode

df['age']=df['age'].fillna(ageMedian)
# print(df.isna().sum())

# experience
df['experience'].loc[df['experience']<0] = np.nan
exprienceMean = round(df['experience'].mean())
print(f"experience mean : {exprienceMean}\n\n")
df['experience']=df['experience'].fillna(exprienceMean)
# print(df[df['experience']==0].head(10))

# step 5 : Pre-Processing and handling missing Numerical discrete columns values 
# #  1   salary      46000 non-null  float64 ------> Numerical : discete (10,000 → 2,00,000), missing value = replace with median
# salary
df['salary'].loc[(df['salary']<10000) | (df['salary']>200000)] = np.nan
salaryMedian = df['salary'].median()
print(f"salary Median : {salaryMedian}\n")
df['salary'] =df['salary'].fillna(salaryMedian)
print(df.info())

# step 6 : pre-processing and handling missing categorical columns values
# 3   city        46000 non-null  str     ------> categorial (delhi,mumbai,chennai,kolkata,bangalore), missing value = replace with mode first value
#  4   education   46000 non-null  str     ------> categorical (school, graduate, postgraduate) ,  missing value = replace with mode first value

# city (delhi,mumbai,chennai,kolkata,bangalore)
allowedCity = ['delhi','mumbai','chennai','kolkata','bangalore']

df['city'] = df['city'].str.strip().str.lower()

# removing all which did not containing allowedCity

df= df.loc[df['city'].isin(allowedCity)]
df.reset_index(inplace=True,drop=True)

cityMode = df['city'].mode()[0]
print(f"city mode value : {cityMode}")
df['city'] = df['city'].fillna(cityMode)


# print(df.info())

# education (school, graduate, postgraduate)
allowedEdu = ['school', 'graduate', 'postgraduate']

df['education'] = df['education'].str.strip().str.lower()

# removing all which did not containing allowedEdu
df = df.loc[df['education'].isin(allowedEdu)]

eduMode = df['education'].mode()[0]
print(f"education mode value : {eduMode}")
df['education'] = df['education'].fillna(eduMode)

# step 7 : pre-processing and handling missing ordinal columns values
# 5   purchased   50000 non-null  int64   ------> Ordinal (0 → Customer did not purchase, 1 → Customer purchased)
 
#  this step is skipped 

# step 8 : dectecting type of displot of numerical data
# 0   age         46000 non-null  float64 ------> Numerical : continous (18 → 65 years)
#  1   salary      46000 non-null  float64 ------> Numerical : discete (10,000 → 2,00,000)

sns.displot(data=df['salary'],kind='kde')
plt.show()
# salary displot is skew
sns.displot(data=df['age'],kind='kde')
plt.show()
# age disploat is skwe

# step 9 : EDA and outliers detection 
# preforming outlier in numerical 
# for skew distribution using tukey method or 1.5*IQR method
# 0   salary         46000 non-null  float64 ------> Numerical : continous (18 → 65 years)
salaryStats = df['salary'].describe()
print(salaryStats)

salaryIQR = salaryStats['75%'] - salaryStats['25%']

lr = salaryStats['25%'] - 1.5*salaryIQR
up = salaryStats['75%'] + 1.5*salaryIQR

df = df.loc[(df['salary']>=lr) & (df['salary']<=up)]
df.reset_index(drop=True,inplace=True)
# print(df.info())

# step 10 : analysis bonus
# salary according to city
citySalary = df.groupby('city')['salary'].sum()
print(citySalary)

# salary according to age
ageSalary = df.groupby('age')['salary'].sum()
print(ageSalary)