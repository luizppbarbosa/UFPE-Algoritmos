"""[Questão 2] Construa um programa que lê o valor das posições de dois vetores de float de 10 posições cada. 
Logo em seguida, calcule a soma dos dois vetores e armazenando-a em outro vetor.
 Por fim, imprima cada um dos valores do vetor soma."""


import numpy as np

v1 = np.empty(10, float)
v2 = np.empty(10, float)
v3 = np.empty(10, float)

for i in range (0,10):
    v1[i] = float(input(f'Digite o termo {i} do primeiro vetor: '))

for i in range (0,10):
    v2[i] = float(input(f'Digite o termo {i} do segundo vetor: '))

for i in range (0,10):
    v3[i] = v1[i] + v2[i]

print(v1)
print(v2)
print(v3)