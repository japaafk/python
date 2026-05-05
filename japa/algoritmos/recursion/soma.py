# SOMA DE ITENS DE UMA LISTA POR MEIO DA RECURSÃO
lista = [2, 4, 5, 2]

def soma(array):
    if len(array) == 0:
        return 0
    else:
        return array[0] + soma(array[1:])

print(soma(lista))