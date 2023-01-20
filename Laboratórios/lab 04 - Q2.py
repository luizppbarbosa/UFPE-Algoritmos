
def leftindex (i):
    return 2*i

def rightindex(i):
    return 2*i + 1

def maxheapify (lista, i, tamanho):
    l = leftindex(i)
    r = rightindex(i)

    if l <= tamanho and lista[l] > lista[i]:
        maior = l
    else:
        maior = i

    if r <= tamanho and lista[r] > lista[maior]:
        maior = r

    if maior != i:
        pos1 = lista[i]
        pos2 = lista[maior]
        lista[i] = pos2
        lista[maior] = pos1

        maxheapify(lista, maior, tamanho)

def criamaxheap (lista,tamanho):
    for i in range(tamanho//2, 0, -1):
        maxheapify(lista, i, tamanho)


lista1 = [3, 10, 40, 1, 60, 34, 21, 100, 5, 31, 2, 4, 6]
lista1 = [None] + lista1
tamanho1 = len(lista1) - 1
lista2 = [100, 90, 80, 70, 60, 50, 40, 30, 20, 11, 1001]
lista2 = [None] + lista2
tamanho2 = len(lista2) - 1
lista3 = [1, 2, 3, 9, 8, 7, 6, 5, 4, 20, 30, 40, 50, 60]
lista3 = [None] + lista3
tamanho3 = len(lista3) - 1

criamaxheap (lista1, tamanho1)
criamaxheap (lista2, tamanho2)
criamaxheap (lista3, tamanho3)

print(lista1[1:])
print(lista2[1:])
print(lista3[1:], '\n')

lista1[1] = lista1[1] // 4
maxheapify(lista1,1,tamanho1)

lista2[1] = lista2[1] // 4
maxheapify(lista2,1,tamanho2)

lista3[1] = lista3[1] // 4
maxheapify(lista3,1,tamanho3)

print(lista1[1:])
print(lista2[1:])
print(lista3[1:])
