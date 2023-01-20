def busca(chaves, pontos):
    inicio = 0
    fim = len(chaves) - 1
    while inicio <= fim:
        meio = int((fim + inicio) / 2)
        print(f'acessado {chaves[meio]}')
        if chaves[meio] > pontos:
            fim = meio - 1
            
        elif chaves[meio] < pontos:
            inicio = meio + 1
        else:
            return meio
    return inicio

lista = []


for i in range (1,101):
    lista.append(2*i + 1)

if lista[busca(lista,195)] == 195:
    print(195)
else:
    print('chave não encontrada')