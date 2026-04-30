from cadastro import lista_nome
def alteracao_perfil():
    perfil = input("Digite seu perfil: ")
    for i in range(len(lista_nome)):
        if lista_nome[i] == perfil:
            perfil = input("Digite seu novo nome de usuário: ")
            lista_nome[i] = perfil
        else:
            i += 1