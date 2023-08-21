# 1

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