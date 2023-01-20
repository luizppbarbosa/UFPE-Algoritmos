""" Você foi contratado por uma empresa de aviação na tentativa de diminuir o custo de sua malha aérea. Eles querem que você desenvolva um sistema que irá receber todos os trechos (ida e volta) com seus respectivos custos, e retorne qual o menor custo possível para a empresa, de modo que, partindo de qualquer cidade, os destinos diretos ou indiretos antes das alterações se mantenham.


Input Specification

Na primeira linha você vai receber 2 valores M e N representando o número de aeroportos e de trechos (ida e volta) respectivamente
Seguido por N linhas representando os trechos.
IdA0 IdB0 P0
IdA1 IdB1 P1
...
IdAn IdBn Pn
Onde:
IdAi representa o id do aeroporto A (0 <= IdAi < M)
IdBi representa o id do aeroporto B (0 <= IdBi < M)
Ci representa o custo para a empresa para manter o trecho entre A e B


Output Specification

Após o processamento o seu sistema deve imprimir o custo minimo para a empresa de modo a manter os destinos diretos e indiretos de cada cidade alcançáveis. """


def main():

    class Grafo:
        def __init__(self, vertices, arestas):
            self.V = vertices
            self.A = arestas

        def find(self, parent, i):
            if parent[i] == i:
                return i
            return self.find(parent, parent[i])

        def apply_union(self, parent, rank, x, y):
            xroot = self.find(parent, x)
            yroot = self.find(parent, y)
            if rank[xroot] < rank[yroot]:
                parent[xroot] = yroot
            elif rank[xroot] > rank[yroot]:
                parent[yroot] = xroot
            else:
                parent[yroot] = xroot
                rank[xroot] += 1

        def kruskal(self):
            result = []
            i, e = 0, 0
            parent = []
            rank = []
            peso = 0
            for node in range(len(self.V)):
                parent.append(node)
                rank.append(0)
            while e < len(self.V) - 1:
                u, v, w = self.A[i]
                i = i + 1
                x = self.find(parent, u)
                y = self.find(parent, v)
                if x != y:
                    e = e + 1
                    result.append([u, v, w])
                    self.apply_union(parent, rank, x, y)
                    peso += w
            print(peso)

    def trocar (lista, i, j):
        temp = lista[i]
        lista[i] = lista[j]
        lista[j] = temp


    def particao(lista, esq, dir):
        pivo = lista[esq][2]
        i = esq
        j = dir + 1

        while True:
            i += 1
            while lista[i][2] < pivo:
                if i >= dir:
                    break
                i += 1
            j -= 1
            while lista[j][2] > pivo:
                if j <= esq:
                    break
                j -= 1
            if i >= j:
                break
            trocar(lista, i, j)
        trocar(lista, esq, j)
        return j


    def qs (lista, esq, dir):
        if esq >= dir:
            return
        p = particao(lista, esq, dir)
        qs(lista, esq, p-1)
        qs(lista, p+1, dir)

    
    def quicksort(lista, tamanho):
        qs(lista, 0, tamanho-1)
        


    in1 = input().split()
    V = int(in1[0])
    E = int(in1[1])

    vertices = [None]*V
    antecessor = [-1]*V
    arestas = []

    for i in range (V):
        vertices[i] = i

    for i in range(E):
        in2 = input().split()
        u = int(in2[0])
        v = int(in2[1])
        w = int(in2[2])
        arestas.append([u, v, w])
    
    tamanho = len(arestas)
    quicksort(arestas, tamanho)
    g = Grafo(vertices, arestas)
    g.kruskal()
    
    


if __name__ == '__main__':
    main()