import pandas as pd
import numpy as np


df = pd.read_csv('https://raw.githubusercontent.com/alexeygrigorev/mlbookcamp-code/master/chapter-02-car-price/data.csv')

print(df.head())
df.columns = df.columns.str.lower().str.replace(' ', '_')
#print(df.isnull().sum())
#print(df.dtypes)

df.dtypes[df.dtypes == 'string']
strings = list(df.dtypes[df.dtypes == 'string'].index)

for col in strings:
    df[col] = df[col].str.lower().str.replace(' ', '_')

print(df.head())


for col in df.columns:
    print(col)
    print(df[col].unique()[:5])
    print(df[col].nunique())
    print()