# 6

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