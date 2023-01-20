""" Dadas N listas com elementos separados por ,, imprima a maior delas.


Input Specification

Seguem N linhas, cada uma contendo uma lista de elementos separados por , e delimitada por [ e ].


Output Specification

Imprima a maior das N listas, como dada na entrada.
Em caso de empate, deve-se imprimir a primeira das N listas que possui tal maior número de elementos. """


def main():
    try:
        linhas = []
        listamaior = ''
        contv = 0
        ordem = -1

        while True:
            linhas.append(input())
     
    except:
        pass
    

    for i in linhas:
        contv = i.count(',')

        if contv > ordem:
            listamaior = i
            ordem = contv

    print(listamaior)
    
    


if __name__ == '__main__':
    main()