#Aulas da 79 a 82

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import statsmodels.api as sm

#Regressão OLS
data = pd.read_excel('C:/Python/Data_files/Housing.xlsx')
print(data)

#Serapando as colunas da base de dados importada

print(data[['House Price', 'House Size (sq.ft.)']])

X = data['House Size (sq.ft.)']
Y = data['House Price']

#Gráfico de dispersão
plt.scatter(X,Y)
plt.show()

plt.scatter(X,Y)
plt.axis([0, 2500, 0, 1500000])
plt.ylabel('House Price')
plt.xlabel('House Size (sq.ft)')
plt.show()

#Calculando Alfa, Beta e R Quadrado
X1 = sm.add_constant(X)
reg = sm.OLS(Y, X1).fit()

print(reg.summary())

#Extraindo estatisticas separadas
slope, intercept, r_value, p_value, std_err = stats.linregress(X,Y)
#inclinação Beta
print(slope)
#Inclinação Alpha
print(intercept)
#Valor de R
print(r_value)
#Valor dr R^2
print(r_value ** 2)
#P Valor
print(p_value)
#Erro padrão
print(std_err)