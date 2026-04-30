from cadastro import lista_nome, lista_email
def lista_users():
    users = {
        'Usuários' : lista_nome,
        'Emails' : lista_email
    }
    print(users)