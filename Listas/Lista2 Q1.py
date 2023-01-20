""" Crie um programa que recebe duas sequências numéricas positivas, onde a primeira sequência está ordenada, e retorna duas sequências: T, que é formada pelos números da 2ª sequência que estão contidos na 1ª e F, formada pelos numeros da 2ª sequência que não estão contidos na 1ª.

Input Specification

S[1] S[2] S[3] ... S[x]
N[1] N[2] N[3] ... N[y]


Output Specification

T[1] T[2] T[3] ... T[z]
F[1] F[2] F[3] ... F[w] """


def main():

    def rank(chaves, pontos):
        inicio = 0
        fim = len(chaves) - 1
        while inicio < fim:
            meio = int((fim + inicio) / 2)
            if chaves[meio] > pontos:
                fim = meio - 1
            elif chaves[meio] < pontos:
                inicio = meio + 1
            else:
                return meio
        return inicio


    entrada1 = input()
    lista1 = entrada1.split()
    for i in range(len(lista1)):
        lista1[i] = int(lista1[i])
    
    entrada2 = input()
    lista2 = entrada2.split()
    for i in range(len(lista2)):
        lista2[i] = int(lista2[i])

    T = []
    F = []

    for i in lista2:
        if i == lista1[rank(lista1,i)]:
            T.append(i)
        else:
            F.append(i)
        

    print(*T, sep = ' ')
    print(*F, sep = ' ')


        
if __name__ == '__main__':
    main()