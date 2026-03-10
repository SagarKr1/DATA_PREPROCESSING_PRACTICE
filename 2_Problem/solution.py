import pandas as pd 
import numpy as np

# step 1 : Dataset import
superStore = pd.read_csv('SampleSuperstore.csv',encoding='latin1')

print(f"Show top 5 data : \n{superStore.head()}\n show last 5 data : \n {superStore.tail()}\n")

# step 2 : Identifing data columns

print(f"\nSample Data info : {superStore.info()}\n")

dataType = '''  
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
'''

# step 3 : Removing duplicate rows      

# superStore.drop_duplicates(ignore_index=True,inplace=True)
