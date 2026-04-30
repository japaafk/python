lista_nome = []
lista_email = []
lista_senha = []

def add_user():
    print("Adicione um novo usuário!")
    nome = input("Nome: ")
    email = input("Email: ").strip()
    senha = input("Senha: ").strip()

    lista_nome.append(nome)
    lista_email.append(email)
    lista_senha.append(senha)