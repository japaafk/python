try:
    n1 = int(input('Primeiro número: '))
    n2 = int(input('Segundo número: '))
    resultado = n1 / n2
    print(resultado)
except ValueError:
    print('É preciso que um número seja digitado!')
except ZeroDivisionError:
    print('Números não podem ser divididos por zero!')