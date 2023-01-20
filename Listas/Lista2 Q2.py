""" Isolado em casa sem nada pra fazer, você descobre perambulando pela internet um jogo extremamente viciante chamando "GAME OF THE ANIMAL". Nele, os jogadores competem apostando em números representados por animais, e, se sorteados, ganham pontuação.

Por ser muito popular, o jogo conta com uma ampla comunidade de jogadores. Mas, infelizmente, não há nenhuma organização entre as pontuações, tornando impossível saber quem é melhor jogador que quem.

Comovido por essa triste realidade e motivado a por em prática seus conhecimentos de programação, você decide implementar um sistema de rankings que recebe o nome e a pontuação de jogadores e os organiza de uma maneira eficiente.

Descrição do Problema
No começo do programa, vocẽ receberá um inteiro K e logo após K comandos do tipo ADD, para adicionar jogadores no sistema, ou PROX, que pede ao sistema que informe as proximidades de um jogador particular.

As proximidades de um jogador são definidas pelo sucessor e predecessor do jogador, se existirem, em ordem crescente de pontuação.

Exemplo:

JOGADOR	  ANA BOB CARLOS DANIEL	ELISA
PONTUAÇÃO	2	3	6	4	5
Em ordem de pontuação, temos:

ANA - BOB - DANIEL - ELISA - CARLOS

Pontanto:

Proximidades de ANA : BOB é seu sucessor.
Proximidades de DANIEL : BOB é seu predecessor, e ELISA é sua sucessora.
Proximidades de CARLOS : ELISA é sua predecessora.
OBS:

Todos os jogadores possuem nomes únicos e pontuações únicas.
Não será requisitada as proximidades de um jogador que não se encontra no sistema.
Comandos
ADD N P -> Insere um jogador de nome N pontuação P.
PROX P -> Retorna as proximidades do jogador de pontuação P.


Input Specification

K
Comando 1
Comando 2
...
Comando N


Output Specification

Após o comando ADD N P:

Se o jogador N já estiver no sistema, imprimir: "N ja esta no sistema."
Senão, imprimir: "N inserido com sucesso!"
Após o comando PROX P:

Se o jogador de pontuação P e nome N não possuir proximidades, imprimir: "Apenas N existe no sistema..."
Senão, se possuir apenas sucessor SUC, imprimir: "N e o menor! e logo apos vem SUC "
Senão, se possuir apenas predecessor PRE, imprimir: "N e o maior! e logo atras vem PRE "
Senão, imprimir: "N vem apos PRE e antes de SUC" """

def main():
    
    class jogador:
        def __init__(self, nome, pontos):
            self.nome = nome
            self.pontos = pontos
            self.esquerda = None
            self.direita = None
            self.pai = None



    def adicionar(raiz, nome, pontos):
        node = jogador(nome, pontos)
        y = None
        x = raiz

        while x != None:
            y = x
            if node.pontos < x.pontos:
                x = x.esquerda
            elif node.pontos > x.pontos:
                x = x.direita
            else:
                print(nome,'ja esta no sistema.')
                return raiz
        
        node.pai = y
        if y == None:
            raiz = node
        elif node.pontos < y.pontos:
            y.esquerda = node
        else:
            y.direita = node
        
        print(nome,'inserido com sucesso!')
        
        return raiz
    
    def maximo(raiz):
        x = raiz
        while x.direita != None:
            x = x.direita
        
        return x

    def minimo(raiz):
        x = raiz
        while x.esquerda != None:
            x = x.esquerda
        
        return x

    def sucessor(node):
        x = node
        if x.direita != None:
            return minimo(x.direita)

        y = x.pai
        while y != None and x == y.direita:
            x = y
            y = y.pai
        
        return y

    def antecessor(node):
        x = node
        if x.esquerda != None:
            return maximo(x.esquerda)
        
        y = x.pai
        while y != None and x == y.esquerda:
            x = y
            y = y.pai
        
        return y

    def busca(raiz, pontos):
        x = raiz
        while x != None and pontos != x.pontos:
            if pontos < x.pontos:
                x = x.esquerda
            else:
                x = x.direita
        
        return x


    def proximidades(raiz, pontos):

        no = busca(raiz, pontos)
        if no.pai == None and no.direita == None and no.esquerda == None:
            print('Apenas', no.nome,'existe no sistema...')
        
        elif no == minimo(raiz):
            print(no.nome,'e o menor! e logo apos vem', sucessor(no).nome)
        
        elif no == maximo(raiz):
            print(no.nome,'e o maior! e logo atras vem', antecessor(no).nome)

        else:
            print(no.nome,'vem apos', antecessor(no).nome,'e antes de', sucessor(no).nome)

        
    
        
    
    n = int(input())
    raiz = None
    

    for i in range (n):
        cmd = input()
        stri = cmd.split()


        if stri[0] == 'ADD':
            
            raiz = adicionar(raiz, stri[1], int(stri[2]))
            
        if stri[0] == 'PROX':
            
            proximidades(raiz, int(stri[1]))



if __name__ == '__main__':
    main()