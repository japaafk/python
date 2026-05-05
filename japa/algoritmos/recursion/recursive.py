def contagem_regressiva(numero):
    print(numero)
    if numero < 1: # CASO BASE - IMPEDE QUE A FUNÇÃO ENTRE EM UM LOOP INFINITO
        quit
    else:
        contagem_regressiva(numero - 1) # CASO RECURSIVO -  A FUNÇÃO CHAMA A SI PRÓPRIA

number = int(input("Digite seu número: "))
contagem_regressiva(number)