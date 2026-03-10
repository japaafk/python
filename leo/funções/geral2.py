def somar_lista(numeros):
    soma = 0
    for numero in numeros:
        soma = soma + numero
    return  soma 
numero = [9, 8, 6 ,4]
soma_lista = somar_lista(numero)
print(f"o reultado é {soma_lista}")