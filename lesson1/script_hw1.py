import pandas as pd
import numpy as np

data = pd.read_csv('car_fuel_efficiency_2026.csv')

#print(data.head())

#print(data.fuel_type.describe())
#print(data.isnull().sum())

#df2 = data[data['origin'] == 'Asia']
#print(df2.fuel_efficiency_mpg.describe())

#print(data.horsepower.describe())

#hp_median = data.horsepower.median()
#print("Old median:", hp_median)
#hp_mode = data.horsepower.mode()[0]
#print(hp_mode.shape)

#data['horsepower'] = data['horsepower'].fillna(hp_mode)

#new_median = data.horsepower.median()
#print("New median:", new_median)

#print(data.isnull().sum())

df2 = data[data['origin'] == 'Asia']
print(df2.head())

df3 = df2[['vehicle_weight', 'model_year']]
X = np.array(df3.head(7))
print(type(X))

XTX = X.T.dot(X)
inverse_XTX = np.linalg.inv(XTX)

y = [1100, 1300, 800, 900, 1000, 1100, 1200]

w = inverse_XTX.dot(X.T).dot(y)
sum_w = w[0] + w[1]
print("w sum = ", sum_w)