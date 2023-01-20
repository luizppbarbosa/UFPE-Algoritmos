""" Crie um programa que recebe 1 sequencia de inteiros sem repetições, e retorna uma mensagem descrevendo a sequencia como sendo um Heap de máximo, um Heap de minímo ou não sendo um Heap.

A sequencia não possuirá repetições


Input Specification

S[1] S[2] S[3] ... S[x]


Output Specification

Caso seja um Heap de maximo o programa deve retornar "E uma Heap de maximo!"
Caso seja um Heap de maximo o programa deve retornar "E uma Heap de minimo!"
Caso não seja um Heap o programa deve retornar "Nao e uma Heap!" """


def main():

    def parentindex(i):
        numero = i/2
        num = round(numero)
        if numero - num <= 0:
            num -= 1
        return num

    def verifyheap(lista):
        heapmax = False
        heapmin = False
        for i in range (1,len(lista)):
            if lista[parentindex(i)] > lista[i]:
                if i == len(lista) - 1:
                    heapmax = True
                    return heapmax, heapmin
            else:
                break

        for i in range (1,len(lista)):
            if lista[parentindex(i)] < lista[i]:
                if i == len(lista) - 1:
                    heapmin = True
                    return heapmax, heapmin
            else:
                break
        
        return heapmax, heapmin
        


    seq = input()
    seq = seq.strip()

    lista = seq.split(' ')

    for i in range(len(lista)):
        lista[i] = int(lista[i])


    heapmax, heapmin = verifyheap(lista)



    if heapmin:
        print('E uma Heap de minimo!')
    elif heapmax:
        print('E uma Heap de maximo!')
    else:
        print('Nao e uma Heap!')

if __name__ == '__main__':
    main()