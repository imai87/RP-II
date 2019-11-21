#Aulas da 77 a 78

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

#Pesos das carteiras
weights = np.array([0.5, 0.5])

weights[0]
weights[1]

#Calculo das variancias anuais de cada empresa
PG_var_a = sec_returns['PG'].var() * 250
print(PG_var_a)

BEI_var_a = sec_returns['BEI.DE'].var() * 250
print(BEI_var_a)

#Variância da carteira
pfolio_var = np.dot(weights.T, np.dot(sec_returns.cov() * 250, weights))

#Cálculo do risco diversificável
dr = pfolio_var - (weights[0] ** 2 * PG_var_a) - (weights[1] ** 2 * BEI_var_a)
print(dr)

#Forma legível de representar
print(str(round(dr*100, 3)) + ' %')

#Cálculo do risco sistemático
n_dr_1 = pfolio_var - dr
print(n_dr_1)

n_dr_2 = (weights[0] ** 2 * PG_var_a) + (weights[1] ** 2 * BEI_var_a)
print(n_dr_2)

print(n_dr_1 == n_dr_2)