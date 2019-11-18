#Aulas 67 e 68
"""
^GSPC = S&P500
^IXIC = NASDAQ
^GDAXI = Índice Alemão DAX
^BVSP = Índice do Ibovespa
"""

import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt

tickers = ['^GSPC', '^IXIC', '^GDAXI', '^BVSP']

ind_data = pd.DataFrame()

for t in tickers:
    ind_data[t] = wb.get_data_yahoo(t, start="1997-1-1")['Adj Close']

print(ind_data.head())

print(ind_data.tail())

#Plotando os dados na base 100
(ind_data / ind_data.iloc[0] * 100).plot(figsize=(15, 6));
plt.show()

#Calculando os retornos simples diários dos índices
ind_returns = (ind_data / ind_data.shift(1) - 1)
print(ind_returns.tail())

#Calculando os retornos anuais
annual_ind_returns = ind_returns.mean() * 250
print(annual_ind_returns)

#Comparando o índice de desempenho da empresa PG com os indíces das bolsas ^GSPC e ^DJI
tickers = ['PG', '^GSPC', '^DJI']
data_2 = pd.DataFrame()

for t in tickers:
    data_2[t] = wb.get_data_yahoo(t, start="2007-1-1")['Adj Close']
print(data_2.tail())

#Normalizando os dados na base 100 e gerando os gráficos
(data_2 / data_2.iloc[0] * 100).plot(figsize=(15, 6));
plt.show()

