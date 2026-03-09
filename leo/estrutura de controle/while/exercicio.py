while True:
    V1 = int(input('Digite um valor: '))
    V2 = int(input('Digite outro valor: '))
    print('Escolha uma dessas opções: ')
    print('[1] Para somar')
    print('[2] Para multiplicar')
    print('[3] Para maior')
    print('[4] Novos numeros')
    print('[5] Sair do programa')
    opcao=int(input('Qual você irá escolher?: '))
    if opcao == 1:
            print(f'a soma entre {V1} + {V2} é igual a {V1+V2}')
            break

    elif opcao == 2:
            print (f'A multiplicação entre {V1} x {V2} é igual a {V1*V2}')
            break

    elif opcao == 3:
        if V1>V2:
            maior= V1
        else:
                maior = V2
                print(f'Entre {V1} e {V2} o maior valor é {maior}')
                break

    elif opcao == 4:
        continue

    elif opcao == 5:
            print('Terminando...')
            break

    else:
        print('opção não disponivel')
    print('=-='*10)
print('Finalizado! Volte sempre')