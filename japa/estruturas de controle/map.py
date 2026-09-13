# map() serve para aplicar uma função para cada item iterável(lista, tupla, resultado de split(), etc)
# com ele voce não precisa escrever um loop manualmente

'''
map(função, iterável)
'''

entrada1 = ['1', '2']
x1, y1 = map(float, entrada1)
print(x1, y1)


entrada2 = '7 3'.split()
x2, y2 = map(int, entrada2)
print(x2, y2)


numeros = "3 7 10".split()
numeros_int = list(map(int, numeros))
print(numeros_int)  # [3, 7, 10]