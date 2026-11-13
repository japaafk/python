# CONTAGEM DO NÚMERO DE ITENS DE UM ARRY
def contador(arr):
    cont = 0
    if arr[0:] == arr[::-1]:
        return 1
    cont += 1
    return cont + contador(arr[1:])


array_exemplo = [0, 1, 2, 3, 5]

print(contador(array_exemplo))
