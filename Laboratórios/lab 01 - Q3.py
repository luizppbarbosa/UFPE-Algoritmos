import numpy as np

"""[Questão 3] Faça um programa que multiplica uma matriz 3 x 3 de inteiros por um escalar k e 
imprima o resultado na tela. O usuário deve fornecer os valores da matriz e de k."""

mat = np.zeros((3,3), int)
matnew = np.zeros((3,3), int)

for i in range (3):
    for j in range (3):
        mat[(i,j)] = int(input(f'Digite o termo da linha {i} e coluna {j}: '))
    
k = int(input('Digite o valor da constante "k" que multiplicará a matriz: '))

for i in range (3):
    for j in range (3):
        matnew[(i,j)] = mat[(i,j)] * k

print(f'A matriz digitada foi: \n{mat}')
print(f'A nova matriz após ser multiplicada pelo escalar {k} é: \n{matnew}')
