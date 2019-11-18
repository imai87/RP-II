#Aula 97 a 100
import numpy as np
import matplotlib.pyplot as plt

rev_m = 170
rev_stdev = 20
iterations = 1000

rev = np.random.normal(rev_m, rev_stdev, iterations)
print(rev)

plt.figure(figsize=(15, 6))
plt.plot(rev)
plt.show()

COGS = - (rev * np.random.normal(0.6, 0.1))

plt.figure(figsize=(15, 6))
plt.plot(COGS)
plt.show()

print(COGS.mean())

print(COGS.std())

#Calculando o lucro bruto
Gross_Profit = rev + COGS
print(Gross_Profit)

plt.figure(figsize=(15, 6))
plt.plot(Gross_Profit)
plt.show()

print(Gross_Profit.mean())
print(Gross_Profit.std())


print(max(Gross_Profit))
print(min(Gross_Profit))

plt.figure(figsize=(10, 6))
plt.hist(Gross_Profit, bins=[40, 50, 60, 70, 80, 90, 100, 110, 120]);
plt.show()

plt.figure(figsize=(10, 6))
plt.hist(Gross_Profit, bins=20)
plt.show()

