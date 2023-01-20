""" Em uma rede social, há n usuários se comunicando entre si e m conexões de amizade. O processo de distribuição de notícias funciona da seguinte maneira:

Um usuário i (1 <= i <= n) recebe a notícia de alguma fonte. Então, esse usuário passa a notícia para seus amigos, os amigos repassam para seus amigos e assim em diante. O processo acaba quando não há um par de amigos em que um sabe a notícia e o outro não.

Para cada usuário i (1 <= i <= n), determine a quantidade de usuários que saberia a notícia se i iniciasse a distruição.


Input Specification

Na primeira linha você vai receber 2 valores n e m representando o número de usuários e de conexões entro os usuários.
Seguido por m linhas com 2 inteiros u e v representando os usuários conectados.


Output Specification

Imprima n inteiros. O i-th inteiro deve ser igual ao número de usuários que saberiam a notícia se o usuário i começar distribuindo-a. """


def main():

    class Grafo:
        def __init__(self, vertices, arestas):
            self.V = vertices
            self.A = arestas
        def adj(self, v):
            return self.A[v]

    def conect(g, v, aux):
        if g.adj(v) == []:
            aux = [v]
            return aux
        for i in g.adj(v):
            if i not in aux:
                aux.append(i)
                conect(g,i, aux)
        return aux


    prim = input().split()

    qtdvertices = int(prim[0])
    qtdarestas = int(prim[1])


    vertices = [None]*qtdvertices
    arestas = {}

    for i in range (qtdvertices):
        vertices[i] = i+1
        arestas[i+1] = []


    for i in range (qtdarestas):
        conex = input().split()
        ar1 = int(conex[0])
        ar2 = int(conex[1])
            
            
        arestas[ar1].append(ar2)
        arestas[ar2].append(ar1)


    g = Grafo(vertices, arestas)
    lista = []
    listaV = []


    for i in g.V:
        if i not in listaV:
            aux = []
            cont = 0
            listaV = conect(g, i, aux)
            cont = len(listaV)
        lista.append(cont)

    print(*lista, sep = ' ')

if __name__ == '__main__':
    main()
