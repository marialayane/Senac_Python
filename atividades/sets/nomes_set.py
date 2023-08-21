# 3
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