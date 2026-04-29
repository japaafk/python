# The enumarate package works: Em vez de criar uma variável de contador manual (como i = 0 e depois i += 1), o enumerate() faz isso de forma automática e elegante.
frutas = ['banana', 'maca', 'uva']

for index, fruta in enumerate(frutas):
    print(f'Index: {index}, fruta: {fruta}')

    