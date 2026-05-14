nomes = ["Matheus", "João", "Estevão", "Leonardo"]

nome = input("Digite um nome: ")

for n in nomes:
    if nome == n:
        print("Encontrei")
        break # precisa de um break, caso contrário, também vai rodar a cláusula "else"
else: # as estruturas "for" também podem receber cláusulas "else"
    print("Não encontrei")