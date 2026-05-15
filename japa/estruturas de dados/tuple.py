# tupla é uma estrutura de dados em Python usada para armazenar uma coleção ordenada de itens
# tuplas são IMUTÁVEIS

pessoas = [
    ("Arthur", 2008),
    ("João", 2008),
    ("Makino", 2007),
    ("Leo", 2007)
]

for amigo, nascimento in pessoas:
    print(f"No ano {nascimento}, {amigo} estava nascendo")