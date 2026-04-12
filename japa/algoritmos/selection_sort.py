lista_desordenada = [12, 43, 22, 91, 55, 3]
def buscarmenor(array):
    menor = array[0]
    menor_index = 0
    for i in range(1, len(array)):
        if array[i] < menor:
            menor = array[i]
            menor_index = i
    return menor_index

def ordenacaoSelecao(array):
    novoArray = []
    for j in range(len(array)):
        menor = buscarmenor(array)
        novoArray.append(array.pop(menor)) # .pop() pega a posição pelo index
    return novoArray

print(ordenacaoSelecao(lista_desordenada))