""" Dado um array representando uma árvore binária, calcule a média dos valores em cada nível da árvore.

Dois nós estão num mesmo nível se a sua altura em relação à raiz é igual.

A representação da árvore se dará por uma sequência de inteiros positivos, tal que:

Para todos os nós "i":
2 * i + 1 é a posição do seu filho esquerdo.
2 * i + 2 é a posição do seu filho direito.
Considere que o nível da raiz é "1". Logo, o nível dos filhos da raiz é "2", e assim em diante.


Input Specification

S[0] S[1] S[2] ... S[n]


Output Specification

Para todos os níveis da árvore, printe:
Media do nivel i = m
Onde:
i = Nível
m = Média dos valores naquele nível. """


def main():

    seq = input()
    lista = seq.split()
    tamanho = len(lista)

    for i in range(tamanho):
        lista[i] = int(lista[i])

    cont = 0
    aux = 1
    k = 1
    dici = {}
    for i in range (1, tamanho+1):
        dici[i] = []


    for i in range(tamanho):

        if k <= 2**cont:
            dici[aux].append(lista[i])
            k += 1
        else:
            dici[aux+1].append(lista[i])
            aux += 1
            cont += 1
            k = 2

    soma = 0
    conta = 0


    for i in dici:
        while dici[i] != []:
            for j in dici[i]:
                if j != -1:
                    soma += j
                    conta += 1
            dici[i] = []
            media = soma / conta
            print('Media do nivel', i, '=', '%.2f' % media)
            soma = 0
            conta = 0


if __name__ == '__main__':
    main()
