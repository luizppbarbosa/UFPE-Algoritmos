"""[Questão 4] Faça um programa para multiplicar duas matrizes com tamanho até 10x10, armazenando o resultado em uma terceira matriz.
- O programa deve solicitar ao usuário as duas dimensões das duas matrizes;
- O programa deve verificar se as matrizes podem ser multiplicadas e apresentar uma mensagem de erro, caso não seja possível."""

import numpy as np

linA = int(input('Qual a quantidade de linhas da matriz A? '))
colA = int(input('Qual a quantidade de colunas da matriz A? '))
matA = np.zeros((linA, colA), int)
for i in range (linA):
    for j in range (colA):
        matA[(i,j)] = int(input(f'Digite o termo da linha {i} e coluna {j}: '))

linB = int(input('Qual a quantidade de linhas da matriz B? '))
colB = int(input('Qual a quantidade de colunas da matriz B? '))
matB = np.zeros((linB, colB), int)
for i in range (linB):
    for j in range (colB):
        matB[(i,j)] = int(input(f'Digite o termo da linha {i} e coluna {j}: '))


if colA != linB:
    print('ERRO! As matrizes não podem ser multiplicadas.\nA quantidade de linhas da matriz A é diferente da quantidade de colunas da matriz B!')
else:
    print('As matrizes podem ser multiplicadas!')
    matC = np.zeros((linA, colB), int)

    for i in range (linA):
        for j in range (colB):
            for k in range (colA):

                matC[(i,j)] = matC[(i,j)] + matA[(i,k)] * matB[(k,j)]

print(matA)
print(matB)
print(matC)