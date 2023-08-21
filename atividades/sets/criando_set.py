# 4
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
