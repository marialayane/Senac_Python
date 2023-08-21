# 7
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
