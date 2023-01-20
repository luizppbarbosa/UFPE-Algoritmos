""" Você bateu a cabeça com bastante força enquanto andava de bicicleta pelo Centro de Informática da UFPE. Felizmente, você passa bem. Há um porém: você agora é viciado no jogo dos extremos. O jogo é muito simples: você recebe uma sequência de inteiros S e uma constante A, e a cada rodada você deve realizar a seguinte operação:

Seja max o maior elemento de S e min o menor elemento de S :

Remova max de S

Faça: K = max - | min * A |

Se K > 0, coloque K em S e parta para a próxima rodada.

Senão, parta para a próxima rodada.
O jogo acaba quando não há mais nenhum elemento em S. Recebendo S e A, descubra em quantas rodada o jogo acabará!

Exemplo:
Entrada: 5 5 8 11 2

Rodada 1:

S (Em ordem decrescente): 11 8 5 5
Operação: 11 - |5 * 2| = 1
Rodada 2:

S: 8 5 5 1
Operação: 8 - |1 * 2| = 6
Rodada 3:

S: 6 5 5 1
Operação: 6 - |1 * 2| = 4
Rodada 4:

S: 5 5 4 1
Operação: 5 - |1 * 2| = 3
[...]

Rodada 10:

S: 1 1 1
Operação: 1 - |1 * 2| = -1
Rodada 11:

S: 1 1
Operação: 1 - |1 * 2| = -1
Rodada 12:

S: 1
Operação: 1 - |1 * 2| = -1
Após a 12 segunda rodada, S está vazia. Logo, foram necessárias 12 rodadas para o jogo acabar.


Input Specification

S[0] S[1] ... S[N-1]
A


Output Specification

Após o cálculo, printe "R rodadas!", onde R é o número de rodadas necessárias para que o jogo acabe. """


def main():


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

    def getmin (lista, tamanho):
        min = 99999999999999999999
        for i in range ((tamanho+1)//2, tamanho):
            if lista[i] < min:
                min = lista[i]

        return min


    seq = input()
    listamax = [None] + seq.split()

    for i in range(1, len(listamax)):
        listamax[i] = int(listamax[i])
        
        
    tamanho = len(listamax) - 1 
    criamaxheap(listamax, tamanho)
    


    const = int(input())


    max = listamax[1]
    min = getmin(listamax, tamanho)
    cont = 0

    while tamanho != 0:
        k = max - abs(min*const)
        cont += 1
        if k > 0:
            listamax[1] = k
            maxheapify(listamax, 1, tamanho)
            max = listamax[1]
            if k < min:
                min = k
            
        else:
            pos1 = listamax[1]
            pos2 = listamax[tamanho]
            listamax[1] = pos2
            listamax[tamanho] = pos1
            tamanho = tamanho - 1
            maxheapify(listamax, 1, tamanho)

    print(cont,'rodadas!')


if __name__ == '__main__':
    main()