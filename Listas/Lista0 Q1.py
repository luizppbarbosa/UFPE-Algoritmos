""" Malu precisa da sua ajuda para criar um programa que verifica se uma expressão está bem formada por chaves. A definição de expressão bem formada é a seguinte:

Uma expressão vazia é sempre bem formada (i.e. uma string vazia)
Se E é bem formada, então { E } também é bem formada
Se E é bem formada, então E E também é bem formada
Ela conseguiu coletar alguns exemplos de expressões bem formadas para te ajudar a entender o problema:

{ { { } } }
{ } { }
{ { } } { }
{ { } { { } { } } }
E também alguns exemplos de expressões mal formadas:

{ } {
{ { } } { } }
{ } { } }
{ { } } { { { } }

Input Specification

A única linha de entrada é composta por uma string E, a expressão formada por chaves. Cada chave estará separada por exatamente um espaço.

Output Specification

Você deve produzir uma única linha de saída com o caractere S caso a expressão seja bem formada, ou N caso contrário. """


def main():
    entrada = input()
    cont1 = entrada.count('{')
    cont2 = entrada.count('}')
    contchave = 0
    verif = True

    for i in range (len(entrada)):
        if entrada[i] == '{':
            contchave += 1
        elif entrada[i] == '}':
            contchave -= 1

        if contchave == -1 and i != " ":
            verif = False


    if contchave != 0:
        print('N')
    elif verif == False:
        print('N')
    else:
        print('S')


        
if __name__ == '__main__':
    main()