import pandas as pd

data = pd.read_csv("Iris.csv")
print(data.head())
nulls = data.isnull().sum()
print(nulls)
