#Aula da 105 a 107

import numpy as np
import pandas as pd
from pandas_datareader import data as wb
from scipy.stats import norm

def d1(S, K, r, stdev, T):
    return (np.log(S / K) + (r + stdev ** 2 / 2) * T) / (stdev * np.sqrt(T))

def d2(S, K, r, stdev, T):
    return (np.log(S / K) + (r - stdev ** 2 / 2) * T) / (stdev * np.sqrt(T))

print(norm.cdf(0))
print(norm.cdf(0.25))
print(norm.cdf(0.75))
print(norm.cdf(9))

def BSM(S, K, r, stdev, T):
    return(S * norm.cdf(d1(S, K, r, stdev, T))) - (K * np.exp(-r * T) * norm.cdf(d2(S, K, r, stdev, T)))

ticker = 'PG'
data = pd.DataFrame()
data[ticker] = wb.get_data_yahoo(ticker, start='2007-1-1', end='2017-3-21')['Adj Close']

S = data.iloc[-1]
print(S)

log_returns = np.log(1 + data.pct_change())

stdev = log_returns.std() * 250 ** 0.5
print(stdev)

r = 0.025
K = 110.0
T = 1

print(d1(S, K, r, stdev, T))

print(d2(S, K, r, stdev, T))

print(BSM(S, K, r, stdev, T))
