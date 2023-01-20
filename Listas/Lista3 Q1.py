""" O professor Fernando quer dar boas vindas aos seus alunos fazendo um café da manhã no CIn, e para isso precisa sacar dinheiro no caixa eletrônico.

Dado um array de N inteiros money_available, representando as cédulas disponíveis no caixa eletrônico e um número inteiro total_cafe representando quanto o café da manhã vai custar, retorne os índices de duas cédulas que somadas, sejam exatamente o valor do café da manhã.

As cédulas são endereçadas por índice. Isto é: Duas cédulas são diferentes se seus índices forem diferentes, mesmo que seus valores sejam iguais.
As cédulas da resposta, se existirem, devem ser diferentes.
Caso não haja nenhuma solução possível, printe "Sem cafe da manha dessa vez :/"
Caso uma entrada tenha mais de uma solução, considere a primeira combinação possível.
Ou seja, se existem duas soluções u = [a,b] e v = [c,d]:
A resposta é u se a < c ou se a = c e b < d. Senão, a resposta é v.


Input Specification

N
Cédula 1
...
Cédula N
total_cafe

As entradas terão o seguinte padrão:

N -> Inteiro que representa a quantidade de cédulas disponíveis no caixa

money_available -> Array de inteiros de tamanho N, que representa as cédulas disponíveis no caixa

total_cafe -> Número inteiro representando quanto o professor deseja sacar

len(money_available) <= 1e6


Output Specification

[a, b]

Após receber total_cafe, imprima os índices dos dois primeiros elementos de money_available que somados sejam iguais a total_cafe. Se não existirem, printe "Sem cafe da manha dessa vez :/". """


def main():

    class dicionario:
        def __init__(self, chave, valor):
            self.chave = chave
            self.valor = valor
            self.esquerda = None
            self.direita = None
            self.pai = None



    def adicionar(raiz, chave, valor):
        node = dicionario (chave, valor)
        y = None
        x = raiz

        while x != None:
            y = x
            if node.valor < x.valor:
                x = x.esquerda
            elif node.valor > x.valor:
                x = x.direita
            else:
                return raiz
        
        node.pai = y
        if y == None:
            raiz = node
        elif node.valor < y.valor:
            y.esquerda = node
        else:
            y.direita = node
        
        
        return raiz
            
    def busca(raiz, valor):
        x = raiz
        while x != None and valor != x.valor:
            if valor < x.valor:
                x = x.esquerda
            else:
                x = x.direita
        
        if x == None:
            return
        else:
            return x.chave


  
    raiz = None
    aux = False

    n = int(input())

    money_available = [-999999999999] * n


    for i in range (n):
        cedula = int(input())
        raiz = adicionar(raiz, i, cedula)
        money_available [i] = cedula


    total_cafe = int(input())

    
    
    
    for i in range (n):
        sobra = total_cafe - money_available [i]
        proc = busca (raiz, sobra)
        if  proc != None:
            print('[',i,', ',proc,']', sep = '')
            aux = True
            break
        
        
            
           
            
    if aux == False:
        print('Sem cafe da manha dessa vez :/')

if __name__ == '__main__':
    main()