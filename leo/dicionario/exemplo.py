aluno = {
    "nome": "leo",
    "idade": 18,
    "nota": 8.5
    }
print("nome:", aluno["nome"])
print("nota:", aluno["nota"])

aluno["curso"] = "engenharia"
for chave,valor in aluno.items():
    print(chave,":", valor)

 #   Existem 3 formas comuns de percorrer um dicionário:


 #   for chave in aluno:    # SÓ AS CHAVES
 #   for valor in aluno:    # SÓ OS VALORES 
 #   for chave,valor in aluno:   # CHAVES E VALORES