from cadastro import *
from lista_de_usuario import *
from alteracao import *
from remocao import *

print("-"*30)
print("CADASTROS, LOGINS E LISTAS DE USUÁRIOS")
print("-"*30)
print("SEJA BEM-VINDO, INICIE SE CADASTRANDO EM NOSSO SISTEMA")

while True:
    print("ESCOLHA O QUE DESEJA FAZER:")
    print("1- Adicione um novo usuário")
    print("2- Analisar lista de usuários cadastrados")
    print("3- Alterar perfil")
    print("4- Remover conta")
    menu_c = str(input("R: ")).strip().lower()

    match menu_c:
        case "1" | "adiconar usuário" | "adicionar usuario":
            add_user()
        case "2" | "analisar lista":
            lista_users()
        case "3" | "alterar perfil":
            alteracao_perfil()
        case "4" | "remover conta":
            user_remove()
        case _:
            print("Essa resposta não existe!")

    run_code = input("Gostaria de continuar no programa? ").lower()
    if run_code == "não" or run_code == "nao":
        break
    else:
        continue

print("Obrigado por se cadastrar!")