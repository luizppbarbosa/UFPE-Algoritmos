import matplotlib.pyplot as plt


def buscabinaria(chaves, pontos):
    cont = 0
    inicio = 0
    fim = len(chaves) - 1
    while inicio <= fim:
        meio = int((fim + inicio) / 2)
        cont += 1
        if chaves[meio] > pontos:
            fim = meio - 1
            
        elif chaves[meio] < pontos:
            inicio = meio + 1
        else:
            return cont
    return cont

def buscalinear(chaves):
    return len(chaves)

lista = []
linear = []
binaria = []

for n in range (10,101):
    for i in range (1,n):
        lista.append(i**2 + i + 10)
    
    linear.append(buscalinear(lista))
    binaria.append(buscabinaria(lista, lista[len(lista) - 1]))

print(linear)
print(binaria)