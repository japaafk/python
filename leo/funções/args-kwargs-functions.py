#  *args  RECEBE VARIOS VALORES INDENPENDENTE DA QUANTIDADE

n1 = float(input("Digite uma nota: "))
n2 = float(input("Digite outra nota: "))
n3 = float(input("Digite uma terceira nota: "))


def media_aluno(*nota):
    soma = sum(nota)
    media = soma / 3 
    return media

resultado = media_aluno(n1, n2, n3)

print("A média do aluno é: ", resultado)



print("-------------------------------------------------------------------")
#  **kawargs  RECEBE DIVERSAS CHAVES E VALORES INDEPENDENTE DA QUANTIDADE



def dados(**pessoa):
    for chave, valor in pessoa.items():
        print(chave, ":", valor)

dados(nome = "leoanardo", cidade = "aracatuba", idade = 18)