# 4
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