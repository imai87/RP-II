import numpy as np
import pandas as pd
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt

data = pd.read_excel('C:/Python/Data_Files/Housing.xlsx')

print(data)

X = data[['House Size (sq.ft.)', 'Number of Rooms', 'Year of Construction']]
Y = data['House Price']

X1 = sm.add_constant(X)
reg = sm.OLS(Y, X1).fit()

print(reg.summary())

X = data[['House Size (sq.ft.)', 'Number of Rooms']]
Y = data['House Price']

X1 = sm.add_constant(X)
reg = sm.OLS(Y, X1).fit()

print(reg.summary())

X = data[['House Size (sq.ft.)', 'Year of Construction']]
Y = data['House Price']

X1 = sm.add_constant(X)
reg = sm.OLS(Y, X1).fit()

print(reg.summary())

X = data[['Number of Rooms', 'Year of Construction']]
Y = data['House Price']

X1 = sm.add_constant(X)
reg = sm.OLS(Y, X1).fit()

print(reg.summary())