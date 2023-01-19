# Se for um problema que use Bellman-Ford, a entrada para seu programa
# deve ser o grafo, o vértice de início, o vértice fim, e a saída o
# menor menor caminho, e seus pesos, entre esses vértices.

from pyvis.network import Network
from tkinter import*

class Grafo:
    # iniciação do grafo
    def __init__(self, vertices, arestas):
        self.V = vertices
        self.A = arestas

def haCiclos(g, peso):
    # verifica se há ciclos negativos no grafo
    for aresta in g.A:
        if peso[int(aresta[0])] != 9999 and peso[int(aresta[1])] > peso[int(aresta[0])] + aresta[2]:
            return False
    return True

class Application:
    # INTERFACE GRÁFICA
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()

        self.quintoContainer = Frame(master)
        self.quintoContainer["pady"] = 20
        self.quintoContainer.pack()

        # título
        self.titulo = Label(self.primeiroContainer, text="Verificar qual a menor rota de\num aeroporto a outro: ")
        self.titulo["font"] = ("Arial", "12", "italic")
        self.titulo.pack()

        # label e input do aeroporto de origem
        self.origemLabel = Label(self.segundoContainer,text="Aeroporto de Origem: ", font=self.fontePadrao)
        self.origemLabel.pack(side=LEFT)

        self.origem = Entry(self.segundoContainer)
        self.origem["width"] = 30
        self.origem["font"] = self.fontePadrao
        self.origem.pack(side=LEFT)

        # label e input do aeroporto de destino
        self.destinoLabel = Label(self.terceiroContainer, text="Aeroporto de Destino: ", font=self.fontePadrao)
        self.destinoLabel.pack(side=LEFT)

        self.destino = Entry(self.terceiroContainer)
        self.destino["width"] = 30
        self.destino["font"] = self.fontePadrao
        self.destino.pack(side=LEFT)

        # gatilho para o algoritmo de bellman-ford
        self.verificar = Button(self.quintoContainer)
        self.verificar["text"] = "Verificar"
        self.verificar["font"] = ("Calibri", "8")
        self.verificar["width"] = 12
        self.verificar["command"] = self.verifica
        self.verificar.pack()

        # fecha o programa
        self.sair = Button(self.quintoContainer)
        self.sair["text"] = "Sair"
        self.sair["font"] = ("Calibri", "6")
        self.sair["width"] = 5
        self.sair["command"] = self.quartoContainer.quit
        self.sair.pack ()

    
    def verifica(self):
        # aplicação do bellman-ford e construção da visualização dos grafo
        origem = int(self.origem.get())
        destino = int(self.destino.get())
        # verifica se os vértices do input são válidos para a base de dados
        if origem < 1 or origem > 332 or destino < 1 or destino > 332:
            # se não, imprime uma mensagem de erro
            self.mensagem = Label(self.quartoContainer, text="Códigos inválidos. Tente novamente. \n[Códigos entre 1 e 332]", font=self.fontePadrao)
            self.mensagem["font"] = ("Arial", "10", "bold")
            self.mensagem.pack()
        else:
            # inicia as variaveis da visualização dos grafos
            net = Network(height='100%', width='100%')
            net2 = Network(height='100%', width='100%')
            # detalhes estéticos dos grafos
            net.set_options('''
                                var options = {
                                "nodes": {
                                    "color": {
                                    "background": "rgba(252,45,34,1)",
                                    "highlight": {
                                        "border": "rgba(233,72,42,1)",
                                        "background": "rgba(75,255,36,1)"
                                    }
                                    },
                                    "font": {
                                    "size": 100,
                                    "strokeWidth": 5,
                                    "strokeColor": "rgba(255,241,174,1)"
                                    }
                                },
                                "edges": {
                                    "arrows": {
                                    "to": {
                                        "enabled": true
                                    },
                                    "middle": {
                                        "enabled": true
                                    }
                                    },
                                    "color": {
                                    "color": "rgba(48,127,237,1)",
                                    "highlight": "rgba(249,32,38,1)",
                                    "inherit": false
                                    },
                                    "smooth": false
                                },
                                "physics": {
                                    "repulsion": {
                                    "springLength": 2000,
                                    "nodeDistance": 10000
                                    },
                                    "minVelocity": 0.75,
                                    "solver": "repulsion"
                                }
                                }
                                ''')
            net2.set_options('''
                                        var options = {
                                        "nodes": {
                                            "color": {
                                            "background": "rgba(252,45,34,1)",
                                            "highlight": {
                                                "border": "rgba(233,72,42,1)",
                                                "background": "rgba(75,255,36,1)"
                                            }
                                            },
                                            "font": {
                                            "size": 100,
                                            "strokeWidth": 5,
                                            "strokeColor": "rgba(255,241,174,1)"
                                            }
                                        },
                                        "edges": {
                                            "arrows": {
                                            "to": {
                                                "enabled": true
                                            },
                                            "middle": {
                                                "enabled": true
                                            }
                                            },
                                            "color": {
                                            "color": "rgba(48,127,237,1)",
                                            "highlight": "rgba(249,32,38,1)",
                                            "inherit": false
                                            },
                                            "smooth": false
                                        },
                                        "physics": {
                                            "repulsion": {
                                            "springLength": 2000,
                                            "nodeDistance": 1000
                                            },
                                            "minVelocity": 0.75,
                                            "solver": "repulsion"
                                        }
                                        }
                                        ''')


            vertices = [0]
            arestas = []
            fim = False
            while not fim:
                try:
                    # leitura do arquivo .txt da base de dados
                    leitura = open("aeroportos.txt", "r")
                    cont = 1
                    for valor in leitura:
                        if 1 < cont < 334:
                            # leitura dos vértices (código e nome do aeroporto)
                            nome = valor[7:47].strip()
                            vertices.append([int(valor[:6].strip()), nome.strip('"')])
                            # adiciona todos os vértices nos grafos
                            net.add_node(int(valor[:6].strip()), label=nome.strip('"'))
                            net2.add_node(int(valor[:6].strip()), label=nome.strip('"'))
                            cont += 1
                        elif 335 < cont < 2462:
                            # leitura das arestas (origem destino peso)
                            valor = valor.split()
                            arestas.append([int(valor[0]), int(valor[1]), float(valor[2])])
                            # adiciona todas as aretas apenas no grafo geral
                            net.add_edge(int(valor[0]), int(valor[1]), value=float(valor[2]))
                            cont += 1
                        else:
                            cont += 1
                    leitura.close()
                except FileNotFoundError:
                    print("Arquivo não encontrado.")
                else:
                    fim = True

            g = Grafo(vertices, arestas)

            # inicia as variáveis para a operação do bellman-ford
            peso = [9999] * (len(g.V)+1)
            antecessor = [-1] * (len(g.V)+1)
            peso[origem] = 0

            # relaxamento dos vértices |v|-1 vezes
            for i in range(len(g.V) - 1):
                for aresta in g.A:
                    if peso[int(aresta[0])] != 9999 and peso[int(aresta[1])] > peso[int(aresta[0])] + aresta[2]:
                        antecessor[aresta[1]] = aresta[0]
                        peso[aresta[1]] = peso[aresta[0]] + aresta[2]

            if not haCiclos(g, peso):
                # checagem dos ciclos negativos
                # já que a base de dados não possui arestas negativas isso nunca será printado
                print("Ciclo negativo encontrado!")
            else:
                u = destino
                # vetor solucao
                arestasusadas = []
                # já que o bellman-ford dá os menores caminhos a partir da origem
                # todos os vértices alcançáveis tem um antecessor diferente de -1
                # se o antecessor do destino é -1 ele não é alcançável
                if antecessor[u] != -1:
                    # o while irá partir do destino e retroceder...
                    # até encontrar a origem
                    while u != origem:
                        # adicionando os vértices e pesos de arestas do caminho em lista solucao
                        arestasusadas.append([antecessor[u], u, peso[u] - peso[antecessor[u]]])
                        # u vira o antecessor
                        u = antecessor[u]


                    # inserindo as arestas no grafo com os caminhos mais curtos
                    # e colorindo o caminho desejado com outro cor
                    arestasorigem = []
                    for i in range(len(g.V)):
                        if antecessor[i] != -1:
                            arestasorigem.append([g.V[antecessor[i]][0], g.V[i][0],
                                              float(peso[i] - peso[antecessor[i]])])
                    for aresta in arestasorigem:
                            if aresta in arestasusadas:
                                net2.add_edge(aresta[0], aresta[1], value=float(aresta[2]), color='purple')
                            else:
                                net2.add_edge(aresta[0], aresta[1], value=float(aresta[2]))

                    # já que partimos do destino, o vetor solução esta invertido
                    # aqui ordenamos eles na forma correta
                    arestasusadas = arestasusadas[::-1]

                    # print do enunciado com o nome do aeroporto origem e destino
                    enuncia = "O caminho do aeroporto " + g.V[origem][1] + " \naté o aeroporto " + g.V[destino][1] + " é:"
                    self.mensagem = Label(self.quartoContainer, text=enuncia, font=self.fontePadrao)
                    self.mensagem["font"] = ("Arial", "10", "bold")
                    self.mensagem.pack()

                    # organiza os vetores solucao em strings bem formatadas
                    caminho = ""
                    for aeroporto in arestasusadas:
                        caminho += str(vertices[aeroporto[0]][1]) + " -> "
                        if aeroporto[0] == arestasusadas[-1][0]:
                            caminho += vertices[destino][1]
                    caminhopeso = ""
                    soma = 0
                    for pesos in arestasusadas:
                        caminhopeso += str(round(pesos[2], 5) * 24) + ' horas'
                        soma += round(pesos[2], 5) * 24
                        if pesos[2] != arestasusadas[-1][2]:
                            caminhopeso += " -> "
                    caminhosoma = "O tempo total da viagem é de " + str(soma) + " horas."

                    # prints na interface gráfica
                    self.mensagem2 = Label(self.quartoContainer, text=caminho, font=self.fontePadrao)
                    self.mensagem2["font"] = ("Arial", "10", "italic")
                    self.mensagem2.pack()
                    self.mensagem3 = Label(self.quartoContainer, text=caminhopeso, font=self.fontePadrao)
                    self.mensagem3["font"] = ("Arial", "10", "italic")
                    self.mensagem3.pack()
                    self.mensagem4 = Label(self.quartoContainer, text=caminhosoma, font=self.fontePadrao)
                    self.mensagem4["font"] = ("Arial", "10", "italic")
                    self.mensagem4.pack()

                    net.show('Grafo_Completo.html')
                    net2.show('Grafo_Origem.html')
                else:
                    # caso não haja caminho possível entre o aeroporto origem e destino
                    # imprime mensagem de acordo
                    naotem = 'Não há caminho entre o aeroporto ' + g.V[origem][1] + '\ne o aeroporto ' + g.V[destino][
                        1] + '.'
                    self.mensagem = Label(self.quartoContainer,
                                          text=naotem,
                                          font=self.fontePadrao)
                    self.mensagem["font"] = ("Arial", "10", "bold")
                    self.mensagem.pack()


root = Tk()
Application(root)
root.mainloop()