""" Uma das partes mais cruciais nos sistemas operacionais é a forma que o sistema escalona o tempo de execução para um processo. Em outras palavras, é como o SO divide o tempo que o processador vai executar um certo programa.

Você será encarregado de, ao receber uma lista de Processos, agenda-los em uma linha de execução e executa-los de acordo com o tempo que o processador disponibilizar. Um processo termina de executar quando seu tempo requerido chega à zero. Cada processo tem um id e um tempo requerido. Ao fim de cada execução, você deve informar quantos processos ainda estão na linha de execução.

A primeira linha do Input será sempre um inteiro N que diz o número de comandos que serão enviados.

Comandos:
ADD ID T -> Insere uma música de id ID e tempo requerido T.
EXE D -> O processador disponibiliza D segundos para a execução.
OBS:
Os processos são executados de acordo com a frente da linha de execução.
Se um processo não terminou a execução, ele deve ser enviado para o fim da linha de execução, com o seu tempo requerido atualizado.
Todos os processos, ao serem agendados, devem ser enviados para o fim da linha de execução.
Se sobrar tempo disponibilizado e o atual processo na frente da linha finalizar, o próximo da linha deve ser executado, até que a linha esteja vazia ou o tempo disponibilizado finalize.


Input Specification

N
Comando 1
Comando 2
...
Comando N


Output Specification

Após o comando ADD, imprimir: "O programa P foi agendado com sucesso!" onde P é o id do programa agendado.
Após o comando EXE, imprimir:
"O programa P executou por T segundos.", onde P é o id do programa executado, e T o tempo que ele executou.
Se o programa finalizar após a execução, imprima "O programa P terminou.", onde P é o id do programa executado.
Após o fim da execução, imprima "A linha possui S programas.", onde S é o número de programas na linha de execução. """

def main():
    
    class processo:
        def __init__(self, id, tempo):
            self.nome = id
            self.tempo = tempo
            self.proximo = None
            self.anterior = None

    def addprocesso(sentinela, id, tempo):
        proc = processo(id,tempo)
        if sentinela.proximo == None:
            proc.proximo = sentinela
            proc.anterior = sentinela
            sentinela.proximo = proc
            sentinela.anterior = proc
        else:
            proc.proximo = sentinela.proximo
            proc.anterior = sentinela
            sentinela.proximo.anterior = proc
            sentinela.proximo = proc
            

        print('O programa', id ,'foi agendado com sucesso!')

       

        
    
    def execprocesso (sentinela, tempo, cont):
        if sentinela.anterior == None:
            cont = 0
            print('A linha possui', cont ,'programas.')
        else:
            tempores = tempo
            while tempores >= 0:

                tempores = tempores - sentinela.anterior.tempo
                if tempores >= 0:
                    if sentinela.anterior.anterior != sentinela:
                        print('O programa', sentinela.anterior.nome ,'executou por', sentinela.anterior.tempo ,'segundos.')
                        print('O programa', sentinela.anterior.nome ,'terminou.')
                        sentinela.anterior.anterior.proximo = sentinela
                        sentinela.anterior = sentinela.anterior.anterior
                        cont -= 1
                    else:
                        print('O programa', sentinela.anterior.nome ,'executou por', sentinela.anterior.tempo ,'segundos.')
                        print('O programa', sentinela.anterior.nome ,'terminou.')
                        sentinela.anterior = None
                        sentinela.proximo = None
                        tempores = -1
                        cont = 0
                        print('A linha possui', cont ,'programas.')

                    
                    
                else:
                    if sentinela.anterior.anterior != sentinela:
                        print('O programa', sentinela.anterior.nome ,'executou por', sentinela.anterior.tempo + tempores ,'segundos.')
                        print('A linha possui', cont ,'programas.')
                        sentinela.anterior.tempo = tempores*(-1)
                        sentinela.proximo.anterior = sentinela.anterior
                        sentinela.anterior.proximo = sentinela.proximo
                        sentinela.anterior.anterior.proximo = sentinela
                        sentinela.anterior = sentinela.anterior.anterior
                        sentinela.proximo.anterior.anterior = sentinela
                        sentinela.proximo = sentinela.proximo.anterior
                        tempores = -1
                        


                         
                    else:
                        print('O programa', sentinela.anterior.nome ,'executou por', sentinela.anterior.tempo + tempores ,'segundos.')
                        print('A linha possui', cont ,'programas.')  
                        sentinela.anterior.tempo = tempores*(-1)
                        tempores = -1
            
        return cont                                      

        
        
    
    n = int(input())
    sentinela = processo(-1, -1)
    sentinela.proximo = sentinela.anterior
    sentinela.anterior = sentinela.proximo
    cont = 0

    for i in range (n):
        cmd = input()
        stri = cmd.split()


        if stri[0] == 'ADD':
            cont += 1
            addprocesso(sentinela, int(stri[1]), int(stri[2]))
        
        if stri[0] == 'EXE':
            
            cont = execprocesso(sentinela, int(stri[1]), cont)



if __name__ == '__main__':
    main()