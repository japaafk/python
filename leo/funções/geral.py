# def CRIA UMA FUNÇÃO ONDE REALIZA UMA AÇÃO ESPECIFICA E PODE SER USADO VARIAS VEZES NO MESMO CODIGO
# USADO PARA EVITAR REPITIÇÃO, ORGANIZAÇÃO DO CODIGO E FACILIDADE NA LEITURA
# 
# def nome_funcao():

def comprimento():
    nome = "leo"
    print(f"olá, tudo bem! Pazer {nome}")

def soma(x,y):
    resultado = x + y
    return resultado

resultado_da_soma = soma(20, 10)
print(resultado_da_soma)


def verificar_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False
    
if verificar_par(7):
        print(" é par")
else:
        print(" é impar")

def somar_lista(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
        return  resultado

soma_lista = somar_lista(6, 7, 2, 9)
print(f"o reultado é {soma_lista}")