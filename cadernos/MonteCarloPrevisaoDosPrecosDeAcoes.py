#Aula 101 a 104

import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt
from scipy.stats import norm

ticker = 'PG'
data = pd.DataFrame()
data[ticker] = wb.get_data_yahoo(ticker, start='2007-1-1')['Adj Close']

log_returns = np.log(1 + data.pct_change())

print(log_returns.tail())

data.plot(figsize=(10, 6))
plt.show()

log_returns.plot(figsize=(10, 6))
plt.show()

u = log_returns.mean()
print(u)

var = log_returns.var()
print(var)

drift = u - (0.5 * var)
print(drift)

stdev = log_returns.std()
print(stdev)

print(type(drift))
print(type(stdev))

np.array(drift)
print(drift.values)
print(stdev.values)
print(norm.ppf(0.95))

x = np.random.rand(10, 2)
print(x)

print(norm.ppf(x))

Z = norm.ppf(np.random.rand(10, 2))
print(Z)

t_intervals = 1000
iterations = 10

daily_returns = np.exp(drift.values + stdev.values * norm.ppf(np.random.rand(t_intervals, iterations)))
print(daily_returns)

S0 = data.iloc[-1]


price_list = np.zeros_like(daily_returns)
print(price_list)

price_list[0] = S0
print(price_list)

for t in range(1, t_intervals):
    price_list[t] = price_list[t - 1] * daily_returns[t]

print(price_list)

plt.figure(figsize=(10, 6))
plt.plot(price_list)
plt.show()