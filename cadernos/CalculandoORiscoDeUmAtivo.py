#Aulas da 69 a 74

import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt

tickers = ['PG', 'BEI.DE']

sec_data = pd.DataFrame()

for t in tickers:
    sec_data[t] = wb.get_data_yahoo(t, start='2007-1-1')['Adj Close']

print(sec_data.tail())

#Retorno logarítmo das empresas PG e BEI.DE
sec_returns = np.log(sec_data / sec_data.shift(1))

print(sec_returns)
#PG
#Cálculo de retorno médio diário e anual
print(sec_returns['PG'].mean())
print(sec_returns['PG'].mean() * 250)

#Cálculo do desvio padrão diário e anual
print(sec_returns['PG'].std())
print(sec_returns['PG'].std() * 250 ** 0.5)

#BEI.DE
#Cálculo de retorno médio diário e anual
print(sec_returns['BEI.DE'].mean())
print(sec_returns['BEI.DE'].mean() * 250)

#Cálculo do desvio padrão diário e anual
print(sec_returns['BEI.DE'].std())
print(sec_returns['BEI.DE'].std() * 250 ** 0.5)

#Apresentando os cálculos simultâneamente das duas empresas
print(sec_returns[['PG', 'BEI.DE']].mean() * 250)
print(sec_returns[['PG', 'BEI.DE']].std() * 250 ** 0.5)

#Calculando a variância, covariância e correlação entre as duas empresas PG e BEI.DE
#Variância
#Diária
PG_var = sec_returns['PG'].var()
print(PG_var)

BEI_var = sec_returns['BEI.DE'].var()
print(BEI_var)

#Anual
PG_var = sec_returns['PG'].var() * 250
print(PG_var)

BEI_var = sec_returns['BEI.DE'].var() * 250
print(BEI_var)

#Covariância
#Diária
cov_matrix = sec_returns.cov()
print(cov_matrix)

#Anual
cov_matrix_a = sec_returns.cov() * 250
print(cov_matrix_a)

#Correlação
corr_matrix = sec_returns.corr()
print(corr_matrix)