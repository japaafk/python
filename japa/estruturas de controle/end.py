resultado = 1
numero = int(input('Digite o valor: '))
for i in range(numero, 0, -1):
    #print(resultado)
    print(f'{i}', end='') # definindo o que será colocado no final da impressão
    print(' x ' if i > 1 else ' = ', end='')
    resultado = resultado * i
    i -= 1
print(resultado)