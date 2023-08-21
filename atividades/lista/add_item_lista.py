# 5
tamanho_lista = input('Quantos nomes você quer adicionar na lista? ')
i = 0
lista = []
lista_maiuscula = []
lista_minuscula = []

while tamanho_lista.isnumeric() == False:
    print('Por favor digite um item.')
    tamanho_lista = input('Quantos nomes você quer adicionar na lista? ')

while i < int(tamanho_lista):
    nome = str(input('Digite um nome: '))
    lista.append(nome)
    i += 1

i = 0
while i < int(tamanho_lista):
    maiuscula = lista[i].upper()
    minuscula = lista[i].lower()
    lista_maiuscula.append(maiuscula)
    lista_minuscula.append(minuscula)
    i += 1

print('Lista atual: {}'.format(lista))
print('Lista maiuscula: {}'.format(lista_maiuscula))
print('Lista minuscula: {}'.format(lista_minuscula))
