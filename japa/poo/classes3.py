class Canal:
    def __init__(self, nome, desc, inscritos):
        self.nome = nome # instância
        self.desc = desc # instância
        self.inscr = inscritos # instância

    def __repr__(self): # é executado ao chamar uma variável dessa classe em formato de string
        return f'<{self.nome}>'

    def inscrever(self, quantidade=1): # caso não seja informado a quantidade, por padrão tem valor 1
        self.inscr += quantidade

class CanalEmpresarial(Canal):
    def __init__(self, nome, desc, inscritos):
        super().__init__(nome, desc, inscritos) # super() se refere à classe pai (Canal)
        self._equipe = []  # encapsulamento
        # _ é uma convenção para dizer que essa propriedade não deve ser mexida diretamente

    def adicionar_membro(self, membro):
        if membro not in self._equipe:
            self._equipe.append(membro)
        else:
            print(f'O membro "{membro}" ja está na equipe')

    def remover_membro(self, membro):
        if membro in self._equipe:
            self._equipe.remove(membro)
        else:
            print(f'O membro "{membro}" não está na equipe')

    def time_do_canal(self):
        return self._equipe

# testando as funcionalidades básicas de uma classe
print('\nNomes dos canais:')
meu_canal = Canal('Poneis du grau', 'esportes e computadores', 5000)
canal_guanabara = Canal('Curso em Video', 'paixão por ensinar', 2500000)
# print(meu_canal.nome)
# print(canal_guanabara.nome)
# uma outra alternativa para mostrar os nomes é dar esse tipo de print
print(meu_canal) # saida sem o método __repr__: <__main__.Canal object at 0x000002B401D76A50>
print(canal_guanabara) # saida sem o metódo __repr__: <__main__.Canal object at 0x000002B402034B90>


print('\n')

print(f'Quantidade de inscritos do meu canal: {meu_canal.inscr}')
meu_canal.inscrever()
print(f'Quantidade de inscritos do meu canal: {meu_canal.inscr}')
print('--------------------------------------------------------')
print(f'Quantidade de inscritos do canal guanabara: {canal_guanabara.inscr}')
meu_canal.inscrever(300)
print(f'Quantidade de inscritos do canal guanabara: {canal_guanabara.inscr}\n')

# analisando a herança do CanalEmpresarial pela classe Canal
print('\nCanal empresarial:')
canal_duolingo = CanalEmpresarial('Duolingo', 'curso de ingles', 450000)
print(canal_duolingo.nome)

# observando as propriedades do encapsulamento
print(f'Membros da equipe: {canal_duolingo.time_do_canal()}\n')

print('Adição do membro: joão')
canal_duolingo.adicionar_membro('joão')
print(f'Membros da equipe: {canal_duolingo.time_do_canal()}\n')
print('Adição do membro: miguel')
canal_duolingo.adicionar_membro('miguel')
print(f'Membros da equipe: {canal_duolingo.time_do_canal()}\n')
print('Adição do membro: miguel')
canal_duolingo.adicionar_membro('miguel')
print(f'Membros da equipe: {canal_duolingo.time_do_canal()}\n')
print('Adição do membro: pedro')
canal_duolingo.adicionar_membro('pedro')
print(f'Membros da equipe: {canal_duolingo.time_do_canal()}\n')

print('Remoção do membro: pedro')
canal_duolingo.remover_membro('pedro')
print(f'Membros da equipe: {canal_duolingo.time_do_canal()}\n')
print('Remoção do membro: pedro')
canal_duolingo.remover_membro('pedro')
print(f'Membros da equipe: {canal_duolingo.time_do_canal()}\n')