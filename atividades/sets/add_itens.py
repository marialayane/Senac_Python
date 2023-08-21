# 1
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