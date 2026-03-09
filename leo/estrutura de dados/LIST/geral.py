# O LIST É UMA ESTRUTURA USADA PARA ARMAZENAR VARIAS VALORES EM UMA SÓ VARIAVEL
# SUA ORDEM DE VARIAVEL PODE SER ALTERADA A QUALQUER HORA E PODE TEER VARIOS TIPOS DE DADOS
# A LISTA É CRIADA USANDO OS COLCHETES []

times =["Palmeiras", "São Paulo", "Corinthians" ]
numeros = ["1, 2, 3, 4, 5"]

# CADA ELEMENTO DA VARIAVEL TEM UM INDICE COMEÇANDO  DO 0 COMO POR EXEMPLOS EM TIMES => 0 = PALMEIRAS, 1 = SÃO PAULO, 2 = CORINTHIANS
print(times[0]) # A SAIDA SERA PALMEIRAS

print(times[2]) # A SAIDA SERA CORINTHIANS


# PRICIPAIS FUNÇÕES
# 1° FUNÇÃO 
append() #ADICIONA UM ELEMENTO AO FINAL DA LISTA

frutas = ["maça" , "pera"]
frutas.append("laranja")
# APÓS ISSO OS VALORES DE FRUTAS SERÃO ["maça" ,"pera", "laranja"]

# 2° FUNÇÃO
insert() # ADICIONA UM ELEMENTO EM UMA POSIÇÃO ESPECIFICA

frutas = ["maça" , "pera"]
frutas.insert(1,"uva")
# APÓS ISSO OS VALORES DE FRUTAS SERÃO ['maçã', 'uva', 'banana']

# 3° FUNÇÃO
remove() # REMOVE UM VALOR ESPECIFICO

frutas = ["maçã", "banana", "laranja"]
frutas.remove("banana")
# APÓS ISSO OS VALORES DE FRUTAS SERÃO ['maçã', 'laranja']

# 4° FUNÇÃO
pop() # REMOVE O ELEMENTO PELO INDICE

frutas = ["maçã", "banana", "laranja"]
frutas.pop(1)
# APÓS ISSO OS VALORELS DE FRUTAS SERÃO ['maçã', 'laranja']
# SE NAO USAR O INDICE REMOVE O ULTIMO ELEMENTO

# 5° FUNÇÃO
len() # MOSTRA QUANTOS ELEMENTOS EXISTEM NA LISTA
frutas = ["maçã", "banana", "laranja"]
print(len(frutas))
# APÓS ISSO A SAIDA SERÁ 3, POIS EXISTEM 3 ELEMENTOS NA LISTA FRUTAS

# 6° FUNÇÃO
sort() # ORGANIZA A ORDEM DA LISTA DE ORDEM CRESCENTE DE ACORDO COM O INDICE
numeros = [5, 1, 3, 2]
numeros.sort()
# APÓS ISSO A ORDEM DO INDICE SERA [ 1, 2, 3, 5 ] 

# 7° FUNÇÃO
reverse() # INVERTE A ORDEM DA LISTA
numeros = [1, 2, 3] 
numeros.reverse()
# APÓS ISSO A ORDEM DA LISTA SERÁ [3, 2, 1]
