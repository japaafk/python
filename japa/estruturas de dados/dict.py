user_id = input('Digite o seu nome: ')
age = int(input('Digite sua idade: '))
weight = float(input('Seu peso: '))

# dicionários idetificam elementos por nomes e não por números como as listas
pessoas = {
            'nome': user_id, # chave: valor
            'idade': age,
            'peso': weight,
           }

print('\n')
print(pessoas.keys()) # vai me dar a identificação do elemento
print('\n')
print(pessoas.values()) # vai me dar o valor
print('\n')
print(pessoas.items()) # vai me dar tanto a identificação quanto o valor
print('\n')
print(pessoas)
print('\n')
print(pessoas.get('idade', 'a variável idade não existe')) # a vantagem dessa forma é que você pode definir um valor padrão, assim não haverá erro se a chave não existir.
print('\n')
print(pessoas.update({'nome': 'Fulaninho', 'altura': 1.8})) # este método atualiza os pares chave-valor com os pares chave-valor de outro dicionário. Se eles tiverem chaves em comum, seus valores serão sobrescritos.
print('\n')
print(pessoas)

# pessoas.clear() - método para remoção de todos chave-valor do dicionário