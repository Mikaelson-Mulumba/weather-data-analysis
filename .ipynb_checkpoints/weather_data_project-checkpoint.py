import pandas as pd


data = pd.read_csv('Weather_Data.csv')
"""
Before analysis, one must first explore all the data using the following commands
to know more about the data you are about to analyse

-head()
-shape()
-index()
-ndim()
-columns()
-dtypes
-unique
-nunique
-count
"""
# Exploring our data set
print(data.head())
print(data.shape)
print(data.ndim)
print(data.columns)
print(data.index)
print(data.dtypes)
print(data['weather'].unique())
print(data['weather'].nunique())
print(data.count())








