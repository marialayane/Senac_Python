#1
"""
print('-' * 48)
print('-------Criando um set e adicionando itens-------')
print('-' * 48)

lista_set = set()
print('Para criar o set, por favor informe alguns dados.')
nome = str(input('Informe o nome: '))
lista_set.add(nome)
idade = int(input('Informe a idade: '))
lista_set.add(idade)
sexo = str(input('Informe o sexo: '))
lista_set.add(sexo)

print('Set: {}'.format(lista_set))
"""

# 2
"""
print('-' * 48)
print('-----Programa para receber 5 nomes e estado-----')
print('-' * 48)
lista_set = set()

for x in range(5):
  nome = str(input('Nome: '))
  estado = str(input('Estado: '))
  lista_set.add(nome)
  lista_set.add(estado)

print(lista_set)
print(type(lista_set))
"""

# 3
"""
lista_set = {'maria', 'ana', 'paulo', 'julia'}
print('Lista atual: ', lista_set)

# adicionando nome na lista
nome = str(input('Informe o nome que deseja adicionar: '))
lista_set.add(nome)
print('O nome adicionado foi: ', nome)
print('Lista atualizada: ', lista_set)
print('-'*60)

# removendo nome da lista
nome_removido = str(input('Informe o nome que deseja remover: '))
lista_set.remove(nome_removido)
print('O nome removido foi: ', nome_removido)
print('Lista atualizada: ', lista_set)
"""

# 4
"""
print('-' * 65)
print('-' * 24, 'Criando um Set', '-' * 25)
print('-' * 65)
lista_set = set()

# adicionar 4 valores num Set
print('Por favor, informe os números que você deseja acrescentar no Set.')
for x in range(4):
    num = int(input('Número {}: '.format(x + 1)))
    lista_set.add(num)

print('Números adicionados pelo usuário:', lista_set)

# remover um valor aleatorio
num_removido = lista_set.pop()
print('Número removido pelo comando pop:', num_removido)
print('Lista atualizada', lista_set)

# esvaziar lista
print('Hora de esvaziar a lista')
lista_set.clear()
print('Lista vazia:', lista_set)
"""
