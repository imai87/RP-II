#Aulas da 65 a 66

import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt

#Carrega os dados do Yahoo Finance
tickers = ['PG', 'MSFT', 'F', 'GE']
mydata = pd.DataFrame()
for t in tickers:
    mydata[t] = wb.get_data_yahoo(t, start="1995-1-1")['Adj Close']

print(mydata.info())
print(mydata.head())
print(mydata.tail())

#Extraindo os dados da primeira coluna da tabela
print(mydata.iloc[0])

#Normalizando os cálculos na base 100
(mydata / mydata.iloc[0] * 100).plot(figsize=(15, 6));
plt.show()

#Gráfico não normalizado
mydata.plot(figsize=(15,6))
plt.show()

mydata.loc['1995-01-03']
mydata.iloc[0]

#Calculando o retorno simples do portfolio
returns = (mydata / mydata.shift(1)) - 1
print(returns.head())

#Distribuição de pesos de investimento nas ações
weights = np.array([0.25, 0.25, 0.25, 0.25])
#Calculando o produto pelo peso de cada ação
print(np.dot(returns, weights))

#Retornos anuais médios
annual_returns = returns.mean() * 250
print(annual_returns)

#Calculando o produto pelo peso de cada ação
print(np.dot(annual_returns, weights))

#Representação mais visível do valor
pfolio_1 = str(round(np.dot(annual_returns, weights), 5) * 100) + ' %'
print(pfolio_1)

#Comparando o desempenho com outra distribuição de pesos investidos na carteira
weights_2 = np.array([0.4, 0.4, 0.15, 0.05])
pfolio_2 = str(round(np.dot(annual_returns, weights_2), 5) * 100) + ' %'
print(pfolio_1)
print(pfolio_2)