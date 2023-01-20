""" Um estudante da disciplina de Algoritmos e Estruturas de Dados resolveu treinar suas habilidades com grafos. Basicamente, a ideia foi implementar um algoritmo com o objetivo de encontrar a rota com menor custo em um grafo conexo e determinar a existência de ciclos negativos. Os grafos utilizados sempre serão conexos, dirigidos e pesados (com um custo associado a cada uma das arestas do grafo).


Input Specification

Inicialmente um inteiro N indicando a quantidade de grafos que serão testados.

N
Após isso, uma linha contendo dois inteiros V e E, representando a quantidade de vertices e arestas do grafo que será testado.

V E
Seguem E linhas contendo u v e w, indicando os vertices que serão conectados e o custo da conexão:

u(0) v(0) w(0)

u(1) v(1) w(1)

...

u(V-1) v(V-1) w(V-1)

Por fim, segue um inteiro S indicando o vértice de partida da rota a ser encontrada.

S


Output Specification

Para cada grafo, deve-se buscar o menor caminho a partir do vértice S e imprimir uma linha contendo: "Ciclo negativo encontrado!" caso exista um ciclo negativo. Se não existir ciclos negativos, devem ser mostradas as seguintes informações: Vértice, Antecessor do Vértice e a Distância do ponto de partida até o Vértice.

"Vertice: u(0) Antecessor: v(0) Distancia: w(0)"
"Vertice: u(1) Antecessor: v(1) Distancia: w(1)"
...
"Vertice: u(V-1) Antecessor: v(V-1) Distancia: w(V-1)"
                  ou
Ciclo negativo encontrado! """


def main():

    class Grafo:
        def __init__(self, vertices, arestas):
            self.V = vertices
            self.A = arestas

        def printdist(self, dist, V, antecessor):
            for i in range(V):
                print('Vertice:', i, 'Antecessor:', antecessor[i], 'Distancia:', dist[i])

        
        def BellmanFord(self, S, V, antecessor):
            dist = [99999999999999] * V
            dist[S] = 0
    
            for _ in range(V - 1):
                
                for u, v, w in self.A:
                    if dist[u] != 99999999999999 and dist[u] + w < dist[v]:
                            dist[v] = dist[u] + w
                            antecessor[v] = u
    
    
            for u, v, w in self.A:
                    if dist[u] != 99999999999999 and dist[u] + w < dist[v]:
                            print('Ciclo negativo encontrado!')
                            return
                            
            
            self.printdist(dist, V, antecessor)




    N = int(input())

    for i in range(N):

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
        
        
        S = int(input())

        g = Grafo(vertices, arestas)

        g.BellmanFord(S, V, antecessor)


if __name__ == '__main__':
    main()
