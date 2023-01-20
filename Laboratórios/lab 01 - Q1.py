"""[Questão 1] Você foi contratado para desenvolver o sistema de Ash, um exímio caçador de Pokemons. Crie um menu onde Ash possa
1) Inserir um Pokemon (para cadastrar, solicite nome e idade do pokemon);
2) Procurar o Pokemon pelo nome; 
3) Remover o Pokemon pelo nome;
4) imprimir todos os Pokemons cadastrados;
5) Sair do Programa.
Implemente uma lista de Python para armazenar os pokemons."""

class pokemon:
    def __init__(self, nomePoke, idadePoke):
        self.nome = nomePoke
        self.idade = idadePoke

    def imprimedados(self):
        print(self.nome, self.idade)
        
pokedex = []

print('\n Menu de opções: \n')
print('1) Inserir um Pokémon (para cadastrar, solicite nome e idade do Pokémon);')
print('2) Procurar o Pokémon pelo nome; ')
print('3) Remover o Pokémon pelo nome;')
print('4) imprimir todos os Pokémons cadastrados;')
print('5) Sair do Programa.\n')

opcao = int(input('Digite a opção desejada: '))
while opcao <= 0 or opcao >= 6:
    opcao = int(input('Opção inválida! Digite a opção desejada: '))

while opcao != 5:
    if opcao == 1:
        nome = input('Digite o nome do Pokémon: ')
        idade = int(input('Digite a idade do Pokémon: '))
        pokedex.append(pokemon(nome,idade))

    elif opcao == 2:
        nome = input('Qual o nome do Pokémon a ser buscado: ')
        cadastrado = False
        for i in pokedex:
            if nome == i.nome:
                cadastrado = True
        if cadastrado:
            print('O Pokemón já está cadastrado na Pokédex')
        else:
            print('O Pokémon não está cadastrado na Pokédex')

    elif opcao == 3:
        nome = input('Qual o nome do Pokémon a ser removido: ')
        cadastrado = False
        for i in pokedex:
            if nome == i.nome:
                cadastrado = True
        if cadastrado:
            pokedex.remove(i)
            print('O Pokemón foi removido da Pokédex')
    
    elif opcao == 4:
        for i in pokedex:
            i.imprimedados()
        
    print('\n1) Inserir um Pokémon (para cadastrar, solicite nome e idade do Pokémon);')
    print('2) Procurar o Pokémon pelo nome; ')
    print('3) Remover o Pokémon pelo nome;')
    print('4) imprimir todos os Pokémons cadastrados;')
    print('5) Sair do Programa.\n')

    opcao = int(input('Digite a próxima opção desejada: '))


    while opcao <= 0 or opcao >= 6:
        opcao = int(input('Opção inválida! Digite a opção desejada: '))
    
print('FIM DO PROGRAMA!')


    

