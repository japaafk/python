# A função enumerate serve para percorrer uma sequência (lista, tupla, string, etc.) enquanto você acompanha o índice de cada elemento.
frutas = ['banana', 'maçã', 'pêra', 'morango']
for index, item in enumerate(frutas):
    print(index, item) # ele junta índice + valor

print('\n')

aparelhos = ['smartphone', 'notebook', 'tevelisão', 'rádio']
for index, item in enumerate(aparelhos, start=1): # start é o índice inicial, seu uso é totalmente opicional
    print(index, item)