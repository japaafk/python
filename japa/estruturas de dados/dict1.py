# APLICANDO UM DICIONÁRIO DENTRO DE UMA LISTA, PERMITINDO UMA ORGANIZAÇÃO MAIS DINÂMICA DE DADOS
pessoas = [
    {'nome': 'Matheus', 'numero': '1899332085', 'email': 'nadaave2026@gmail.com'}, # dict 1
    {'nome': 'Tevo', 'numero': '17993357789'}, # dict 2
    {'nome': 'Leo', 'numero': '18990045678'} # dict 3
]

nome = input('Nome: ')

for individuo in pessoas:
    if individuo['nome'] == nome:
        numero = individuo['numero']
        print('Encontrado')
        print(f'Nome: {individuo['nome']};\nNumero: {numero}.')
        break
else:
    print('Não encontrado')