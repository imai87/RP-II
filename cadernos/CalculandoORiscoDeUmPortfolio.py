#Aulas da 75 a 76

import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt

#Portfolio com as empresas PG e BEI.DE

tickers = ['PG', 'BEI.DE']

sec_data = pd.DataFrame()

for t in tickers:
    sec_data[t] = wb.get_data_yahoo(t, start='2007-1-1')['Adj Close']

#Retorno logarítmo das empresas PG e BEI.DE
sec_returns = np.log(sec_data / sec_data.shift(1))

weights = np.array([0.5, 0.5])

#Variância da carteira
pfolio_var = np.dot(weights.T, np.dot(sec_returns.cov() * 250, weights))
print(pfolio_var)

#Volatilidade da carteira
pfolio_vol = (np.dot(weights.T, np.dot(sec_returns.cov() * 250, weights))) ** 0.5
print(pfolio_vol)

#Representação mais legível da volatilidade da carteira
print(str(round(pfolio_vol, 5) * 100) + ' %')
