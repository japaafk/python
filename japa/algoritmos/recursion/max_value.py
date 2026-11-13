# ENCONTRANDO O VALOR MÁXIMO DE UM ARRAY
def ValorMaximo(arr):
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    sub_max = ValorMaximo(arr[1:])
    return arr[0] if arr[0] > sub_max else sub_max


lista = [1, 3, 5, 2, 9, 7]
print(ValorMaximo(lista))