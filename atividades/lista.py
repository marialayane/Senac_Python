# 1
"""
print('-' * 42)
print('------ Adicionando itens numa lista ------')
print('-' * 42)
tamanho_lista = input('Quantos itens você quer adicionar na lista? ')
i = 0
lista = []
while tamanho_lista.isnumeric() == False:
   print('Digite um número.')
   tamanho_lista = input('Quantos itens você quer adicionar na lista? ')
while i < int(tamanho_lista):
    item = input('Digite um item: ')
    lista.append(item)
    i+=1
print('A lista é igual a {}'.format(lista))
"""

# 2
"""
print('-' * 42)
print('-----Comparando dois números inteiros-----')
print('-' * 42)
i = int(input('Digite o primeiro número: '))
j = int(input('Digite o segundo número: '))
listaNumeros = [i, j]
if i > j:
    print('O primeiro número ({}) é maior que o segundo ({})'.format(i, j))
elif j > i:
    print('O segundo número ({}) é maior que o primeiro número ({})'.format(j, i))
else:
    print('Os números são iguais')
"""

# 3
"""
print('-' * 42)
print('------ Ordenando números numa lista ------')
print('-' * 42)
tamanho_lista = input('Quantos números você quer digitar? ')
i = 0
lista_numero = []
while tamanho_lista.isnumeric() == False:
    print('Por favor digite um número.')
    tamanho_lista = input('Quantos números você quer digitar? ')

while i < int(tamanho_lista):
    numero = int(input('Digite um número: '))
    lista_numero.append(numero)
    i += 1

print('\n')
print('*' * 42)
print('lista atual: {}'.format(lista_numero))
lista_numero.sort()
print('A lista em ordem crescente: {}'.format(lista_numero))
lista_numero.sort(reverse=True)
print('A lista em ordem decrescente: {}'.format(lista_numero))
"""

# 4
"""
lista_de_compras = ['Achocolatado', 'Açúcar', 'Azeite', 'Batata palha', 'Feijão', 'Fermento', 'Gelatina', 'Palmito',
                    'Vinagre', 'Chá', 'Café']
print('-' * 42)
item = input('Qual item você quer verificar se existe na lista de compras? \nDigite aqui: ')

if item in lista_de_compras:
    print('O item {} está dentro da lista'.format(item))
    print('Lista atual: {}'.format(lista_de_compras))

    print('Até mais!! :)')
    print('-' * 42)
else:
    print('O item {} não está dentro da lista'.format(item))
    verificacao = input('Deseja adicioná-lo? \n1- Sim \n2- Não \nInforme aqui: ')
    if verificacao == '1':
        lista_de_compras.append(item)
        print('Item adicionado com sucesso!')
        print('Lista atual: {}'.format(lista_de_compras))
        print('Até mais!! :)')
        print('-' * 42)
    else:
        print('Até mais!! :)')
        print('-' * 42)
"""
# 5
"""
tamanho_lista = input('Quantos nomes você quer adicionar na lista? ')
i = 0
lista = []
lista_maiuscula = []
lista_minuscula = []

while tamanho_lista.isnumeric() == False:
    print('Por favor digite um item.')
    tamanho_lista = input('Quantos nomes você quer adicionar na lista? ')

while i < int(tamanho_lista):
    nome = str(input('Digite um nome: '))
    lista.append(nome)
    i += 1

i = 0
while i < int(tamanho_lista):
    maiuscula = lista[i].upper()
    minuscula = lista[i].lower()
    lista_maiuscula.append(maiuscula)
    lista_minuscula.append(minuscula)
    i += 1

print('Lista atual: {}'.format(lista))
print('Lista maiuscula: {}'.format(lista_maiuscula))
print('Lista minuscula: {}'.format(lista_minuscula))
"""

# 6
"""
print('-' * 117)
print('-' * 45, 'Removendo itens numa lista', '-' * 44)
print('-' * 117)

lista = ['Camomila', 'Erva doce', 'Erva cidreira', 'Hibisco', 'Verde', 'Hortelã', 'Alecrim', 'Boldo', 'Lavanda']

print('Lista atual: {}'.format(lista))
remover = int(input('qual item você quer remover? \nInforme a posição do item na lista: '))
lista.pop(remover)
print('\n')
print('Item removido com sucesso! :)')
print('Lista atualizada: {}'.format(lista))

print('\n')
print('Obrigada pela interação!! :)')
print('Até mais')
"""

#7
"""
print('-' * 110)
print('-' * 38, 'Realizando uma adição numa tupla', '-' * 38)
print('-' * 110)

tupla = (1958, 1962, 1970, 1994)
print('Anos que o Brasil ganhou a Campeonato Mundial de Futebol Masculino: {}'.format(tupla))

lista = list(tupla)
lista.append(2002)
tupla_atualizada = tuple(lista)
print('\n')
print('Atualizando...')
print('Anos que o Brasil ganhou a Campeonato Mundial de Futebol Masculino atualizada*: {}'.format(tupla_atualizada))
"""