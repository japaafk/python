# Os set() são mutáveis ​​e não ordenados, o que significa que seus elementos não são armazenados em nenhuma ordem específica, portanto, você não pode usar índices ou chaves para acessá-los
# set() também não recebem elementos duplicados 

meu_set = {1, 2, 3, 4, 5}
seu_set = {2, 3, 4, 6}

meu_set.add(6) # adiciona o número 6 dentro dele
meu_set.add(5) # não vai mudar nada porque já temos o número 5 dentro dele
print(meu_set)

# remoção de algum valor
meu_set.remove(6) # a única diferença entre eles é que caso a função .remove() vai mostrar KeyError caso o elemento são seja achado
meu_set.discard(6)
print(meu_set)

# meu_set.clear() - remove todos os elementos do set

# Os métodos .issubset() e .issuperset() verificam se um set é subconjunto ou superconjunto de outro set, respectivamente.
print(f'função .issubset(): {seu_set.issubset(meu_set)}') # False - porque nem todos os elementos do seu_set estão no meu_set
print(f'função .issuperset(): {meu_set.issuperset(seu_set)}') # False - porque meu_set não todos os elementos presentes no seu_set

# O método .isdisjoint() verifica se dois set são disjuntos, ou seja, se não possuem elementos em comum.
print(f'função .isdisjoint(): {meu_set.isdisjoint(seu_set)}') # False - pois meu_set e seu_set possuem elementos em comum: 2, 3 e 4

# o operador "|" retorna um novo set com todos os elementos dos dois sets
print(f'operador "|", novo set: {meu_set | seu_set}')

# o operador "&" retorna um novo set com os valores comuns entre os sets
print(f'operador "&", novo set: {meu_set & seu_set}')

# o operador "-" retorna um novo set com os elementos do primeiro set que não estão presentes nos outros sets
print(f'operador "-", novo set: {meu_set - seu_set}')

# o operador "^" retorna um novo set com os elementos que estão presentes no primeiro ou no segundo set, mas não em ambos
print(f'operador "^", novo set: {meu_set ^ seu_set}')