# 5
lista_set = {'ana', 35, 'maria', 12}
print('Lista Atual:', lista_set)

print('Informe qual categoria você quer encontrar na lista!')
print('(1)Para Texto')
print('(2)Para Inteiro')
resp = str(input('Digite aqui: '))

if resp == '1':
    nome = str(input('Informe o nome que você deseja encontrar na lista: '))
    if nome in lista_set:
        print('O nome "{}" está dentro da lista!'.format(nome))
    else:
        print('Lamento! Mas, o nome "{}" não está dentro da lista!'.format(nome))
elif resp == '2':
    num = int(input('Informe o número que você deseja encontrar na lista: '))
    if num in lista_set:
        print('O número "{}" está dentro da lista!'.format(num))
    else:
        print('Lamento! Mas, o número "{}" não está dentro da lista!'.format(num))
else:
    print('\n')
    print('*' * 44)
    print('Você não digitou nenhuma das opções acima :(')
    print('Por favor, reinicie o programa.')

print('\n')
print('Porgrama finalizado! Até mais :)')