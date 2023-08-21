# 2
print('-' * 42)
print('-----Comparando dois números inteiros-----')
print('-' * 42)
i = int(input('Digite o primeiro número: '))
j = int(input('Digite o segundo número: '))
listaNumeros = [i, j]
if i > j:
    print('O primeiro número ({}) é maior que o segundo ({})'.format(i, j))
elif j > i:
    print('O segundo número ({}) é maior que o primeiro número ({})'.format(j, i))
else:
    print('Os números são iguais')