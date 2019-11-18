#Aulas da 59 à 64
#Calculando o retorno simples e logarítmo da empresa PG = The Procter & Gamble Company
import yahoo_finance as yf
import numpy as np
from pandas_datareader import data as wb
import matplotlib.pyplot as plt

PG = wb.get_data_yahoo("PG", start="1995-1-1")

print(PG.head())
print(PG.tail())

#Realiza o cálculo de retorno simples
PG['simple_return'] = (PG['Adj Close'] / PG['Adj Close'].shift(1)) - 1
print(PG['simple_return'])

#Exibe o gráfico
PG['simple_return'].plot(figsize=(8, 5))
plt.show()

#Cálculo da média diária de retorno
avg_returns_d = PG['simple_return'].mean()
print(avg_returns_d)

#Cálcudo da média anual de retorno
avg_returns_a = PG['simple_return'].mean() * 250
print(avg_returns_a)

#Esse seria o valor para apresentar na saída de dados
#Cálculo da média anual de retorno melhor apresentável
print(str(round(avg_returns_a, 5) * 100) + ' %')

#Cálculo com o valor logaritmo, observação é usado somente para o cálculo de uma única ação
print(PG.head())

#Realiza o cálculo de retorno simples
PG['log_return'] = np.log(PG['Adj Close'] / PG['Adj Close'].shift(1))
print(PG['log_return'])

#Exibe o gráfico
PG['log_return'].plot(figsize=(8, 5))
plt.show()

#Cálculo diário
log_return_d = PG['log_return'].mean()
print(log_return_d)

#Cálculo anual
log_return_a = PG['log_return'].mean() * 250
print(log_return_a)

#Esse seria o valor para apresentar na saída de dados
print(str(round(log_return_a, 5) * 100) + ' %')
