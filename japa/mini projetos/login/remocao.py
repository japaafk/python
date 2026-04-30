from cadastro import *
def user_remove():
    print("Neste momento você irá remover a sua conta da lista de usuários, esteja ciente disso")
    perfil = input("Nome do usuário: ")
    email = input("Email: ")
    if perfil in lista_nome and email in lista_email:
        lista_nome.remove(perfil)
        lista_email.remove(email)
        print("Sua conta foi removida com sucesso")
        print(lista_nome)
        print(lista_email)
    else:
        print("Usuário não encontrado :(")