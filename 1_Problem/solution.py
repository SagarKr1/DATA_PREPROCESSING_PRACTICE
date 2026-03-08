# This is the solution to the question provided in the README.md file.

import pandas as pd
import numpy as np

empdata = pd.read_csv(
    "E:/Practice_IHFC/DATA_PREPROCESSING_PRACTICE/1_Problem/dataset.csv"
)
# use this when on same working directry
# empdata = pd.read_csv('dataset.csv')


print(f"1. See only few Data : \n{empdata.head()}\n")
print(
    f"Step 1. Identify the type of data for each column (Numerical , Categorical, Ordinal and PureString)\n"
)
print(f"{empdata.info()}\n\n")
print(
    """
      <class 'pandas.DataFrame'>
RangeIndex: 5000 entries, 0 to 4999
Data columns (total 9 columns):
 #   Column      Non-Null Count  Dtype
---  ------      --------------  -----
 0   emp_id      5000 non-null   int64 -----> Numerical : continous
 1   name        5000 non-null   str   -----> Pure String
 2   age         5000 non-null   int64 -----> Numerical : continous
 3   gender      5000 non-null   str   -----> Categorical : (Male , Female)
 4   department  5000 non-null   str   -----> Categorical 
 5   salary      5000 non-null   int64 -----> Numerical : continous
 6   experience  5000 non-null   int64 -----> Numerical : continous
 7   city        5000 non-null   str   -----> Categorical
 8   join_date   5000 non-null   str   -----> Date and Time
dtypes: int64(4), str(5)
memory usage: 351.7 KB
      """
)

print(f"Step 2 : Check and remove all Duplicate Records from the dataframe\n")
empdata.drop_duplicates(subset="emp_id",ignore_index=True, inplace=True)
print(f"All Duplicate Value Removed : \n {empdata}\n")

print(
    f"step 3: Check and remove all Duplicate Columns from the dataframe \n But there is no duplicate Columns\n"
)

print(
    f"""Step 4 : If your column is Numerical column, perform the following:

               - If dealing with Continuous ND, check w.r.t domain whether the following parameter is valid or not
                       a. Positive Numbers are allowed or not
                       b. Negative Numbers are allowed or not
                       c. Decimals are allowed or not

                 If any of the above is not allowed, DELETE THAT COLUMN ENTRY

               - If dealing with Discrete ND, check w.r.t domain whether the following parameter is valid or not
                       a. Positive Numbers are allowed or not
                       b. Negative Numbers are allowed or not
                       c. Decimals are allowed or not
                       d. Check whether the numbers fall in a specified range as defined by the domain.

                 If any of the above is not allowed, DELETE THAT COLUMN ENTRY
                 
                 0   emp_id      5000 non-null   int64 -----> Numerical : continous
                 2   age         5000 non-null   int64 -----> Numerical : continous
                 5   salary      5000 non-null   int64 -----> Numerical : continous
                 6   experience  5000 non-null   int64 -----> Numerical : continous
"""
)

print(f"1. Employees must be: 18 ≤ age ≤ 60\n")
# empdata[(empdata["age"]>=18) & (empdata['age']<=60)]
empdata = empdata.loc[(empdata["age"] >= 18) & (empdata["age"] <= 60)]
empdata.reset_index(inplace=True)
print(f"empdata after age filter : \n{empdata.info()}\n")

print(f"2. Salary must be: salary > 0\n")
empdata = empdata.loc[empdata["salary"] > 0]
empdata.reset_index(drop=True,inplace=True)

print(f"Data after salary filter : \n {empdata.info()}\n")

print("3. Experience must be: experience ≥ 0\n")
empdata = empdata.loc[empdata["experience"] >= 0]
# empdata.reset_index(inplace=True) # getting error raise ValueError(f"cannot insert {column}, already exists")
empdata.drop_duplicates(ignore_index=True, inplace=True)

print(f"Data after experience filter : \n{empdata.info()}\n")

print(
    """
      Step 5 : 5. If the columns are Categorical columns, perform the following

       a. Get the unique values of the column
       b. Handle the data that has SPELLING ERRORS, CASE ERRORS (Normalization), or any FORMATTING ERRORS. Ensure CASE is UNIFIED
       c. Check whether the categories/groups found in the unique values match the domain spec.

    If any unusual category found, DELETE THAT SPECIFIC RECORD.
    
    3   gender      5000 non-null   str   -----> Categorical : (Male , Female)
    4   department  5000 non-null   str   -----> Categorical 
    7   city        5000 non-null   str   -----> Categorical
      """
)

print("1. Gender (Valid Categories) : Male, Female\n")
allowedGender = ["male","female"]

empdata['gender']=empdata['gender'].apply(str.lower)
empdata = empdata.loc[empdata['gender'].isin(allowedGender)]
empdata.reset_index(drop=True,inplace=True) # getting error 
# empdata.drop_duplicates(ignore_index=True, inplace=True)

print(f"Gener Filter : \n {empdata.info()}\n")

print(f"2. Department (Valid Categories) : IT, HR, Finance, Sales, Marketing")

allowedDep = ['it', 'hr', 'finance', 'sales', 'marketing']
empdata['department'] = empdata['department'].apply(str.lower)

empdata = empdata.loc[empdata['department'].isin(allowedDep)]
empdata.reset_index(drop=True,inplace=True) # getting error 
# empdata.drop_duplicates(ignore_index=True, inplace=True)

print(f"department Cleaning : \n {empdata.info()}")

print('3. City (Valid Categories) : Delhi, Mumbai, Chennai, Bangalore, Kolkata')
allowedCity = ['delhi', 'mumbai', 'chennai', 'bangalore', 'kolkata']

empdata['city'] = empdata['city'].apply(str.lower)

empdata = empdata.loc[empdata['city'].isin(allowedCity)]
empdata.reset_index(drop=True,inplace=True) # getting error 
# empdata.drop_duplicates(ignore_index=True, inplace=True)


print(f"City cleaning : \n {empdata.info()}\n")

print('4. Into proper datetime format')

empdata['join_date'] = pd.to_datetime(empdata['join_date'])

print(empdata)



analysisData = {
    "AverageSalary":{
        
    },
    "Exprience":{
        
    },
    "Cities":{
        
    }
}

# Average salary per department
# Average experience per department
for dep in allowedDep:
    avSal = empdata.loc[empdata['department']==dep]
    analysisData['AverageSalary'][dep] = round(np.mean(avSal['salary']),2)
    analysisData['Exprience'][dep] = round(np.mean(avSal['experience']),2)
    # print(dep)

# Number of employees per city
for city in allowedCity:
    emp = empdata.loc[empdata['city']==city]
    analysisData['Cities'][city] = len(emp)
    # print(city)

# print(analysisData)
# Top 3 highest paying departments
sorted_averageSalary = sorted(analysisData['AverageSalary'].items(), key=lambda item: item[1],reverse=True)
analysisData = pd.DataFrame(analysisData)
print(f"Analysis Report Data : \n{analysisData}\n")
print(f"Average Salary according to highest to lowest Value : \n{sorted_averageSalary}")
