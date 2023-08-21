# 2
print('-' * 48)
print('-----Programa para receber 5 nomes e estado-----')
print('-' * 48)
lista_set = set()

for x in range(5):
  nome = str(input('Nome: '))
  estado = str(input('Estado: '))
  lista_set.add(nome)
  lista_set.add(estado)

print(lista_set)
print(type(lista_set))