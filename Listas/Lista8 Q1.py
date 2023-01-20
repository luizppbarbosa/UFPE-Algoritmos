""" Você é um ladrão de alto calibre, que pelos anos de experiência no ramo sabe exatamente quanto dinheiro existe em cada casa da rua mais rica da região. Mas, antes de realizar o roubo que te tornará dono do quadrilionário, você deve ter precaução: é conhecimento comum de todo bom ladrão que não se rouba duas casas consecutivas, pois o vizinho já terá alertado a polícia. Sabendo disso, descubra qual o maior valor em reais que você pode adquirir roubando a rua, sem alertar a polícia.

Ex:

5
4 5 7 8 1
Casa 0: 4 Reais

Casa 1: 5 Reais

Casa 2: 7 Reais

Casa 3: 8 Reais

Casa 4: 1 Real

A maior quantidade que pode ser roubada sem alertar a polícia é de 5 (Casa 1) + 8 (Casa 3) = 13 Reais. Perceba que não é possível roubar nenhuma outra casa sem alertar a polícia.


Input Specification

N
S[0] S[1] S[2] ... S[n-1]

N , o número de casas na rua.
S[0] S[1] S[2] ... S[n-1], onde S[i] representa o valor guardado na casa de posição i.


Output Specification

Após o cálculo, printe "X reais podem ser roubados hoje!", onde X é a quantia máxima total que pode ser roubada pelas casas S. """


def main():

    def maximo (i, j):
        if i >= j:
            return i
        else:
            return j

    n = int(input())
    s = input().split()
    for i in range(len(s)):
        s[i] = int(s[i])

    if n == 0:
        return 0
    
    if n == 1:
        return s[0]

    if n == 2:
        return maximo(s[0], s[1])

    
    aux = [None]*n
    aux[0] = s[0]
    aux[1] = maximo(s[0], s[1])
    for i in range (2,n):
        aux[i] = maximo(s[i] + aux[i-2], aux[i-1])


    
    print(aux[-1],'reais podem ser roubados hoje!')
    

if __name__ == '__main__':
    main()