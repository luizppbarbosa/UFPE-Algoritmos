class NoLista:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.proximo = None
        self.anterior = None

def inserirElemento(noInicio, nome, idade):
    no = NoLista(nome, idade)
    no.proximo = noInicio
    if noInicio != None:
        noInicio.anterior = no
    noInicio = no
    no.anterior = None
    
    return no

def imprimeTodos(noInicio):
    x = noInicio
    print("POKEMONS CADASTRADOS")
    while x!= None :
        print(x.nome)
        x = x.proximo
    return x

def procurarElemento(noInicio, nome):
    x = noInicio
    while x!= None and x.nome != nome:
        x = x.proximo
    return x
    
def removerElemento(noInicio, nome):
    elemento = procurarElemento(noInicio, nome)
    if elemento == None: 
      print("Elemento não existe na lista")
      return noInicio
      
    if elemento.anterior !=None:
        elemento.anterior.proximo = elemento.proximo
    else:
        noInicio = elemento.proximo
    if (elemento.proximo != None):
        elemento.proximo.anterior = elemento.anterior
    
    return noInicio
    
    
noInicio = None
while(True):
    print("1-cadastrar\n2-procurar;\n3-remover\n4-imprimir todos\n5-Sair\n")
    opcao = input()
    if (opcao == "1"):
        nome = input("digite o nome:")
        idade = input("digite o idade:")
        noInicio = inserirElemento(noInicio, nome, idade)
                      
    elif(opcao == "2"):
        nome = input("digite o nome:")
        x = procurarElemento(noInicio, nome)
        if (x == None):
            print("nao encontrado")
        else:
            print("nome", x.nome, "idade", x.idade)
        
    elif(opcao == "3"):
        nome = input("digite o nome:")
        noInicio = removerElemento(noInicio, nome)
    elif (opcao == "4"): 
        imprimeTodos(noInicio)
    elif (opcao == "5"):
        break
        