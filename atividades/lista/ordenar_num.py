# 3
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
