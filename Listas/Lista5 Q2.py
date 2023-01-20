""" Guilherme está no processo seletivo para a empresa de software CInderela. A recrutadora perguntou a sua expectativa salarial, mas ele não soube responder na hora.

Ele resolveu que vai pedir um salário de acordo com a mediana dos salários da empresa que ele trabalha atualmente e da CInderela, e precisa da sua ajuda para isso.

Dados dois arrays ordenados salarios_m e salarios_n, representando respectivamente os salários da empresa atual e os salários da empresa CInderela, retorne a mediana dos dois arrays ordenados.


Input Specification

salarios_m

salarios_n


Output Specification

Após o cálculo, retorne a mediana dos dois arrays formatada com 2 casas decimais. 
"""

def main():

    def merge (lista, esq, meio, dir, aux):
        i = esq
        j = meio + 1

        for k in range (esq, dir+1):
            aux[k] = lista[k]
            
        for k in range (esq, dir+1):
            if i > meio:
                lista[k] = aux[j]
                j += 1
            elif j > dir:
                lista[k] = aux[i]
                i += 1
            elif aux[i] > aux[j]:
                lista[k] = aux[j]
                j += 1
            else:
                lista[k] = aux[i] 
                i += 1





    salarios_m = input()
    salarios_n = input()

    lista1 = salarios_m.split()
    lista2 = salarios_n.split()

    lista = lista1 + lista2

    tamanho = len(lista)

    for i in range(tamanho):
        lista[i] = int(lista[i])



    aux = lista[:]
   #SORT
    merge(lista, 0, len(lista1)-1, len(lista)-1, aux)
    
 

    if tamanho % 2 == 0:
        mediana = (lista[tamanho//2 - 1]  + lista[(tamanho//2)]) / 2
    else:
        mediana = lista[(tamanho//2)]

    print ('%.2f' % mediana)

if __name__ == '__main__':
    main()