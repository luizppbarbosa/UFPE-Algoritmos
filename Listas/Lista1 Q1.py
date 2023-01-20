""" Uma pilha é um tipo abstrato de dado e estrutura de dados baseado no princípio de Last In First Out (LIFO), ou seja "o último que entra é o primeiro que sai" caracterizando um empilhamento de dados. Pilhas são fundamentalmente compostas por duas operações: push que adiciona um elemento no topo da pilha e pop que remove o último elemento adicionado. Seu objetivo é desenvolver um tipo diferente de pilha, a qual é composta pelas seguintes operações:

push x : Insere um novo elemento.
getMax : Consulta o maior elemento da pilha.
getMin : Consulta o menor elemento da pilha.
pop : Remove o elemento no topo da pilha.


Input Specification

Um inteiro N , indicando a quantidade de comandos.
Comando 1
Comando 2
...
Comando N


Output Specification

Após o comando getMax, imprima um inteiro N tal que N é o maior elemento da pilha.
Após o comando getMin, imprima um inteiro N tal que N é o menor elemento da pilha.
Após o comando pop, imprima um inteiro N tal que N é o elemento no topo da pilha.
Caso a pilha se encontre vazia durante alguma operação, imprima "empty stack". """

def main(): 
    class pilha:
        def __init__(self, num):
            self.num = num
            self.proximo = None
            self.anterior = None

    def push(topo, num):
        elem = pilha(num)
        elem.proximo = topo
        if topo != None:
            topo.anterior = elem
        topo = elem
        elem.anterior = None
       

        return topo

    def pop(topo):
        if topo == None:
            print ('empty stack')
        else:
            if topo.proximo == None:
                print(topo.num)
                topo = None
            else:
                print(topo.num)
                topo.proximo.anterior = None
                topo = topo.proximo
        
        return topo

    def getMax(topo):
        aux = topo
        max = topo
        if topo == None:
            print ('empty stack')
        else:
            while aux.proximo != None:
                aux = aux.proximo
                if aux.num >= max.num:
                    max = aux
            print(max.num)
        
    def getMin(topo):
        aux = topo
        min = topo
        if topo == None:
            print ('empty stack')
        else:
            while aux.proximo != None:
                aux = aux.proximo
                if aux.num < min.num:
                    min = aux
            print(min.num)


    n = int(input())
    topo = None

    for i in range (n):
        cmd = input()

        if cmd [:4] == 'push':
            cod, num = cmd.split(' ')
            topo = push(topo, int(num))
            
        elif cmd == 'pop':
            topo = pop(topo)

        elif cmd == 'getMax':
            getMax(topo)

        elif cmd == 'getMin':
            getMin(topo)    

if __name__ == '__main__':
    main()