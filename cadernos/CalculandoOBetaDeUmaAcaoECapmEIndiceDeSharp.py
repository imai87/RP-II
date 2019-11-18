#Aulas da 87 à 94

import numpy as np
import pandas as pd
from pandas_datareader import data as wb

tickers = ['PG', '^GSPC']
data = pd.DataFrame()
for t in tickers:
    data[t] = wb.get_data_yahoo(t, start='2012-1-1', end='2016-12-31')['Adj Close']

sec_returns = np.log(data / data.shift(1))

cov = sec_returns.cov() * 250
print(cov)

cov_with_market = cov.iloc[0,1]
print(cov_with_market)

market_var = sec_returns['^GSPC'].var() * 250
print(market_var)

#Calculando o BETA
PG_beta = cov_with_market / market_var
print(PG_beta)

#Calculando o retorno esperado de uma ação CAPM
PG_er = 0.025 + PG_beta * 0.05
print(PG_er)

#Índice de Sharpe
Sharpe = (PG_er - 0.025) / (sec_returns['PG'].std() * 250 ** 0.5)
print(Sharpe)
