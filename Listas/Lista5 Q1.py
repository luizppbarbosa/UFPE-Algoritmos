""" Wes decidiu entrar na trupe do Scooby Doo e uma das fases do processo seletivo era um problema um tanto quanto simples porém com um tom de complexidade... Serão entregue para ele dois baús: um repleto de chaves e outro repleto de cadeados trancados. Cada chave e cada cadeado possuia uma inscrição única, indicando qual chave abre qual cadeado.

A função de Wes é, diversas vezes, organizar de maneira sequencial as chaves e os cadeados de maneira que a i-ésima chave da sequencia de chaves abra o i-ésimo cadeado da sequência de cadeados.

Os baús são entregues de maneira separada - as chaves ficam em uma partição a esquerda e os cadeados em uma partição a direita. Para encontrar a sequência correta, Wes não pode comparar as chaves entre si ou os cadeados entre si. Dessa forma, a decisão de mover ou não uma chave deve ser tomada exclusivamente olhando para os cadeados e vice versa.

Scooby sabe que Wes é compuyteiro e decidiu contradizer a comum (e errada cof cof) opinião de que a disciplina não serve para nada. Assim, ele determinou que Wes deveria utilizar os seus conhecimentos aprendidos na disciplina de Algoritmos e Estrutura de Dados para solucionar o problema e, portanto, que deveria utilizar um método de ordenação que seja um algoritmo de divisão e conquista que utilize o conceito de pivôs.

Descrição do Problema
Dado k conjuntos de n chaves diferentes e n cadeados diferentes, crie duas sequências onde a i-ésima chave da sequencia de chaves abra o i-ésimo cadeado da sequência de cadeados.

Restrição 1: A comparação de uma chave com outra chave ou um cadeado com outro cadeado não é permitida. Isso significa que a chave só pode ser comparada com o cadeado e o cadeado só pode ser comparado com a chave para ver qual deles é maior / menor.

Restrição 2: A metodologia de resolução deve seguir os requisito impostos por Scooby.

Para cada iteração, você deve exibir a sequência organizada das chaves e a sequência organizada dos cadeados.


Input Specification

O primeiro valor k informado será a quantidade de vezes que Wesley realizará um desafio.

K

Após isso, seguem k vezes duas sequencias correspondentes ao baú das chaves e ao baú dos cadeados, respectivamente.

B0

C0

...

Bk

Ck


Output Specification

Para cada iteração, você deve exibir a sequência organizada das chaves e a sequência organizada dos cadeados. """

def main():

    def trocar (lista, i, j):
        temp = lista[i]
        lista[i] = lista[j]
        lista[j] = temp


    def particao(lista, esq, dir, listaaux):
        pivo = listaaux[esq]
        i = esq
        j = dir + 1

        while True:
            i += 1
            while lista[i] < pivo:
                if i >= dir:
                    break
                i += 1
            j -= 1
            while lista[j] > pivo:
                if j <= esq:
                    break
                j -= 1
            if i >= j:
                break
            trocar(lista, i, j)
        trocar(lista, esq, j)
        return j


    def qs (lista, esq, dir, listaaux):
        if esq >= dir:
            return
        p = particao(lista, esq, dir, listaaux)
        qs(lista, esq, p-1, listaaux)
        qs(lista, p+1, dir, listaaux)

    
    def quicksort(lista, tamanho, listaaux):
        qs(lista, 0, tamanho-1, listaaux)

    
    k = int(input())

    for i in range(k):
        chaves = input()
        cadeados = input()
        
        listachaves = chaves.split()
        listacadeados = cadeados.split()

        tamanhocahves = len(listachaves)
        tamanhocadedos = len(listacadeados)

        cont = 0
        while cont <= 35:
            quicksort(listachaves, tamanhocahves, listacadeados)
            quicksort(listacadeados, tamanhocadedos, listachaves)
            cont += 1  

        print(*listachaves, sep = ' ')
        print(*listacadeados, sep = ' ')


if __name__ == '__main__':
    main()